from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import date
from .models import ContactMessage
from .models import Job,Feedback
from .models import QuizQuestion

from .models import (
    Job,
    Subscriber,
    QuizQuestion,
    QuizAttempt,
    ContactMessage,
    Feedback
)



# ================= HOME PAGE =================


def home(request):

    central_jobs = Job.objects.filter(job_type="Central").order_by("-created_at")[:6]

    telangana_jobs = Job.objects.filter(job_type="Telangana").order_by("-created_at")[:6]

    my_feedbacks = []

    if request.user.is_authenticated:
        my_feedbacks = Feedback.objects.filter(user=request.user).order_by("-created_at")

    context = {
        "central_jobs": central_jobs,
        "telangana_jobs": telangana_jobs,
        "my_feedbacks": my_feedbacks,
    }

    return render(request, "jobportal/home.html", context)

# ================= LOGIN =================


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user:

            login(request,user)

            return redirect("home")


        else:

            messages.error(
                request,
                "Invalid username or password"
            )


    return render(
        request,
        "jobportal/login.html"
    )




# ================= REGISTER =================


def register_view(request):

    if request.method=="POST":

        username=request.POST.get("username")

        email=request.POST.get("email")

        password=request.POST.get("password")

        confirm=request.POST.get("confirm_password")



        if password != confirm:

            messages.error(
                request,
                "Passwords do not match"
            )

            return redirect("register")



        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect("register")



        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        messages.success(
            request,
            "Registration successful"
        )


        return redirect("login")



    return render(
        request,
        "jobportal/register.html"
    )




# ================= STATIC PAGES =================


def latest_jobs(request):
    return render(
        request,
        "jobportal/latest_jobs.html"
    )



def results(request):
    return render(
        request,
        "jobportal/results.html"
    )



def admit_cards(request):
    return render(
        request,
        "jobportal/admit_cards.html"
    )



def answer_keys(request):

    return render(
        request,
        "jobportal/answer_keys.html"
    )



def notifications(request):

    return render(
        request,
        "jobportal/notifications.html"
    )



def previous_papers(request):

    return render(
        request,
        "jobportal/previous_papers.html"
    )



def current_affairs(request):

    return render(
        request,
        "jobportal/current_affairs.html"
    )



def saved_jobs(request):

    return render(
        request,
        "jobportal/saved_jobs.html"
    )



def about(request):

    return render(
        request,
        "jobportal/about.html"
    )



def faq(request):

    return render(
        request,
        "jobportal/faq.html"
    )



def dashboard(request):

    return render(
        request,
        "jobportal/dashboard.html"
    )



# ================= CONTACT =================


def contact(request):

    if request.method=="POST":


        subject=request.POST.get("subject")

        message=request.POST.get("message")



        reply = (

            "Thank you for contacting Govt Jobs Portal.\n\n"

            "We received your request.\n\n"

            "Latest government job notifications are updated regularly."

        )



        ContactMessage.objects.create(

            user=request.user 
            if request.user.is_authenticated 
            else None,

            name=request.POST.get("name"),

            email=request.POST.get("email"),

            mobile=request.POST.get("mobile"),

            subject=subject,

            message=message,

            admin_reply=reply,

            status="Replied"

        )



        messages.success(
            request,
            "Message submitted successfully"
        )

        return redirect("contact")

    return render(
        request,
        "jobportal/contact.html"
    )




# ================= FEEDBACK =================


def feedback(request):
    if request.method == "POST":
        Feedback.objects.create(
            user=request.user if request.user.is_authenticated else None,
            name=request.POST["name"],
            email=request.POST["email"],
            rating=request.POST["rating"],
            message=request.POST["message"],
        )

        messages.success(request, "Thank you for your feedback.")

    return render(request, "jobportal/feedback.html")



# ================= SUBSCRIBE =================


def subscribe(request):

    if request.method=="POST":

        email=request.POST.get("email")


        if not Subscriber.objects.filter(
            email=email
        ).exists():


            Subscriber.objects.create(
                email=email
            )


            messages.success(
                request,
                "Subscribed successfully"
            )


        else:

            messages.warning(
                request,
                "Email already subscribed"
            )


    return redirect("home")




# ================= DAILY QUIZ =================

@login_required
def daily_quiz(request):

    questions = QuizQuestion.objects.all()[:20]
    total = questions.count()

    if request.method == "POST":

        score = 0
        wrong = 0
        results = []

        for question in questions:

            user_answer = request.POST.get(f"q{question.id}")

            is_correct = user_answer == question.answer

            if is_correct:
                score += 1
            else:
                wrong += 1

            results.append({
                "question": question.question,
                "user_answer": user_answer if user_answer else "Not Answered",
                "correct_answer": question.answer,
                "correct": is_correct,
            })

        return render(
            request,
            "jobportal/quiz_result.html",
            {
                "score": score,
                "wrong": wrong,
                "correct": score,
                "total": total,
                "results": results,
            },
        )

    return render(
        request,
        "jobportal/daily_quiz.html",
        {
            "questions": questions,
            "total": total,
        },
    )
# ================= SCORE HISTORY =================

@login_required(login_url="login")
def score_history(request):

    attempts = QuizAttempt.objects.filter(
        user=request.user
    ).order_by("-attempted_date")



    return render(

        request,

        "jobportal/score_history.html",

        {

            "attempts":attempts

        }

    )




# ================= MY QUERIES =================


@login_required(login_url="login")
def my_queries(request):

    print("Current User:", request.user)
    print("User ID:", request.user.id)

    queries = ContactMessage.objects.filter(user=request.user).order_by("-created_at")

    print("Queries Count:", queries.count())

    return render(
        request,
        "jobportal/my_queries.html",
        {
            "queries": queries
        }
    )

# ================= JOB DETAILS PAGES =================


def tgpsc_group_1(request):

    return render(
        request,
        "jobportal/tgpsc_group_1.html"
    )



def ssc_cgl(request):

    return render(
        request,
        "jobportal/ssc_cgl.html"
    )



def railway_group_d(request):

    return render(
        request,
        "jobportal/railway_group_d.html"
    )



# ================= RESULT PAGES =================


def ssc_cgl_result(request):

    return render(
        request,
        "jobportal/ssc_cgl_result.html"
    )



def tgpsc_result(request):

    return render(
        request,
        "jobportal/tgpsc_result.html"
    )



def railway_result(request):

    return render(
        request,
        "jobportal/railway_result.html"
    )

def search(request):
    query = request.GET.get("q", "").strip()

    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(organization__icontains=query) |
            Q(job_type__icontains=query) |
            Q(category__icontains=query) |
            Q(state__icontains=query) |
            Q(location__icontains=query) |
            Q(qualification__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, "jobportal/search.html", {
        "jobs": jobs,
        "query": query,
    })

@login_required
def my_feedback(request):
    feedbacks = Feedback.objects.filter(user=request.user).order_by("-id")
    return render(request, "jobportal/my_feedback.html", {
        "my_feedbacks": feedbacks
    })
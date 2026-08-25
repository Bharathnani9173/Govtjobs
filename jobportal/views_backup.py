from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import date
from .models import ContactMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Job
import os
from django.conf import settings
from django.templatetags.static import static
from django.http import FileResponse, Http404
from django.urls import reverse


from .models import (
    Job,
    Subscriber,
    QuizQuestion,
    QuizAttempt,
    ContactMessage,
    Feedback,
     PreviousPaper,
    AnswerKey,
    CurrentAffair,
    Syllabus,
    MockTest,
    MockTestQuestion,
)

RESOURCE_CATEGORY_MAP = {

"SSC": [
    "SSC",
    "General Knowledge",
    "Current Affairs",
    "Aptitude",
    "Reasoning",
    "English",
    "Computer",
],

"UPSC": [
    "UPSC",
    "General Knowledge",
    "Current Affairs",
    "Polity",
    "History",
    "Geography",
],

"Railway": [
    "Railway",
    "General Knowledge",
    "Current Affairs",
    "Aptitude",
    "Reasoning",
    "General Science",
],

"Bank": [
    "Bank",
    "Current Affairs",
    "Aptitude",
    "Reasoning",
    "English",
    "Computer",
],

"Police": [
    "Police",
    "Current Affairs",
    "General Knowledge",
    "Reasoning",
    "Aptitude",
],

"Defence": [
    "Defence",
    "Current Affairs",
    "General Knowledge",
    "Reasoning",
    "Aptitude",
],

"Teaching": [
    "Teaching",
    "Current Affairs",
    "General Knowledge",
    "Reasoning",
    "English",
],

"PSU": [
    "PSU",
    "Current Affairs",
    "General Knowledge",
    "Aptitude",
    "Reasoning",
],

"State PSC": [
    "State PSC",
    "Current Affairs",
    "General Knowledge",
    "State GK",
    "Reasoning",
],

"High Court": [
    "High Court",
    "Current Affairs",
    "General Knowledge",
    "Reasoning",
    "English",
],

"Health": [
    "Health",
    "Current Affairs",
    "General Knowledge",
    "Reasoning",
],

"Other": [
    "General Knowledge",
    "Current Affairs",
    "Aptitude",
    "Reasoning",
    "English",
],

}


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

def notifications(request):

    return render(
        request,
        "jobportal/notifications.html"
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

@login_required(login_url="login")
def daily_quiz(request):

    today = timezone.now().date()

    # ==========================================
    # CHECK IF USER ALREADY ATTEMPTED TODAY
    # ==========================================

    already_attempted = QuizAttempt.objects.filter(
        user=request.user,
        attempted_date=today
    ).exists()

    if already_attempted and request.method == "GET":

        return render(
            request,
            "jobportal/already_attempted.html"
        )

    # ==========================================
    # SUBMIT QUIZ
    # ==========================================

    if request.method == "POST":

        question_ids = request.POST.getlist(
            "question_ids"
        )

        questions = QuizQuestion.objects.filter(
            id__in=question_ids
        )

        question_dict = {
            str(q.id): q
            for q in questions
        }

        ordered_questions = []

        for qid in question_ids:

            if qid in question_dict:

                ordered_questions.append(
                    question_dict[qid]
                )

        score = 0
        wrong = 0
        results = []

        for question in ordered_questions:

            user_answer = request.POST.get(
                f"q{question.id}"
            )

            correct_answer = question.answer

            is_correct = (
                user_answer is not None
                and str(user_answer).strip().lower()
                == str(correct_answer).strip().lower()
            )

            if is_correct:
                score += 1
            else:
                wrong += 1

            results.append({
                "question": question.question,

                "user_answer": (
                    user_answer
                    if user_answer
                    else "Not Answered"
                ),

                "correct_answer": correct_answer,

                "correct": is_correct,
            })

        total = len(ordered_questions)

        # ==========================================
        # SAVE ATTEMPT
        # ==========================================

        QuizAttempt.objects.create(
            user=request.user,
            score=score,
            total_questions=total,
            time_taken=0,
            question_ids=[
                q.id
                for q in ordered_questions
            ]
        )

        return render(
            request,
            "jobportal/quiz_result.html",
            {
                "score": score,
                "correct": score,
                "wrong": wrong,
                "total": total,
                "results": results,
            }
        )

    # ==========================================
    # GET QUESTIONS FOR TODAY
    # ==========================================

    # Get question IDs used in previous attempts
    previous_attempts = QuizAttempt.objects.exclude(
        attempted_date=today
    ).values_list(
        "question_ids",
        flat=True
    )

    used_question_ids = set()

    for ids in previous_attempts:

        if ids:

            used_question_ids.update(ids)

    # ==========================================
    # GET QUESTIONS NOT USED BEFORE
    # ==========================================

    available_questions = QuizQuestion.objects.exclude(
        id__in=used_question_ids
    )

    # Random 20 questions
    questions = list(
        available_questions.order_by("?")[:20]
    )

    # ==========================================
    # IF LESS THAN 20 UNUSED QUESTIONS
    # ==========================================

    if len(questions) < 20:

        # Start using the full question bank again
        questions = list(
            QuizQuestion.objects.order_by("?")[:20]
        )

    total = len(questions)

    return render(
        request,
        "jobportal/daily_quiz.html",
        {
            "questions": questions,
            "total": total,
        }
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

# ================= EXAM DASHBOARD =================

def exam_dashboard(request, job_id):
    jobs = Job.objects.all().order_by("-created_at")

    return render(
        request,
        "jobportal/exam_dashboard.html",
        {"jobs": jobs}
    )

@login_required
def exam_dashboard_list(request):

    jobs = Job.objects.all().order_by("-created_at")

    return render(
        request,
        "jobportal/exam_dashboard_list.html",
        {
            "jobs": jobs,
        }
    )

# ================= JOB DETAILS =================
def job_detail(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    return render(
        request,
        "jobportal/job_detail.html",
        {
            "job": job
        }
    )

def previous_papers(request):

    job_id = request.GET.get("job")

    if not job_id:
        return redirect("exam_dashboard_list")

    job = get_object_or_404(Job, id=job_id)

    # ---------------------------------
    # DETERMINE PDF FOLDER FROM JOB
    # ---------------------------------

    text = " ".join([
        str(job.title or ""),
        str(job.organization or ""),
        str(job.category or ""),
    ]).lower()

    folder = "other"

    if "ssc cgl" in text or "combined graduate" in text:
        folder = "ssc_cgl"

    elif "ssc chsl" in text or "combined higher secondary" in text:
        folder = "ssc_chsl"

    elif "ssc gd" in text:
        folder = "ssc_gd"

    elif "ssc mts" in text:
        folder = "ssc_mts"

    elif "ssc cpo" in text:
        folder = "ssc_cpo"

    elif "ssc je" in text:
        folder = "ssc_je"

    elif "stenographer" in text:
        folder = "ssc_stenographer"

    elif "group d" in text:
        folder = "railway_group_d"

    elif "ntpc" in text:
        folder = "railway_ntpc"

    elif "alp" in text:
        folder = "railway_alp"

    elif "technician" in text:
        folder = "railway_technician"

    elif "rrb je" in text:
        folder = "rrb_je"

    elif "sbi clerk" in text:
        folder = "sbi_clerk"

    elif "sbi po" in text:
        folder = "sbi_po"

    elif "ibps clerk" in text:
        folder = "ibps_clerk"

    elif "ibps po" in text:
        folder = "ibps_po"

    elif "ibps rrb" in text:
        folder = "ibps_rrb"

    elif "tspsc group 1" in text or "tgpsc group 1" in text:
        folder = "tspsc_group_1"

    elif "tspsc group 2" in text or "tgpsc group 2" in text:
        folder = "tspsc_group_2"

    elif "tspsc group 3" in text or "tgpsc group 3" in text:
        folder = "tspsc_group_3"

    elif "tspsc group 4" in text or "tgpsc group 4" in text:
        folder = "tspsc_group_4"

    elif "telangana police" in text:
        folder = "telangana_police"

    elif "police constable" in text:
        folder = "police_constable"

    elif "mazagon dock" in text:
        folder = "mazagon_dock"

    elif "esic" in text:
        folder = "esic"

    elif "epfo" in text:
        folder = "epfo"

    elif "lic" in text:
        folder = "lic"

    elif "post office" in text:
        folder = "post_office"

    elif "army" in text:
        folder = "army"

    elif "navy" in text:
        folder = "navy"

    elif "air force" in text:
        folder = "air_force"

    elif "tet" in text:
        folder = "tet"

    elif "dsc" in text:
        folder = "dsc"

    # ---------------------------------
    # PDF DIRECTORY
    # ---------------------------------

    pdf_directory = os.path.join(
        settings.BASE_DIR,
        "jobportal",
        "static",
        "pdfs",
        "previous_papers",
        folder,
    )

    papers = []

    if os.path.exists(pdf_directory):

        for filename in sorted(os.listdir(pdf_directory)):

            if filename.lower().endswith(".pdf"):

                papers.append({
                    "name": os.path.splitext(filename)[0],
                    "filename": filename,

                    # VIEW
                    "url": static(
                    f"pdfs/previous_papers/{folder}/{filename}"
                    ),
                })

    return render(
        request,
        "jobportal/previous_papers.html",
        {
            "job": job,
            "papers": papers,
            "folder": folder,
        },
    )

# =========================
# ANSWER KEYS
# =========================

def answer_keys(request):
    job_id = request.GET.get("job")

    if not job_id:
        return redirect("exam_dashboard_list")

    job = get_object_or_404(Job, id=job_id)

    # Only answer keys specifically linked to this job
    answer_keys_list = AnswerKey.objects.filter(
        job=job
    ).order_by("-release_date")

    return render(
        request,
        "jobportal/answer_keys.html",
        {
            "job": job,
            "answer_keys": answer_keys_list,
        }
    )


# =========================
# CURRENT AFFAIRS
# =========================

def current_affairs(request):

    job_id = request.GET.get("job")

    if not job_id:
        return redirect("exam_dashboard_list")

    job = get_object_or_404(Job, id=job_id)

    # ---------------------------------
    # CURRENT AFFAIRS PDF FOLDER
    # ---------------------------------

    pdf_directory = os.path.join(
        settings.BASE_DIR,
        "jobportal",
        "static",
        "pdfs",
        "current_affairs",
    )

    affairs = []

    # ---------------------------------
    # READ ALL PDF FILES
    # ---------------------------------

    if os.path.exists(pdf_directory):

        for filename in sorted(
            os.listdir(pdf_directory),
            reverse=True
        ):

            if filename.lower().endswith(".pdf"):

                file_path = os.path.join(
                    pdf_directory,
                    filename
                )

                # Ignore empty files
                if os.path.getsize(file_path) == 0:
                    continue

                # Remove .pdf extension
                title = os.path.splitext(filename)[0]

                # Make filename look nicer
                title = title.replace("_", " ")

                affairs.append({
                    "title": title,
                    "date": "",
                    "category": "SSC",
                    "description": f"Current Affairs PDF for {job.title}",
                    "pdf_link": static(
                        f"pdfs/current_affairs/{filename}"
                    ),
                })

    # ---------------------------------
    # PAGE
    # ---------------------------------

    return render(
        request,
        "jobportal/current_affairs.html",
        {
            "job": job,
            "affairs": affairs,
        },
    )

# =========================
# SYLLABUS
# =========================

def syllabus(request):
    job_id = request.GET.get("job")

    if not job_id:
        return redirect("exam_dashboard_list")

    job = get_object_or_404(Job, id=job_id)

    # One syllabus is associated with one job
    syllabus_obj = Syllabus.objects.filter(
        job=job
    ).first()

    return render(
        request,
        "jobportal/syllabus.html",
        {
            "job": job,
            "syllabus": syllabus_obj,
        }
    )


@login_required
def mock_test(request):

    job_id = request.GET.get("job")

    if not job_id:
        return redirect("exam_dashboard_list")

    job = get_object_or_404(Job, id=job_id)

    # =====================================================
    # SUBMIT MOCK TEST
    # =====================================================

    if request.method == "POST":

        question_ids = request.POST.get("question_ids", "")

        if question_ids:
            ids = [
                int(x)
                for x in question_ids.split(",")
                if x.isdigit()
            ]
        else:
            ids = []

        questions = QuizQuestion.objects.filter(
            id__in=ids,
            job=job
        )

        score = 0
        attempted = 0
        results = []

        for question in questions:

            selected_answer = request.POST.get(
                f"question_{question.id}"
            )

            if selected_answer:
                attempted += 1

            correct = False

            if selected_answer:
                if (
                    selected_answer.strip().lower()
                    ==
                    question.answer.strip().lower()
                ):
                    score += 1
                    correct = True

            results.append({
                "question": question.question,
                "user_answer": selected_answer,
                "correct_answer": question.answer,
                "correct": correct,
            })

        total = questions.count()

        wrong = attempted - score
        unanswered = total - attempted

        # Save attempt
        QuizAttempt.objects.create(
            user=request.user,
            score=score,
            total_questions=total,
            time_taken=0,
            question_ids=ids,
        )

        return render(
            request,
            "jobportal/mock_test_result.html",
            {
                "job": job,
                "score": score,
                "total": total,
                "attempted": attempted,
                "wrong": wrong,
                "unanswered": unanswered,
                "results": results,
            }
        )

    # =====================================================
    # START MOCK TEST
    # =====================================================

    questions = QuizQuestion.objects.filter(
        job=job
    ).order_by("?")[:20]

    if not questions.exists():

        return render(
            request,
            "jobportal/mock_test.html",
            {
                "job": job,
                "questions": [],
                "no_questions": True,
            }
        )

    return render(
        request,
        "jobportal/mock_test.html",
        {
            "job": job,
            "questions": questions,
            "no_questions": False,
            "question_ids": ",".join(
                str(q.id) for q in questions
            ),
        }
    )

@login_required
def start_mock_test(request, test_id):

    mock_test = get_object_or_404(
        MockTest,
        id=test_id
    )

    questions = MockTestQuestion.objects.filter(
        mock_test=mock_test
    ).order_by("?")[:mock_test.total_questions]

    if request.method == "POST":

        score = 0
        results = []

        for question in questions:

            user_answer = request.POST.get(
                f"question_{question.id}"
            )

            is_correct = (
                user_answer == question.answer
            )

            if is_correct:
                score += 1

            results.append({
                "question": question.question,
                "user_answer": user_answer or "Not Answered",
                "correct_answer": question.answer,
                "correct": is_correct,
            })

        return render(
            request,
            "jobportal/mock_test_result.html",
            {
                "mock_test": mock_test,
                "score": score,
                "total": len(questions),
                "results": results,
            }
        )

    return render(
        request,
        "jobportal/start_mock_test.html",
        {
            "mock_test": mock_test,
            "questions": questions,
        }
    )

def view_pdf(request, folder, filename):

    pdf_path = os.path.join(
        settings.BASE_DIR,
        "jobportal",
        "static",
        "pdfs",
        "previous_papers",
        folder,
        filename,
    )

    if not os.path.isfile(pdf_path):
        raise Http404("PDF not found")

    response = FileResponse(
        open(pdf_path, "rb"),
        content_type="application/pdf",
    )

    response["Content-Disposition"] = f'inline; filename="{filename}"'

    return response


def download_pdf(request, folder, filename):
    pdf_path = os.path.join(
        settings.BASE_DIR,
        "jobportal",
        "static",
        "pdfs",
        "previous_papers",
        folder,
        filename,
    )

    if not os.path.isfile(pdf_path):
        raise Http404("PDF not found")

    response = FileResponse(
        open(pdf_path, "rb"),
        content_type="application/pdf",
    )

    response["Content-Disposition"] = (
        f'attachment; filename="{filename}"'
    )

    return response
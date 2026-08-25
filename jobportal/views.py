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
from pathlib import Path


from .models import (
    Job,
    Subscriber,
    QuizQuestion,
    MockTestAttempt,
    DailyMockTest,
    ContactMessage,
    Feedback,
    PreviousPaper,
    AnswerKey,
    CurrentAffair,
    Syllabus,
    MockTest,
    MockTestQuestion,
    Exam,
    QuizAttempt,
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


def generate_contact_reply(subject, message):
    text = f"{subject} {message}".lower()

    # Admit Card
    if any(word in text for word in [
        "admit card",
        "admitcard",
        "hall ticket",
        "hallticket"
    ]):
        if any(word in text for word in [
            "download",
            "downloading",
            "open",
            "not opening",
            "error",
            "issue",
            "problem",
            "not working"
        ]):
            return (
                "We’re sorry you’re experiencing a problem while downloading "
                "your admit card. We understand that the admit card is "
                "important for your examination. Please check whether the "
                "official admit card link is active and try downloading it "
                "again. We will also verify the admit card link on Govt Jobs "
                "Portal and update it if there is any problem."
            )

        return (
            "Thank you for contacting Govt Jobs Portal regarding your admit "
            "card. We have received your request and will verify the "
            "available admit card information and related link."
        )

    # Answer Key
    elif any(word in text for word in [
        "answer key",
        "answerkey",
        "answer keys"
    ]):
        if any(word in text for word in [
            "download",
            "downloading",
            "error",
            "issue",
            "problem",
            "not opening",
            "not working"
        ]):
            return (
                "We’re sorry you’re having trouble accessing or downloading "
                "the answer key. Please try downloading the answer key again "
                "after refreshing the page. We will verify the answer-key "
                "file and link and correct it if necessary."
            )

        return (
            "Thank you for reporting the answer-key issue. We have received "
            "your request and will verify the available answer key and its "
            "related information."
        )

    # Results
    elif any(word in text for word in [
        "result",
        "results",
        "score card",
        "scorecard"
    ]):
        return (
            "Thank you for reporting the result-related issue. We have "
            "received your message and will verify the result information "
            "and available result link. If the link or information is "
            "incorrect or unavailable, we will update it."
        )

    # Notifications
    elif any(word in text for word in [
        "notification",
        "notifications",
        "job notification"
    ]):
        return (
            "Thank you for reporting the notification issue. We have received "
            "your message and will verify the job notification details, "
            "availability and related links. We will update the information "
            "if any correction is required."
        )

    # Previous Papers
    elif any(word in text for word in [
        "previous paper",
        "previous papers",
        "old paper",
        "question paper",
        "previous year paper"
    ]):
        return (
            "We’re sorry you’re having trouble accessing the previous-year "
            "paper. Please try downloading the paper again. We will verify "
            "the PDF file and download link and correct the issue if "
            "necessary."
        )

    # Mock Test / Quiz
    elif any(word in text for word in [
        "mock test",
        "mocktest",
        "quiz",
        "exam test",
        "practice test"
    ]):
        return (
            "We’re sorry you’re experiencing an issue with the mock test. "
            "Please refresh the page and try the test again. We will check "
            "the mock-test questions, submission process and result "
            "calculation and resolve the issue if required."
        )

    # Login
    elif any(word in text for word in [
        "login",
        "log in",
        "sign in",
        "password"
    ]):
        return (
            "We’re sorry you’re having trouble logging in. Please verify your "
            "username and password and try again. If the problem continues, "
            "please provide the error message you are receiving so that we "
            "can investigate the issue."
        )

    # Registration
    elif any(word in text for word in [
        "register",
        "registration",
        "create account",
        "signup",
        "sign up"
    ]):
        return (
            "We’re sorry you’re having trouble with registration. Please "
            "make sure all required details are entered correctly and try "
            "again. If the issue continues, we will investigate the "
            "registration problem."
        )

    # PDF / Download
    elif any(word in text for word in [
        "pdf",
        "download",
        "downloading",
        "file",
        "document"
    ]):
        return (
            "We’re sorry you’re having trouble downloading the requested "
            "file. Please refresh the page and try again. We will verify "
            "the PDF file and download link and correct the issue if "
            "necessary."
        )

    # Search
    elif any(word in text for word in [
        "search",
        "searching",
        "job search",
        "filter"
    ]):
        return (
            "Thank you for reporting the search-related issue. Please try "
            "refreshing the page and searching again. We will check the "
            "search and filter functionality and resolve the issue if "
            "necessary."
        )

    # Job Application
    elif any(word in text for word in [
        "application",
        "apply",
        "applying",
        "application link"
    ]):
        return (
            "Thank you for reporting the job application issue. Please "
            "verify the official application link and application dates. "
            "We will check the information available on the portal and "
            "correct it if necessary."
        )

    # Website
    elif any(word in text for word in [
        "website",
        "page",
        "site",
        "not working",
        "problem",
        "issue",
        "error"
    ]):
        return (
            "Thank you for reporting this website issue. We have received "
            "your message and reviewed the issue you described. We will "
            "check the relevant section of the portal and take the "
            "necessary action to resolve it."
        )

    # Default
    return (
        "Thank you for contacting Govt Jobs Portal. We have received your "
        "message and reviewed the issue you described. We will check the "
        "relevant section of the portal and take the necessary action."
    )


# ================= CONTACT =================

def contact(request):

    if request.method == "POST":

        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        # Generate reply based on the user's actual issue
        reply = generate_contact_reply(
            subject,
            message
        )

        ContactMessage.objects.create(

            user=(
                request.user
                if request.user.is_authenticated
                else None
            ),

            name=request.POST.get("name", "").strip(),

            email=request.POST.get("email", "").strip(),

            mobile=request.POST.get("mobile", "").strip(),

            subject=subject,

            message=message,

            admin_reply=reply,

            status="Replied"
        )

        messages.success(
            request,
            "Message submitted successfully. You can view the reply in My Queries."
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
    return render(request, "jobportal/previous_papers.html")

# =========================
# ANSWER KEYS
# =========================

def answer_keys(request):

    job_id = request.GET.get("job")

    if job_id:
        job = get_object_or_404(Job, id=job_id)

        answer_keys_list = AnswerKey.objects.filter(
            job=job
        ).order_by("-release_date")

    else:
        job = None

        answer_keys_list = AnswerKey.objects.all().order_by(
            "-release_date"
        )

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

    if job_id:
        job = get_object_or_404(Job, id=job_id)

    else:
        job = None

    pdf_directory = os.path.join(
        settings.BASE_DIR,
        "jobportal",
        "static",
        "pdfs",
        "current_affairs",
    )

    affairs = []

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

                if os.path.getsize(file_path) == 0:
                    continue

                title = os.path.splitext(filename)[0]
                title = title.replace("_", " ")

                affairs.append({
                    "title": title,
                    "date": "",
                    "category": "Current Affairs",
                    "description": (
                        f"Current Affairs PDF"
                        + (f" for {job.title}" if job else "")
                    ),
                    "pdf_link": static(
                        f"pdfs/current_affairs/{filename}"
                    ),
                })

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
        return redirect("home")

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
    exam_id = request.GET.get("exam")

    if not exam_id:
        return redirect("home")

    exam = get_object_or_404(Exam, id=exam_id)

    if request.method == "POST":
        question_ids = request.POST.get("question_ids", "")

        ids = [
            int(x)
            for x in question_ids.split(",")
            if x.isdigit()
        ]

        questions = QuizQuestion.objects.filter(
            id__in=ids,
            exam=exam
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

                is_correct = (
                    selected_answer == question.answer
                )

                if is_correct:
                    score += 1

                results.append({
                    "question": question,
                    "selected": selected_answer,
                    "correct": question.answer,
                    "is_correct": is_correct,
                })

        total = questions.count()
        wrong = attempted - score
        unanswered = total - attempted

        return render(
            request,
            "jobportal/mock_test_result.html",
            {
                "exam": exam,
                "score": score,
                "total": total,
                "attempted": attempted,
                "wrong": wrong,
                "unanswered": unanswered,
                "results": results,
            }
        )

    questions = list(
        QuizQuestion.objects.filter(
            exam=exam
        ).order_by("?")[:20]
    )

    if not questions:
        return render(
            request,
            "jobportal/mock_test.html",
            {
                "exam": exam,
                "questions": [],
                "no_questions": True,
            }
        )

    return render(
        request,
        "jobportal/mock_test.html",
        {
            "exam": exam,
            "questions": questions,
            "no_questions": False,
            "question_ids": ",".join(
                str(q.id) for q in questions
            ),
        }
    )

# =========================================================
# EXAM-WISE MOCK TEST
# =========================================================

@login_required(login_url="login")
def exam_mock_test(request, exam_name):

    from django.utils import timezone
    from django.db import transaction

    today = timezone.now().date()

    # ---------------------------------------------------------
    # GET EXAM
    # ---------------------------------------------------------
    exam = get_object_or_404(
        Exam,
        name__iexact=exam_name.strip()
    )

    # ---------------------------------------------------------
    # GET ALL ACTIVE QUESTIONS FOR THIS EXAM
    # ---------------------------------------------------------
    available_questions = MockTestQuestion.objects.filter(
        exam=exam,
        exam_name__iexact=exam.name,
        is_active=True
    )

    question_count = available_questions.count()

    # ---------------------------------------------------------
    # MINIMUM 50 QUESTIONS REQUIRED
    # ---------------------------------------------------------
    if question_count < 50:

        return render(
            request,
            "jobportal/mock_test.html",
            {
                "exam": exam,
                "questions": [],
                "no_questions": True,
                "message": (
                    f"Only {question_count} questions are available "
                    f"for {exam.name}. "
                    f"At least 50 questions are required."
                ),
            }
        )

    # ---------------------------------------------------------
    # GET OR CREATE TODAY'S MOCK TEST
    # ---------------------------------------------------------
    daily_test = DailyMockTest.objects.filter(
        exam=exam,
        exam_name=exam.name,
        test_date=today
    ).first()

    # ---------------------------------------------------------
    # CREATE TODAY'S TEST IF IT DOES NOT EXIST
    # ---------------------------------------------------------
    if daily_test is None:

        # Random 50 exam-specific questions
        questions = list(
            available_questions
            .order_by("?")[:50]
        )

        daily_test = DailyMockTest.objects.create(
            exam=exam,
            exam_name=exam.name,
            test_date=today,
            title=f"{exam.name} Daily Mock Test",
            duration=20,
            total_questions=50
        )

        daily_test.questions.set(questions)

    else:

        # -----------------------------------------------------
        # GET QUESTIONS FROM TODAY'S TEST
        # -----------------------------------------------------
        questions = list(
            daily_test.questions.filter(
                exam=exam,
                exam_name__iexact=exam.name,
                is_active=True
            )
        )

        # -----------------------------------------------------
        # IF OLD DAILY TEST HAS INVALID/EMPTY QUESTIONS,
        # REBUILD IT
        # -----------------------------------------------------
        if len(questions) < 50:

            daily_test.questions.clear()

            questions = list(
                available_questions
                .order_by("?")[:50]
            )

            daily_test.questions.set(questions)

    # ---------------------------------------------------------
    # FINAL SAFETY CHECK
    # ---------------------------------------------------------
    if len(questions) < 50:

        return render(
            request,
            "jobportal/mock_test.html",
            {
                "exam": exam,
                "questions": [],
                "no_questions": True,
                "message": (
                    f"Unable to create a 50-question mock test "
                    f"for {exam.name}."
                ),
            }
        )

    # ---------------------------------------------------------
    # RANDOMIZE QUESTIONS
    # ---------------------------------------------------------
    questions = list(questions)

    # ---------------------------------------------------------
    # QUESTION IDS
    # ---------------------------------------------------------
    question_ids = ",".join(
        str(question.id)
        for question in questions
    )

    # ---------------------------------------------------------
    # POST - SUBMIT TEST
    # ---------------------------------------------------------
    if request.method == "POST":

        score = 0
        attempted = 0

        for question in questions:

            selected_answer = request.POST.get(
                f"question_{question.id}"
            )

            if selected_answer:
                attempted += 1

                if selected_answer.strip().lower() == question.answer.strip().lower():
                    score += 1

        percentage = round(
            (score / len(questions)) * 100,
            2
        )

        # Save attempt if model exists
        MockTestAttempt.objects.create(
            user=request.user,
            daily_test=daily_test,
            score=score,
            total_questions=len(questions),
            percentage=percentage,
            question_ids=[
                question.id
                for question in questions
            ]
        )

        return render(
            request,
            "jobportal/mock_test_result.html",
            {
                "exam": exam,
                "daily_test": daily_test,
                "score": score,
                "attempted": attempted,
                "total_questions": len(questions),
                "percentage": percentage,
            }
        )

    # ---------------------------------------------------------
    # DISPLAY MOCK TEST
    # ---------------------------------------------------------
    return render(
        request,
        "jobportal/mock_test.html",
        {
            "exam": exam,
            "daily_test": daily_test,
            "questions": questions,
            "question_ids": question_ids,
            "no_questions": False,
        }
    )


def view_pdf(request, folder, filename):
    pdf_path = (
        settings.BASE_DIR
        / "jobportal"
        / "static"
        / "pdfs"
        / folder
        / filename
    )

    if not pdf_path.exists():
        raise Http404(f"PDF not found: {pdf_path}")

    if not pdf_path.is_file():
        raise Http404("Requested PDF is not a file.")

    return FileResponse(
        open(pdf_path, "rb"),
        content_type="application/pdf"
    )


def download_pdf(request, folder, filename):
    pdf_path = (
        settings.BASE_DIR
        / "jobportal"
        / "static"
        / "pdfs"
        / folder
        / filename
    )

    if not pdf_path.exists():
        raise Http404(f"PDF not found: {pdf_path}")

    if not pdf_path.is_file():
        raise Http404("Requested PDF is not a file.")

    response = FileResponse(
        open(pdf_path, "rb"),
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        f'attachment; filename="{filename}"'
    )

    return response

EXAM_PAPERS = {
    "ssc-cgl": {
        "name": "SSC CGL",
        "category": "SSC",
        "description": "Staff Selection Commission Combined Graduate Level previous year papers.",
        "papers": [
            {
                "year": "2025",
                "title": "SSC CGL 2025 Previous Year Paper",
                "file": "pdfs/previous_papers/ssc_cgl/ssc_cgl_2025.pdf",
            },
            {
                "year": "2024",
                "title": "SSC CGL 2024 Previous Year Paper",
                "file": "pdfs/previous_papers/ssc_cgl/ssc_cgl_2024.pdf",
            },
        ],
    },

    "ssc-chsl": {
        "name": "SSC CHSL",
        "category": "SSC",
        "description": "Staff Selection Commission CHSL previous year papers.",
        "papers": [
            {
                "year": "2025",
                "title": "SSC CHSL 2025 Previous Year Paper",
                "file": "pdfs/previous_papers/ssc_chsl/ssc_chsl_2025.pdf",
            },
            {
                "year": "2024",
                "title": "SSC CHSL 2024 Previous Year Paper",
                "file": "pdfs/previous_papers/ssc_chsl/ssc_chsl_2024.pdf",
            },
        ],
    },

    "banking": {
        "name": "Banking Exams",
        "category": "Banking",
        "description": "Previous year papers for major banking examinations.",
        "papers": [
            {
                "year": "2025",
                "title": "SBI Clerk 2025 Previous Year Paper",
                "file": "pdfs/previous_papers/banking/sbi_clerk_2025.pdf",
            },
            {
                "year": "2025",
                "title": "IBPS PO 2025 Previous Year Paper",
                "file": "pdfs/previous_papers/banking/ibps_po_2025.pdf",
            },
        ],
    },

    "upsc": {
        "name": "UPSC",
        "category": "UPSC",
        "description": "Union Public Service Commission previous year papers.",
        "papers": [
            {
                "year": "2025",
                "title": "UPSC 2025 Previous Year Paper",
                "file": "pdfs/previous_papers/upsc/upsc_2025.pdf",
            },
            {
                "year": "2024",
                "title": "UPSC 2024 Previous Year Paper",
                "file": "pdfs/previous_papers/upsc/upsc_2024.pdf",
            },
        ],
    },

    "telangana": {
        "name": "Telangana Government Exams",
        "category": "Telangana",
        "description": "Previous year papers for Telangana government examinations.",
        "papers": [
            {
                "year": "2025",
                "title": "TSPSC Group 1 2025 Previous Year Paper",
                "file": "pdfs/previous_papers/telangana/tspsc_group1_2025.pdf",
            },
            {
                "year": "2025",
                "title": "Telangana Police Constable 2025 Previous Year Paper",
                "file": "pdfs/previous_papers/telangana/police_constable_2025.pdf",
            },
        ],
    },
}


def exam_papers(request, exam_slug):
    exam = EXAM_PAPERS.get(exam_slug)

    if not exam:
        from django.http import Http404
        raise Http404("Exam not found")

    return render(
        request,
        "jobportal/exam_papers.html",
        {
            "exam": exam,
            "exam_slug": exam_slug,
        }
    )

# =========================================================
# MOCK TEST DASHBOARD
# =========================================================

login_required(login_url="login")
def mock_tests(request):

    exams = Exam.objects.all().order_by("name")

    return render(
        request,
        "jobportal/mock_tests.html",
        {
            "exams": exams,
        }
    )


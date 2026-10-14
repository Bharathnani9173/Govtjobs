from ast import pattern

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count, Sum, Max
from datetime import date
from .models import ContactMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Job
import os
import json
from django.conf import settings
from django.templatetags.static import static
from django.http import FileResponse, Http404
from django.urls import reverse
from pathlib import Path
from django.db.models import Sum, Max
from django.contrib.admin.views.decorators import staff_member_required
from django.core.management import call_command


from .models import (
    Job,
    Subscriber,
    QuizQuestion,
    QuizQuestionHistory,
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
    AdmitCard,
    Result,
    ExamPattern,
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


from datetime import timedelta

def latest_jobs(request):
    today = timezone.now().date()
    new_job_date = today - timedelta(days=7)

    jobs = (
        Job.objects
        .filter(
            is_latest=True,
            official_link__isnull=False,
            official_link__gt="",
        )
        .order_by("-notification_date", "-created_at")
    )

    return render(
        request,
        "jobportal/latest_jobs.html",
        {
            "jobs": jobs,
            "new_job_date": new_job_date,
        },
    )


def results(request):
    return render(
        request,
        "jobportal/results.html"
    )



def admit_cards(request):
    admit_cards = AdmitCard.objects.all()

    search = request.GET.get("search", "").strip()
    category = request.GET.get("category", "").strip()
    status = request.GET.get("status", "").strip()
    year = request.GET.get("year", "").strip()

    if search:
        admit_cards = admit_cards.filter(
            Q(exam_name__icontains=search) |
            Q(organization__icontains=search) |
            Q(title__icontains=search)
        )

    if category:
        admit_cards = admit_cards.filter(category=category)

    if status:
        admit_cards = admit_cards.filter(status=status)

    if year:
        admit_cards = admit_cards.filter(year=year)

    years = (
        AdmitCard.objects
        .exclude(year__isnull=True)
        .values_list("year", flat=True)
        .distinct()
        .order_by("-year")
    )

    context = {
        "admit_cards": admit_cards,
        "years": years,
        "search": search,
        "selected_category": category,
        "selected_status": status,
        "selected_year": year,
    }

    return render(
        request,
        "jobportal/admit_cards.html",
        context
    )

def results(request):

    results = Result.objects.all()

    search = request.GET.get("search", "").strip()
    category = request.GET.get("category", "").strip()
    status = request.GET.get("status", "").strip()
    year = request.GET.get("year", "").strip()

    if search:
        results = results.filter(
            Q(exam_name__icontains=search) |
            Q(organization__icontains=search) |
            Q(title__icontains=search)
        )

    if category:
        results = results.filter(category=category)

    if status:
        results = results.filter(status=status)

    if year:
        results = results.filter(year=year)

    years = (
        Result.objects
        .exclude(year__isnull=True)
        .values_list("year", flat=True)
        .distinct()
        .order_by("-year")
    )

    context = {
        "results": results,
        "years": years,
        "search": search,
        "selected_category": category,
        "selected_status": status,
        "selected_year": year,
    }

    return render(
        request,
        "jobportal/results.html",
        context
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

    # Random 40 questions
    questions = list(
        available_questions.order_by("?")[:40]
    )

    # ==========================================
    # IF LESS THAN 40 UNUSED QUESTIONS
    # ==========================================

    if len(questions) < 40:

        # Start using the full question bank again
        questions = list(
            QuizQuestion.objects.order_by("?")[:40]
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

@login_required
def score_history(request):
    attempts = MockTestAttempt.objects.filter(
        user=request.user
    ).select_related("daily_test")

    return render(
        request,
        "jobportal/score_history.html",
        {
            "attempts": attempts
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

@login_required(login_url="login")
def previous_papers(request):
    exams = Exam.objects.prefetch_related(
        "previous_papers"
    ).order_by("name")

    return render(
        request,
        "jobportal/previous_papers.html",
        {
            "exams": exams,
        }
    )

@login_required(login_url="login")
def exam_previous_papers(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    papers = PreviousPaper.objects.filter(
        exam=exam
    ).order_by("-year", "paper_name")

    return render(
        request,
        "jobportal/exam_previous_papers.html",
        {
            "exam": exam,
            "papers": papers,
        }
    )
# =========================
# ANSWER KEYS
# =========================
def answer_keys(request):

    # =========================================================
    # ANSWER KEY YEAR RULE
    # Only historical years up to 2022
    # 2023, 2024, 2025 and 2026 will NOT be displayed
    # =========================================================

    MAX_ANSWER_KEY_YEAR = 2022

    # =========================================================
    # ALL 34 EXAMS
    # =========================================================

    exam_catalog = [
        "Air Force",
        "Banking",
        "DSC",
        "District Court",
        "Forest Range Officer",
        "Health Department",
        "High Court",
        "IBPS Clerk",
        "IBPS PO",
        "Indian Army",
        "RRB ALP",
        "RRB Group D",
        "RRB JE",
        "RRB NTPC",
        "RRB Technician",
        "Railway Constable",
        "Railway SI",
        "Revenue Department",
        "SBI Clerk",
        "SBI PO",
        "SSC CGL",
        "SSC CHSL",
        "SSC GD",
        "TET",
        "TGPSC Group 1",
        "TGPSC Group 2",
        "TGPSC Group 3",
        "TGPSC Group 4",
        "Telangana AE",
        "Telangana AEE",
        "Telangana Police Constable",
        "Telangana Police SI",
        "UPSC",
        "UPSC CSE",
    ]

    # =========================================================
    # GET FILTER VALUES
    # =========================================================

    selected_exam = request.GET.get("exam", "").strip()
    selected_year = request.GET.get("year", "").strip()
    selected_shift = request.GET.get("shift", "").strip()
    selected_set = request.GET.get("set", "").strip()

    # =========================================================
    # IMPORTANT:
    # NEVER SHOW 2023, 2024, 2025, 2026
    # =========================================================

    answer_keys = AnswerKey.objects.filter(
        year__lte=MAX_ANSWER_KEY_YEAR
    )

    # =========================================================
    # EXAM FILTER
    # =========================================================

    if selected_exam:
        answer_keys = answer_keys.filter(
            exam_name=selected_exam
        )

    # =========================================================
    # YEAR FILTER
    # =========================================================

    if selected_year:

        try:
            selected_year_int = int(selected_year)

            # Do not allow 2023+
            if selected_year_int <= MAX_ANSWER_KEY_YEAR:
                answer_keys = answer_keys.filter(
                    year=selected_year_int
                )
            else:
                answer_keys = AnswerKey.objects.none()

        except ValueError:
            answer_keys = AnswerKey.objects.none()

    # =========================================================
    # SHIFT FILTER
    # =========================================================

    if selected_shift:
        answer_keys = answer_keys.filter(
            shift=selected_shift
        )

    # =========================================================
    # SET / BOOKLET FILTER
    # =========================================================

    if selected_set:
        answer_keys = answer_keys.filter(
            set_name=selected_set
        )

    # =========================================================
    # ORDER
    # =========================================================

    answer_keys = answer_keys.order_by(
        "exam_name",
        "-year",
        "shift",
        "set_name",
        "paper_code"
    )

    # =========================================================
    # AVAILABLE YEARS
    # ONLY <= 2022
    # =========================================================

    year_queryset = AnswerKey.objects.filter(
        year__lte=MAX_ANSWER_KEY_YEAR
    )

    if selected_exam:
        year_queryset = year_queryset.filter(
            exam_name=selected_exam
        )

    years = (
        year_queryset
        .exclude(year__isnull=True)
        .values_list("year", flat=True)
        .distinct()
        .order_by("-year")
    )

    # =========================================================
    # AVAILABLE SHIFTS
    # =========================================================

    shift_queryset = AnswerKey.objects.filter(
        year__lte=MAX_ANSWER_KEY_YEAR
    )

    if selected_exam:
        shift_queryset = shift_queryset.filter(
            exam_name=selected_exam
        )

    if selected_year:
        try:
            selected_year_int = int(selected_year)

            if selected_year_int <= MAX_ANSWER_KEY_YEAR:
                shift_queryset = shift_queryset.filter(
                    year=selected_year_int
                )

        except ValueError:
            pass

    shifts = (
        shift_queryset
        .exclude(shift="")
        .values_list("shift", flat=True)
        .distinct()
        .order_by("shift")
    )

    # =========================================================
    # AVAILABLE SETS / BOOKLETS
    # =========================================================

    set_queryset = AnswerKey.objects.filter(
        year__lte=MAX_ANSWER_KEY_YEAR
    )

    if selected_exam:
        set_queryset = set_queryset.filter(
            exam_name=selected_exam
        )

    if selected_year:
        try:
            selected_year_int = int(selected_year)

            if selected_year_int <= MAX_ANSWER_KEY_YEAR:
                set_queryset = set_queryset.filter(
                    year=selected_year_int
                )

        except ValueError:
            pass

    if selected_shift:
        set_queryset = set_queryset.filter(
            shift=selected_shift
        )

    sets = (
        set_queryset
        .exclude(set_name="")
        .values_list("set_name", flat=True)
        .distinct()
        .order_by("set_name")
    )

    # =========================================================
    # COUNT
    # =========================================================

    total_keys = answer_keys.count()

    # =========================================================
    # RENDER
    # =========================================================

    return render(
        request,
        "jobportal/answer_keys.html",
        {
            "exam_catalog": exam_catalog,
            "answer_keys": answer_keys,
            "years": years,
            "shifts": shifts,
            "sets": sets,

            "selected_exam": selected_exam,
            "selected_year": selected_year,
            "selected_shift": selected_shift,
            "selected_set": selected_set,

            "total_keys": total_keys,

            # Send this to template
            "max_answer_key_year": MAX_ANSWER_KEY_YEAR,
        }
    )
# =========================
# CURRENT AFFAIRS
# =========================

from .models import Job, CurrentAffair
def current_affairs(request):
    period = request.GET.get("period")
    job_id = request.GET.get("job")

    if period:
        affairs = CurrentAffair.objects.filter(
            period=period
        ).order_by("-date")

        selected_period = period
    else:
        affairs = CurrentAffair.objects.none()
        selected_period = None

    periods = CurrentAffair.PERIOD_CHOICES

    return render(
        request,
        "jobportal/current_affairs.html",
        {
            "affairs": affairs,
            "periods": periods,
            "selected_period": selected_period,
        }
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

    # ==========================================================
    # JUNIOR ASSISTANT
    # ==========================================================
    if exam.name == "Junior Assistant":

        subject = request.GET.get("subject")

        # ------------------------------------------------------
        # STEP 1: SHOW SUBJECTS
        # ------------------------------------------------------
    if not subject:
        patterns = ExamPattern.objects.filter(
        exam=exam
    ).order_by("id")

    return render(
        request,
        "jobportal/mock_test_subjects.html",
        {
            "exam": exam,
            "patterns": patterns,
        }
    )

def get_unused_questions_for_user(user, exam, subject, total_questions):
    """
    Return questions the user has NOT attempted before
    for this exam and subject.
    """

    # Get all previous attempts by this user
    previous_attempts = QuizAttempt.objects.filter(
        user=user
    )

    # Collect all previously attempted question IDs
    used_question_ids = set()

    for attempt in previous_attempts:
        if attempt.question_ids:
            used_question_ids.update(
                int(qid) for qid in attempt.question_ids
            )

    # Get available questions
    questions = QuizQuestion.objects.filter(
        exam=exam,
        subject=subject
    ).exclude(
        id__in=used_question_ids
    ).order_by("?")[:total_questions]

    return list(questions)

# =========================================================
# EXAM-WISE MOCK TEST
# =========================================================
@login_required(login_url="login")
def exam_mock_test(request, exam_name):

    exam = get_object_or_404(Exam, name=exam_name)

    # Get the selected subject
    subject = request.GET.get("subject") or request.POST.get("subject")

    # Get subject patterns for this exam
    patterns = ExamPattern.objects.filter(
        exam=exam
    ).order_by("id")

    # --------------------------------------------------
    # SELECT SUBJECT
    # --------------------------------------------------
    if not subject:
        return render(
            request,
            "jobportal/mock_test_subjects.html",
            {
                "exam": exam,
                "patterns": patterns,
            }
        )

    # Get the pattern for the selected subject
    pattern = get_object_or_404(
        ExamPattern,
        exam=exam,
        subject=subject
    )

    required_count = pattern.question_count
    duration_minutes = pattern.duration_minutes
    marks_per_question = pattern.marks_per_question
    negative_marking = pattern.negative_marking

    # --------------------------------------------------
    # SUBMIT TEST
    # --------------------------------------------------
    if request.method == "POST":

        question_ids = request.POST.get("question_ids", "")

        question_ids = [
            int(x)
            for x in question_ids.split(",")
            if x.strip().isdigit()
        ]

        # Only accept question IDs belonging to this exam
        # and the selected subject.
        questions = list(
            QuizQuestion.objects.filter(
                id__in=question_ids,
                exam=exam,
                subject=subject
            ).distinct()
        )

        # Avoid counting duplicated or invalid submitted IDs
        question_ids = [q.id for q in questions]

        score = 0
        correct = 0
        wrong = 0
        unanswered = 0
        answers = {}

        for question in questions:

            user_answer = request.POST.get(
                f"question_{question.id}"
            )

            answers[str(question.id)] = user_answer

            if not user_answer:
                unanswered += 1

            elif user_answer == question.answer:
                correct += 1
                score += marks_per_question

            else:
                wrong += 1
                score -= negative_marking

        # Save the attempt
        MockTestAttempt.objects.create(
            user=request.user,
            exam=exam,
            daily_test=None,
            score=score,
            total_questions=len(questions),
            correct_answers=correct,
            wrong_answers=wrong,
            unanswered=unanswered,
            answers=answers,
            question_ids=question_ids
        )

        # Record questions already attempted
        for question_id in question_ids:
            QuizQuestionHistory.objects.get_or_create(
                user=request.user,
                question_id=question_id,
                exam=exam
            )

        return redirect("score_history")

    # --------------------------------------------------
    # GET AVAILABLE QUESTIONS
    # --------------------------------------------------
    seen_ids = QuizQuestionHistory.objects.filter(
        user=request.user,
        exam=exam
    ).values_list(
        "question_id",
        flat=True
    )

    available_questions = QuizQuestion.objects.filter(
        exam=exam,
        subject=subject
    ).exclude(
        id__in=seen_ids
    )

    available_count = available_questions.count()

    total_subject_questions = QuizQuestion.objects.filter(
        exam=exam,
        subject=subject
    ).count()

    attempted_questions = QuizQuestionHistory.objects.filter(
        user=request.user,
        exam=exam,
        question_id__in=QuizQuestion.objects.filter(
            exam=exam,
            subject=subject
        ).values_list(
            "id",
            flat=True
        )
    ).values(
        "question_id"
    ).distinct().count()

    # --------------------------------------------------
    # NOT ENOUGH QUESTIONS
    # --------------------------------------------------
    if available_count < required_count:

        return render(
            request,
            "jobportal/exam_mock_test.html",
            {
                "exam": exam,
                "subject": subject,
                "pattern": pattern,
                "required_count": required_count,
                "question_count": total_subject_questions,
                "available_count": available_count,
                "attempted_questions": attempted_questions,
                "duration_minutes": duration_minutes,
                "marks_per_question": marks_per_question,
                "negative_marking": negative_marking,
                "questions": [],
                "question_ids": "",
                "not_enough_questions": True,
            }
        )

    # --------------------------------------------------
    # SELECT RANDOM QUESTIONS
    # --------------------------------------------------
    questions = list(
        available_questions.order_by("?")[:required_count]
    )

    question_ids = ",".join(
        str(question.id) for question in questions
    )

    # --------------------------------------------------
    # SHOW TEST
    # --------------------------------------------------
    return render(
        request,
        "jobportal/exam_mock_test.html",
        {
            "exam": exam,
            "subject": subject,
            "pattern": pattern,
            "questions": questions,
            "question_ids": question_ids,
            "required_count": required_count,
            "question_count": len(questions),
            "duration_minutes": duration_minutes,
            "marks_per_question": marks_per_question,
            "negative_marking": negative_marking,
            "not_enough_questions": False,
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
@login_required(login_url="login")
def mock_tests(request):

    excluded_exams = [
        "TSPSC Group 1",
        "TSPSC Group 2",
        "TSPSC Group 3",
        "TSPSC Group 4",
        "Air Force",
        "Army",
    ]

    exams = Exam.objects.exclude(
        name__in=excluded_exams
    ).order_by("name")

    mock_tests_list = []

    for exam in exams:

        patterns = ExamPattern.objects.filter(
            exam=exam
        ).order_by("id")

        if patterns.exists():

            subjects = []

            for pattern in patterns:
                actual_count = QuizQuestion.objects.filter(
                    exam=exam,
                    subject=pattern.subject
                ).count()

                subjects.append({
    "name": pattern.subject,
    "questions": pattern.question_count,
    "available_questions": actual_count,
    "duration_minutes": pattern.question_count,
    "marks_per_question": pattern.marks_per_question,
    "negative_marking": pattern.negative_marking,
})

            total_questions = sum(
                pattern.question_count for pattern in patterns
            )

            available = all(
                subject["available_questions"] >= subject["questions"]
                for subject in subjects
            )

            mock_tests_list.append({
                "exam": exam,
                "exam_name": exam.name,
                "question_count": total_questions,
                "subjects": subjects,
                "available": available,
                "is_configured": True,
            })

        else:
            question_count = QuizQuestion.objects.filter(
                exam=exam
            ).count()

            mock_tests_list.append({
                "exam": exam,
                "exam_name": exam.name,
                "question_count": question_count,
                "subjects": [],
                "available": question_count > 0,
                "is_configured": False,
            })

    return render(
        request,
        "jobportal/mock_tests.html",
        {
            "mock_tests": mock_tests_list,
            "exams": mock_tests_list,
        }
    )

@login_required
def leaderboard(request):
    leaderboard_data = (
        MockTestAttempt.objects
        .values(
            "user__username"
        )
        .annotate(
            total_score=Sum("score"),
            best_score=Max("score"),
            tests_taken=Count("id")
        )
        .order_by("-total_score")[:50]
    )

    return render(
        request,
        "jobportal/leaderboard.html",
        {
            "leaderboard": leaderboard_data
        }
    )



from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token


@staff_member_required
@require_http_methods(["GET", "POST"])
def import_exam_patterns_once(request):
    if not request.user.is_superuser:
        return HttpResponse("Superuser access required.", status=403)

    if request.method == "POST":
        call_command("import_exam_patterns")
        return HttpResponse(
            "Exam pattern import completed. "
            "Open Django Admin and verify the ExamPattern records."
        )

    csrf_token = get_token(request)
    return HttpResponse(
        f"""
        <h2>Import Exam Patterns</h2>
        <p>This will import the 79 exam patterns.</p>
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken"
                   value="{csrf_token}">
            <button type="submit">Import Exam Patterns</button>
        </form>
        """
    )


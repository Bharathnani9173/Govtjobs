from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (
    Job,
    Result,
    AdmitCard,
    AnswerKey,
    PreviousPaper,
    CurrentAffair,
    Notification,
    Feedback,
    ContactMessage,
    SavedJob,
    StudyMaterial,
    Subscriber,
    QuizQuestion,
    MockTestAttempt,
    DailyMockTest,
    DailyQuiz,
    Exam,
    MockTest,
    MockTestQuestion,
    QuizAttempt,
    Syllabus,
)


# =========================================================
# JOB
# =========================================================

@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):

    list_display = (
        "title",
        "organization",
        "job_type",
        "category",
        "state",
        "qualification",
        "vacancies",
        "last_date",
    )

    search_fields = (
        "title",
        "organization",
        "state",
        "qualification",
        "location",
    )

    list_filter = (
        "job_type",
        "category",
        "state",
        "application_mode",
    )

    ordering = (
        "-notification_date",
    )


# =========================================================
# PREVIOUS PAPERS
# =========================================================

@admin.register(PreviousPaper)
class PreviousPaperAdmin(admin.ModelAdmin):

    list_display = (
        "exam_name",
        "job",
        "category",
        "year",
    )

    search_fields = (
        "exam_name",
        "job__title",
        "job__organization",
    )

    list_filter = (
        "category",
        "year",
    )

    ordering = (
        "-year",
    )


# =========================================================
# ANSWER KEYS
# =========================================================

@admin.register(AnswerKey)
class AnswerKeyAdmin(admin.ModelAdmin):

    list_display = (
        "exam_name",
        "job",
        "category",
        "release_date",
    )

    search_fields = (
        "exam_name",
        "job__title",
        "job__organization",
    )

    list_filter = (
        "category",
        "release_date",
    )

    ordering = (
        "-release_date",
    )


# =========================================================
# CURRENT AFFAIRS
# =========================================================

@admin.register(CurrentAffair)
class CurrentAffairAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "job",
        "category",
        "date",
    )

    search_fields = (
        "title",
        "job__title",
        "job__organization",
        "description",
    )

    list_filter = (
        "category",
        "date",
    )

    ordering = (
        "-date",
    )


# =========================================================
# SYLLABUS
# =========================================================

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "job",
        "pdf_link",
    )

    search_fields = (
        "title",
        "job__title",
        "job__organization",
        "description",
    )

    list_filter = (
        "job__category",
    )


# =========================================================
# MOCK TEST
# =========================================================

@admin.register(MockTest)
class MockTestAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "duration",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "title",
    )

# =========================================================
# MOCK TEST QUESTIONS
# =========================================================

@admin.register(MockTestQuestion)
class MockTestQuestionAdmin(admin.ModelAdmin):

    list_display = (
        "question",
        "answer",
    )

    search_fields = (
        "question",
        "option1",
        "option2",
        "option3",
        "option4",
        "answer",
    )

    ordering = (
        "id",
    )


# =========================================================
# QUIZ QUESTIONS
# =========================================================

@admin.register(QuizQuestion)
class QuizQuestionAdmin(ImportExportModelAdmin):

    list_display = (
        "question",
        "subject",
        "answer",
    )

    search_fields = (
        "question",
        "subject",
    )

    list_filter = (
        "subject",
    )


@admin.register(MockTestAttempt)
class MockTestAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "daily_test",
        "score",
        "total_questions",
        "correct_answers",
        "wrong_answers",
        "unanswered",
        "time_taken",
        "attempted_at",
    )

    list_filter = (
        "daily_test__exam_name",
        "attempted_at",
    )

    search_fields = (
        "user__username",
        "daily_test__exam_name",
    )



@admin.register(DailyMockTest)
class DailyMockTestAdmin(admin.ModelAdmin):
    list_display = (
        "exam_name",
        "title",
        "test_date",
        "duration",
        "total_questions",
    )

    list_filter = (
        "exam_name",
        "test_date",
    )

    search_fields = (
        "exam_name",
        "title",
    )


# =========================================================
# DAILY QUIZ
# =========================================================

@admin.register(DailyQuiz)
class DailyQuizAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "quiz_date",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "-quiz_date",
    )


# =========================================================
# RESULTS
# =========================================================

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        "exam_name",
        "result_date",
        "official_link",
    )

    search_fields = (
        "exam_name",
    )

    ordering = (
        "-result_date",
    )


# =========================================================
# ADMIT CARDS
# =========================================================

@admin.register(AdmitCard)
class AdmitCardAdmin(admin.ModelAdmin):

    list_display = (
        "exam_name",
        "release_date",
        "official_link",
    )

    search_fields = (
        "exam_name",
    )

    ordering = (
        "-release_date",
    )


# =========================================================
# NOTIFICATIONS
# =========================================================

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "last_date",
        "official_link",
    )

    search_fields = (
        "title",
        "organization",
    )

    ordering = (
        "-last_date",
    )


# =========================================================
# FEEDBACK
# =========================================================

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "rating",
        "category",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "message",
        "category",
    )

    list_filter = (
        "rating",
        "category",
        "status",
    )

    ordering = (
        "-created_at",
    )


# =========================================================
# CONTACT MESSAGES
# =========================================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "mobile",
        "subject",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "mobile",
        "subject",
        "message",
    )

    list_filter = (
        "status",
    )

    ordering = (
        "-created_at",
    )


# =========================================================
# SAVED JOBS
# =========================================================

@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):

    list_display = (
        "job",
        "saved_on",
    )

    search_fields = (
        "job__title",
        "job__organization",
    )

    ordering = (
        "-saved_on",
    )


# =========================================================
# STUDY MATERIAL
# =========================================================

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "subject",
        "uploaded_on",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "subject",
    )

    ordering = (
        "-uploaded_on",
    )


# =========================================================
# SUBSCRIBERS
# =========================================================

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):

    list_display = (
        "email",
        "name",
        "subscribed_date",
    )

    search_fields = (
        "email",
        "name",
    )

    ordering = (
        "-subscribed_date",
    )


# =========================================================
# EXAMS
# =========================================================

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "organization",
        "state",
        "status",
        "vacancies",
        "application_start",
        "application_end",
        "exam_date",
    )

    search_fields = (
        "name",
        "organization",
        "state",
    )

    list_filter = (
        "state",
        "status",
    )

    ordering = (
        "-created_at",
    )


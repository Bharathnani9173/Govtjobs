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
    DailyQuiz,
)


# ==========================
# JOB ADMIN (IMPORT / EXPORT)
# ==========================
@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    list_display = (
        "title",
        "organization",
        "category",
        "state",
        "qualification",
        "last_date",
    )

    search_fields = (
        "title",
        "organization",
        "state",
        "qualification",
    )

    list_filter = (
        "category",
        "state",
    )


# ==========================
# QUIZ QUESTION ADMIN
# ==========================
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


# ==========================
# DAILY QUIZ ADMIN
# ==========================
@admin.register(DailyQuiz)
class DailyQuizAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "quiz_date",
    )


# ==========================
# CONTACT MESSAGE ADMIN
# ==========================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "subject",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    list_filter = (
        "status",
    )


# ==========================
# OTHER MODELS
# ==========================
admin.site.register(Result)
admin.site.register(AdmitCard)
admin.site.register(AnswerKey)
admin.site.register(PreviousPaper)
admin.site.register(CurrentAffair)
admin.site.register(Notification)
admin.site.register(Feedback)
admin.site.register(SavedJob)
admin.site.register(StudyMaterial)
admin.site.register(Subscriber)
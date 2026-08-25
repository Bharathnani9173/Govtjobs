from django.urls import path
from . import views


urlpatterns = [

    # =========================
    # HOME / AUTH
    # =========================

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


    # =========================
    # JOBS
    # =========================

    path(
        'latest-jobs/',
        views.latest_jobs,
        name='latest_jobs'
    ),

    path(
        'search/',
        views.search,
        name='search'
    ),

    path(
        'job/<int:job_id>/',
        views.job_detail,
        name='job_detail'
    ),


    # =========================
    # RESULTS / ADMIT CARDS
    # =========================

    path(
        'results/',
        views.results,
        name='results'
    ),

    path(
        'admit-cards/',
        views.admit_cards,
        name='admit_cards'
    ),

    path(
        'job/tgpsc-group-1/',
        views.tgpsc_group_1,
        name='tgpsc_group_1'
    ),

    path(
        'job/ssc-cgl/',
        views.ssc_cgl,
        name='ssc_cgl'
    ),

    path(
        'job/railway-group-d/',
        views.railway_group_d,
        name='railway_group_d'
    ),

    path(
        'results/ssc-cgl/',
        views.ssc_cgl_result,
        name='ssc_cgl_result'
    ),

    path(
        'results/tgpsc-group-1/',
        views.tgpsc_result,
        name='tgpsc_result'
    ),

    path(
        'results/railway-group-d/',
        views.railway_result,
        name='railway_result'
    ),


    # =========================
    # STUDY MATERIAL
    # =========================

    path(
        'previous-papers/',
        views.previous_papers,
        name='previous_papers'
    ),

    path(
        'answer-keys/',
        views.answer_keys,
        name='answer_keys'
    ),

    path(
        'current-affairs/',
        views.current_affairs,
        name='current_affairs'
    ),

    path(
        'syllabus/',
        views.syllabus,
        name='syllabus'
    ),


    # =========================
    # EXAM PAPERS
    # =========================
    # Dynamic exam pages:
    #
    # /job/upsc/
    # /job/ssc-chsl/
    # /job/banking/
    # /job/telangana/
    #
    # The specific URLs above (SSC CGL, Railway, TGPSC)
    # are matched first.

    path(
    "job/<slug:exam_slug>/",
    views.exam_papers,
    name="exam_papers"
    ),


    # =========================
    # MOCK TESTS / QUIZ
    # =========================

    path(
        'mock-test/',
        views.mock_test,
        name='mock_test'
    ),

    
    path(
      "mock-tests/",
       views.mock_tests,
       name="mock_tests"
    ),



    path(
        'daily-quiz/',
        views.daily_quiz,
        name='daily_quiz'
    ),

    path(
        'score-history/',
        views.score_history,
        name='score_history'
    ),


    # =========================
    # USER FEATURES
    # =========================

    path(
        'saved-jobs/',
        views.saved_jobs,
        name='saved_jobs'
    ),

    path(
        'my-queries/',
        views.my_queries,
        name='my_queries'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'faq/',
        views.faq,
        name='faq'
    ),

    path(
        'feedback/',
        views.feedback,
        name='feedback'
    ),

    path(
        'subscribe/',
        views.subscribe,
        name='subscribe'
    ),

    path(
        'notifications/',
        views.notifications,
        name='notifications'
    ),

    path(
    "job/<slug:exam_slug>/",
    views.exam_papers,
    name="exam_papers"
    ),

    path(
      "exam/<str:exam_name>/mock-test/",
       views.exam_mock_test,
       name="exam_mock_test"
    ),

    # =========================
    # PDF
    # =========================

    path(
    "view-pdf/<str:folder>/<str:filename>/",
    views.view_pdf,
    name="view_pdf",
    ),

    path(
    "download-pdf/<str:folder>/<str:filename>/",
    views.download_pdf,
    name="download_pdf",
    ),
]


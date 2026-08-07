from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),

    path('register/', views.register_view, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('latest-jobs/', views.latest_jobs, name='latest_jobs'),

    path('results/', views.results, name='results'),

    path('admit-cards/', views.admit_cards, name='admit_cards'),

    path('job/tgpsc-group-1/', views.tgpsc_group_1, name='tgpsc_group_1'),

    path('job/ssc-cgl/', views.ssc_cgl, name='ssc_cgl'),

    path('job/railway-group-d/', views.railway_group_d, name='railway_group_d'),

    path('results/ssc-cgl/', views.ssc_cgl_result, name='ssc_cgl_result'),

    path('results/tgpsc-group-1/', views.tgpsc_result, name='tgpsc_result'),

    path('results/railway-group-d/', views.railway_result, name='railway_result'),

    path('answer-keys/', views.answer_keys, name='answer_keys'),

    path('previous-papers/', views.previous_papers, name='previous_papers'),

    path('current-affairs/', views.current_affairs, name='current_affairs'),

    path('notifications/', views.notifications, name='notifications'),

    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),

    path('contact/', views.contact, name='contact'),

    path('about/', views.about, name='about'),

    path('faq/', views.faq, name='faq'),

    path('feedback/', views.feedback, name='feedback'),

    path('search/', views.search, name='search'),


     path(
        "subscribe/",
        views.subscribe,
        name="subscribe"
    ),


    path(
    "daily-quiz/",
    views.daily_quiz,
    name="daily_quiz"
    ),


    path(
    "score-history/",
    views.score_history,
    name="score_history"
    ),

    path(
    "my-queries/",
    views.my_queries,
    name="my_queries"
    ),
    
]
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from surveys import views

urlpatterns = [
    path('test/', views.TestListAdmin.as_view()),
    path('test/<int:pk>/', views.TestDetailAdmin.as_view()),

    path('answer/', views.AnsverList.as_view()),
    path('answer/<int:pk>/', views.AnsverDetail.as_view()),
    path('answer/view/<int:user_id>/', views.AnswerViewsId.as_view()),

    path('choice/', views.ChoiceListAdmin.as_view()),
    path('choice/<int:pk>/', views.ChoiceDetailAdmin.as_view()),

    path('question/', views.QuestionListAdmin.as_view()),
    path('question/<int:pk>/', views.QuestionDetailAdmin.as_view()),

    
    path('login/', views.User.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
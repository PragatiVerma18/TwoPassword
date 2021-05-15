from django.urls import path

from . import views

urlpatterns = [
    path('', views.PasswordList.as_view()),
    path('create/', views.PasswordCreate.as_view()),
    path('<int:pk>/', views.PasswordDetail.as_view()),
]

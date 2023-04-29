from django.urls import path
from love import views

urlpatterns = [
    path('love/', views.LoveList.as_view()),
    path('love/<int:pk>/', views.LoveDetail.as_view()),
]
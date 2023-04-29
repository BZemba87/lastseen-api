from django.urls import path
from fave import views


urlpatterns = [
    path('fave/', views.FaveList.as_view()),
    path('fave/<int:pk>/', views.FaveDetail.as_view())
]
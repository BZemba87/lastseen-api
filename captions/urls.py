from django.urls import path
from captions import views

urlpatterns = [
    path('captions/', views.CaptionList.as_view()),
    path('captions/<int:pk>/', views.CaptionDetail.as_view())
]
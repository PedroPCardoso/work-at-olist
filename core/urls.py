from django.urls import path
from core import views

urlpatterns = [
    path('calls/', views.list),
    #path('calls/<int:pk>/', views.PersonDetail.as_view()),
]
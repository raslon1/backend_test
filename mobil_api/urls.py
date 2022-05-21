from django.contrib import admin

from django.urls import path

from .views import POSView, VisitView

urlpatterns = [
    path('pos/', POSView.as_view()),
    path('visit/', VisitView.as_view()),
]
"""PubQuizMania URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from PubQuizMania.app.startup import start_script
from PubQuizMania.app.controller.controller import (
    get_categories,
    get_labeling_stats,
    get_random_quiz,
    get_unlabeled_question,
    label_question,
)
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Quiz API",
            description="A wonderful API for Quiz Questions",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path("admin/", admin.site.urls),
    path("random_quiz/", get_random_quiz, name="get_quiz"),
    path("unlabeled/", get_unlabeled_question, name="get_unlabeled_question"),
    path("categories/", get_categories, name="get_categories"),
    path("label/stats/", get_labeling_stats, name="get_labeling_stats"),
    path("label/", label_question, name="label_question")
]

start_script()

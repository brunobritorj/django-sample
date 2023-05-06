from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from . import views
from .views import protected_view

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^.*$', protected_view),
]

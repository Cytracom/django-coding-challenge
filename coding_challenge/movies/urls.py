from django.urls import path

from movies.views import MovieListView

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
]

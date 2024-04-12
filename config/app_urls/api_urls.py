from django.urls import include, path

# All URLS included in here will be prefixed with 'api/'
urlpatterns = [
    path("movies/", include("movies.urls")),
]


# Django Coding Challenge for Cytracom

This simple Django project uses Docker and can be built via `docker compose build` and run via `docker compose up`

To run initial migrations, run `docker compose run --rm django python manage.py migrate`

This project will serve an API on `localhost:8080`

The project includes a List API for Movies at `localhost:8080/api/movies`

## Your Task

Your task is to extend this project wth some new endpoints and features, as follows:

* Add a Detail View for Movies
* Modify the API to return `movie_name` instead of `title`
* Add a new field to the API: `runtime_formatted` that returns the runtime as a string in the format `H:MM`
* Add a second Model for Reviews that is many:one related to Movies
  * Include, at minimum, fields for the reviewer's name and rating out of 5 stars
* Add Reviews to both the List and Detail Movie Views
  * Include the whole model, not just an ID reference
* Add Query Parameters to the List View that allows filtering on the `runtime`
  * It should be possible to filter for either longer or shorter than the input

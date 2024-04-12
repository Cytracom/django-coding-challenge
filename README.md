# Django Coding Challenge for Cytracom

This simple Django project uses Docker and can be built via `docker compose build` and run via `docker compose up`

To run initial migrations, run `docker compose run --rm django python manage.py migrate`

This project will serve an API on `localhost:8080`

The project includes a List API for Movies at `localhost:8080/api/movies`


## Your Task

All of the relevant code for these tasks lives in `coding_challenge/movies/`

Your task is to extend this project wth some new endpoints and features, as follows:

* Add a Detail View for Movies
  * Querying GET `/api/movies/1` would return the Movie with `id: 1`
  * Allow PUT, PATCH, DELETE on `/api/movies/<id>` as well
* Add a new field to the API: `runtime_formatted` that returns the runtime as a string in the format `H:MM`
  * A `runtime` of 142 minutes should have a `runtime_formatted` of `2:22`
* Add a second Model for Reviews that is many:one related to Movies
  * Include, at minimum, fields for the reviewer's name and rating out of 5 stars
* Add Reviews to both the List and Detail Movie Views
  * Include the whole model, not just an ID reference
  * Example output:
    ```
    {
      "title": "Forrest Gump",
      "runtime": 142,
      "release_date": "1994-07-06",
      "reviewers": [{"name": "Roger Ebert", "rating": 4}, {"name": "Gene Siskel", "rating": 3}]
    }
    ```
* Add a new field to the API: `avg_rating` that returns the average rating of a movie by all the reviewers
  * A Movie with 4 reviewers, who each gave the Movie 2, 2, 3, and 4 stars would result in an `avg_rating` of `2.75`
* Add Query Parameters to the List View that allows filtering on the `runtime`
  * It should be possible to filter for either longer or shorter than the input

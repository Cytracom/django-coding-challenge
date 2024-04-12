FROM python:3.11-slim-bookworm as python

FROM python as python-build-stage

RUN apt-get update && apt-get install --no-install-recommends -y build-essential libpq-dev curl

RUN curl -sSL https://install.python-poetry.org | python - --version 1.7.1
ENV PATH="${PATH}:/root/.local/bin"

COPY ./pyproject.toml ./poetry.lock /
RUN poetry export --without-hashes --output requirements.txt --with dev
RUN pip install --upgrade pip
RUN pip wheel --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python as python-run-stage

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y libpq-dev postgresql-client gettext git

COPY --from=python-build-stage /usr/src/app/wheels /wheels/
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* && rm -rf /wheels/

COPY ./compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . /app

ENTRYPOINT ["/entrypoint"]

FROM python:3.10.5-bullseye

ARG GROUP_ID
ARG USER_ID
ARG USER_NAME
ARG WORK_DIR

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PATH=/home/$USER_NAME/.local/bin:$PATH

RUN groupadd --gid $GROUP_ID $USER_NAME \
    && useradd --uid $USER_ID --gid $GROUP_ID --create-home $USER_NAME \
    && runuser --user $USER_NAME -- mkdir $WORK_DIR
USER $USER_NAME

WORKDIR $WORK_DIR

COPY pyproject.toml poetry.lock ./
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python - \
    && poetry install

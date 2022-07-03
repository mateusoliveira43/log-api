FROM python:3.10.4-bullseye as setup

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
    && useradd --uid $USER_ID --gid $GROUP_ID --create-home $USER_NAME
USER $USER_NAME

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python \
    && mkdir $WORK_DIR
WORKDIR $WORK_DIR

FROM setup as install

COPY pyproject.toml poetry.lock ./
RUN poetry install

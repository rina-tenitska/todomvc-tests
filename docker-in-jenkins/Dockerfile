FROM python:3.8
# Switch to root user to install .NET SDK, pyenv and poetry
USER root
# Print kernel and distro info
RUN echo "Distro info:" && uname -a && cat /etc/*release
# Makes  the  default  answers  be used for all questions for apt
ARG DEBIAN_FRONTEND=noninteractive
# Set of all dependencies needed for pyenv to work on Ubuntu
RUN apt-get update \
&& apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8
ENV POETRY_HOME $HOME/.poetry
ENV PATH="$PATH:$POETRY_HOME/bin"
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

COPY . /workdir
WORKDIR /workdir
RUN poetry install
ENV context="remote"
ARG ALLUREDIR="/allure-results"
CMD poetry run pytest -n auto --alluredir=$ALLUREDIR


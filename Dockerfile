FROM python:3.10-slim

ENV PYTHONUNBUFFERED True
ENV PYTHONDONTWRITEBYTECODE True
# ENV PYTHONPATH="${PYTHONPATH}:/app"

# Add poetry config
ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_NO_INTERACTION=1W
ENV PATH="$POETRY_HOME/bin:$PATH"

## Add environment value for application
ENV PROJECT_ID="ksst-genai-app"
ENV LOCATION="asia-northeast1"

# Install poetry
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get purge -y --auto-remove curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . ./

# Install python library
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

CMD ["poetry", "run", "python", "src/main.py"]

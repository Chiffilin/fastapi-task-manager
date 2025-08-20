# [stage__base]-[BEGIN]================================================
FROM python:3.13.1-slim AS base

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd

# [update_and_pre_install]-[BEGIN]
RUN apt-get update && apt-get upgrade -y
# [update_and_pre_install]-[END]

ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} &&\
    chown --recursive ${USER} ${WORKDIR}
# [stage__base]-[END]================================================


# [stage__builder]-[BEGIN]===============================================
FROM base AS builder

COPY --from=ghcr.io/astral-sh/uv:0.6.13 /uv /usr/local/bin/

COPY uv.lock .
COPY pyproject.toml .

RUN uv sync --frozen && uv pip install uvicorn gunicorn
# [stage__builder]-[END]================================================


# [stage__final]-[BEGIN]================================================
FROM base AS final

ARG WORKDIR=/wd
ARG VENV_DIR=${WORKDIR}/.venv

COPY --from=builder /wd/.venv ${VENV_DIR}

COPY app/ ./app

# ---- ВИПРАВЛЕНО ----
# Додаємо права на виконання для віртуального середовища
RUN chmod -R +x ${VENV_DIR}/bin

ENV PATH="${VENV_DIR}/bin:$PATH"

# Використовуємо sh -c для більш надійного запуску
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000"]
# [stage__final]-[END]==================================================

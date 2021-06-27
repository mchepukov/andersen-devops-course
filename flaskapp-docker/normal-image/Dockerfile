FROM python:3.9-slim-buster AS build
WORKDIR /app

RUN apt-get update && apt-get -y install git --no-install-recommends
RUN git clone https://github.com/mchepukov/andersen-devops-course.git

WORKDIR /app/andersen-devops-course/python-flask-app

RUN python -m venv .venv && .venv/bin/pip3 install --no-cache-dir -U pip setuptools
RUN .venv/bin/pip3 install --no-cache-dir -r /app/andersen-devops-course/python-flask-app/requirements.txt
RUN find .venv \( -type d -a -name test -o -name tests \) -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' \+

FROM python:3.9-alpine
WORKDIR /app

COPY --from=build /app/andersen-devops-course/python-flask-app /app
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python3", "app.py"]
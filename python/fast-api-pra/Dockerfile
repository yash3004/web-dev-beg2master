FROM python:3.10-slim-buster

WORKDIR /fast-api-pra




COPY . .

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["uvicorn","app",".","main",":","app","--reload","--host", "0.0.0.0", "--port", "8000"]

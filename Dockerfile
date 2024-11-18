from python:3.9.20-slim-bookworm

WORKDIR /Users/yuvraj/flask-practice/docker

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]

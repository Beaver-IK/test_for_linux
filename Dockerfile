FROM python:3.9-slim

WORKDIR /tests

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["pytest"]
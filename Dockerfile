FROM python:3.7

WORKDIR /src
ENV PYTHONPATH /src

ADD requirements.txt /src/requirements.txt
ADD api /src/api

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "api.app:app"]

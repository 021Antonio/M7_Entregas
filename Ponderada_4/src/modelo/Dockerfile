FROM python:3.10

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "python_api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

EXPOSE 8000
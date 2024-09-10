FROM python:3.12.4-slim

WORKDIR /route

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 5000

CMD ["python", "route.py"]
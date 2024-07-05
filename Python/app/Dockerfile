FROM python:3

WORKDIR /myapp

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

COPY . /myapp

CMD ["python3", "run.py"]

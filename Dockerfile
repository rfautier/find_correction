FROM python:3-alpine

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY find_correction.py .

ENTRYPOINT ["python", "find_correction.py"]

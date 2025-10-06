FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000 

CMD ["python", "main.py", "--mode", "api", "--port", "3000"]

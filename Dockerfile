FROM python:3.10

WORKDIR /app

COPY app/ ./app/
COPY index.html .
COPY start.sh ./
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x start.sh

EXPOSE 8000

CMD ["./start.sh"]

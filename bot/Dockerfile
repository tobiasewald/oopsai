FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install requests
CMD ["python3", "send_to_discord.py", "ai_response.json"]
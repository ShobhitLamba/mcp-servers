FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install uv \
 && uv sync
CMD ["python", "test_run.py"]

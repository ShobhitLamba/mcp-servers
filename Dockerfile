FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install uv 
RUN pip install --no-cache-dir uv \
 && uv sync 
CMD ["uv", "run", "uvicorn", "test_run:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install uv && uv pip install -r <(uv pip compile pyproject.toml)
CMD ["python", "test_run.py"]

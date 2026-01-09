FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install uv \
 && uv pip compile pyproject.toml -o requirements.txt \
 && uv pip install -r requirements.txt
CMD ["python", "test_run.py"]

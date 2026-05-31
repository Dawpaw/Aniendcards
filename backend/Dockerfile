FROM python:3.13-slim

WORKDIR /app

RUN pip install uv

ENV UV_SYSTEM_PYTHON=1

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev

COPY . .

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
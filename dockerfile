FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies (no venv, system install)
RUN uv sync --frozen --no-dev --no-install-project

# Copy application code
COPY . .

EXPOSE 8501

ENV PORT=8080

CMD ["uv", "run", "streamlit", "run", "main.py", "--server.port", "8080", "--server.enableCORS", "false"]

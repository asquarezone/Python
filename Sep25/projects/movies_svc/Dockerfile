# Base image: Python + uv preinstalled
FROM ghcr.io/astral-sh/uv:python3.12-bookworm

# Workdir inside container
WORKDIR /app

# Avoid .pyc files and buffered stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy project metadata first (better caching)
COPY pyproject.toml README.md ./

# Install dependencies (without installing the project itself yet)
RUN uv sync --no-install-project

# Copy source code
COPY src ./src

# Install the project (so package fastapi_books_uv is importable)
RUN uv sync

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI via uv + uvicorn
CMD ["uv", "run", "uvicorn", "movies_svc.main:app", "--host", "0.0.0.0", "--port", "8000"]

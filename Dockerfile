# 1. Choose base image
FROM ubuntu:22.04

# 2. Set environment variables
ENV PATH=/root/.local/bin:$PATH
WORKDIR /usr/src/python_pkg

# 3. Install dependencies: curl, python3, pip, etc.
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 4. Install pipx using pip
RUN python3 -m pip install --user pipx \
    && python3 -m pipx ensurepath

# 5. Verify pipx installation
RUN pipx --version

RUN pipx install poetry

# 7. Create a volume for Poetry cache to persist between builds
VOLUME ["/root/.cache/pypoetry"]

# 8. Copy only the dependency files first for better layer caching
COPY pyproject.toml poetry.lock ./

# 9. Leverage the Poetry cache during dependency installation
RUN poetry config cache-dir /root/.cache/pypoetry \
    && poetry install --no-root

# It is important to have readme as well if we want to install the pacakge editable mode.
COPY ./src ./src
COPY ./tests ./tests
COPY ./README.md ./ 

RUN poetry install

EXPOSE 8888

CMD ["poetry", "run", "jupyter-lab", "--port=8888", "--no-browser", "--allow-root", "--ip=0.0.0.0"]

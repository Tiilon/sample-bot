# Stage 1: Build the application
FROM python:3.9-slim AS builder

WORKDIR /code

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the application code
COPY . .

# Stage 2: Create the final production image
FROM python:3.9-slim AS final

WORKDIR /code

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

RUN pip install --ignore-installed uvicorn==0.20.0

# Copy the application code from the builder stage
COPY --from=builder /code .

EXPOSE 80

# Set the entry point command
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

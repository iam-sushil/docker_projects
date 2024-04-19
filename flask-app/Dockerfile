# Get the base image with python 3.9
# ---------- STAGE 1 ---------
FROM python:3.9 AS backend-builder

# Create working directory in the container 
WORKDIR /app

# Copy the source code to the working directory of container
COPY . .

# Install the required dependencies with docker builder base
RUN pip install -r requirements.txt

# ---------- STAGE 2 ---------------
FROM python:3.9-slim

WORKDIR /app

COPY --from=backend-builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

COPY --from=backend-builder /app /app

# Run the python base Flask app
CMD ["python", "run.py"]

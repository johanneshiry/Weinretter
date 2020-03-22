# Set base image
FROM python:3-buster

# Set workdir
WORKDIR /backend

# Copy full directory to image storage
COPY . .

# Install all Python 3 requirements via pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Add user
RUN adduser --disabled-login --disabled-password --gecos "" backend

# Add owner
RUN chown -R backend:backend /backend

# Change user
USER backend

# Define entrypoint
ENTRYPOINT ["gunicorn", "-w", "5", "-b", "0.0.0.0:5000",  "app:app"]

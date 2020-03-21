FROM python:3-buster

WORKDIR /backend



COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt



RUN adduser --disabled-login --disabled-password --gecos "" backend
RUN chown -R backend:backend /backend
USER backend

ENTRYPOINT [ "gunicorn", "-w", "5", "-b", "0.0.0.0:5000",  "app:app" ]
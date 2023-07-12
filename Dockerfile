# Base image
FROM python:3.10-slim

RUN apt-get update
RUN apt-get install python3-dev build-essential -y

# Set working directory
WORKDIR /app

#set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV VIRTUAL_ENV=/opt/venv

RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv ${VIRTUAL_ENV}

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy project files to the working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the necessary port (e.g., 8000 for Django development server)
EXPOSE 8000

# Define the command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.development"]

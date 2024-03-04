# Use an official Python runtime as a parent image
FROM python:latest
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

EXPOSE 8000
# Run the application
CMD ["python", "manage.py", "runserver"]

# Use an official Python runtime as a parent image


FROM python:3.10
RUN python3 -m venv /venvm venv /venv
# Activate the virtual environment
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# Set the working directory in the container
WORKDIR /app

# Install system dependencies

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
RUN pip install virtualenv

# Dockerfile
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh
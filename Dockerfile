FROM python:3.8

# Create app directory
WORKDIR /usr/src/app

# Copy the Django app source to the working directory
COPY . .

# Install Django
RUN pip install -r requirements.txt

# Expose the required port
EXPOSE 8080

# Specify the command to run the Django app
CMD ["python", "manage.py", "runserver"]
FROM python:3.8

# Create app directory
# WORKDIR /usr/src/app
WORKDIR /usr/src/pokenea_project

# Copy the Django app source to the working directory
COPY . .

# Install Django
RUN pip install -r requirements.txt

# Expose the required port
EXPOSE 8000

# Specify the command to run the Flask app
CMD ["python", "manage.py"]
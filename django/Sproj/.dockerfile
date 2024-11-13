FROM python:latest
# Set the working directory
WORKDIR /
# Install the dependencies
# Copy the app files
COPY . .
# Expose the port
EXPOSE 50
# Run the app
CMD ["python", "manage.py","makemigrations"],["python","manage.py","migrate"],["python","manage.py","runserver","127.0.0.1:50"] 

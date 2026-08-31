# Base image
FROM python:3.14-slim

#Working directory
WORKDIR /"FLASK_APP_CICD_AUTOMATION"

#Copy everything
COPY . .

# Installing dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

#Expose the port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
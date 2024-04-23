# Use the Python base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy your Python code into the container
COPY  . .

# Install any necessary dependencies (if required)
RUN pip install nltk 
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt
# Specify the command to run when the container starts
CMD ["python", "app.py"]

# Use the official Python image as the base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY StopWordsRemoval.py .

# Install NLTK and download necessary resources
RUN pip install nltk
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

# Run the Python script when the container starts
CMD ["python", "StopWordsRemoval.py"]

FROM python:3.9

WORKDIR /app

COPY StopWordsRemoval.py .

RUN pip install nltk
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

CMD ["python", "StopWordsRemoval.py"]

# Stage 1: Build the application with dependencies
FROM python:3.10 AS build

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY ./questgen.py .

# Install any dependencies for your Python application
RUN pip install --no-cache-dir \
    git+https://github.com/ramsrigouthamg/Questgen.ai \
    git+https://github.com/boudinfl/pke.git@69337af9f9e72a25af6d7991eaa9869f1322dd72

# Download the NLTK universal tagset
RUN python -m nltk.downloader universal_tagset

# Download the spaCy English model
RUN python -m spacy download en

# Download and extract the sense2vec model
RUN wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz && \
    tar -xvf s2v_reddit_2015_md.tar.gz && \
    rm s2v_reddit_2015_md.tar.gz

# Stage 2: Create the final image with optimized size
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# Install cmake package
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    git \
    cmake

# Install SentencePiece library
RUN git clone https://github.com/google/sentencepiece.git && \
    cd sentencepiece && \
    git checkout tags/v0.1.90 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j $(nproc) && \
    make install && \
    cd / && \
    rm -rf sentencepiece && \
    ldconfig

# Copy the application code into the container
COPY . /app

# Set any environment variables, if needed
# ENV MY_ENV_VAR=my_value

# Expose any necessary ports
# EXPOSE 8000

# Run the Python application
CMD ["python", "questgen.py"]

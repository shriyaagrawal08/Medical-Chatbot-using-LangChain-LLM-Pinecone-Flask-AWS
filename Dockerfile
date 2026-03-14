# base python image
FROM python:3.9-slim

# set working directory
WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y build-essential \
    gcc \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# upgrade pip
RUN pip install --upgrade pip

# copy requirements file 
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy entire project
COPY . .

# expose flask app port
EXPOSE 8080

# run the application
CMD ["python", "app.py"]
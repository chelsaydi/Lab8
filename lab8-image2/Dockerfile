# Lab 8 - Image 2: Flask API on port 3000 exposing GET /get_users
# Build:  docker image build -t ces13/lab8-chelsey_saydi:0.0.2.RELEASE .
# Run:    docker run -p 3000:3000 -d --name lab8_api_v2 ces13/lab8-chelsey_saydi:0.0.2.RELEASE

# start by pulling the python image
# (flask==3.1.3 needs Python >= 3.9, so 3.11-alpine instead of 3.8-alpine)
FROM python:3.11-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local folder to the image
COPY . /app

# document the port the app listens on
EXPOSE 3000

CMD ["python3", "app.py"]

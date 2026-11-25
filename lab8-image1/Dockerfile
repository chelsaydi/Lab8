# Lab 8 - Image 1: Lab 5 "Postman and APIs" Flask app on port 5000
# Build:  docker image build -t ces13/lab8-chelsey_saydi:0.0.1.RELEASE .
# Run:    docker run -p 5000:5000 -d --name lab8_api_v1 ces13/lab8-chelsey_saydi:0.0.1.RELEASE

# start by pulling the python image
# (the lab uses python:3.8-alpine, but flask==3.1.3 in requirements.txt needs
#  Python >= 3.9, so 3.11-alpine is used instead)
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
EXPOSE 5000

CMD ["python3", "app.py"]

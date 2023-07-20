FROM python:latest

WORKDIR /chat-python-test
COPY . /chat-python-test
 
CMD ["python3" , "main.py"]

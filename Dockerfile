FROM python:latest

WORKDIR /chat-python-test
COPY . /chat-python-test

CMD ["ifconfig"]
 
CMD ["python3" , "main.py"]

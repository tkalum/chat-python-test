FROM python:latest

WORKDIR /chat-python-test
COPY . /chat-python-test

RUN pip install pyrogram tgcrypto

CMD ["ifconfig"]
 
CMD ["python3" , "main.py"]

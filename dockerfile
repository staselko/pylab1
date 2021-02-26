FROM python:3
WORKDIR /hello.py
COPY . .
CMD ["hello.py"]
ENTRYPOINT ["python3"]
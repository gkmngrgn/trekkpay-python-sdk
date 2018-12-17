FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["coverage", "run", "setup.py", "test"]

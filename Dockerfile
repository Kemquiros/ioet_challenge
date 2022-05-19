FROM python:3.11-rc-alpine

WORKDIR /app

COPY . .
RUN python setup.py install --user
CMD ["python", "ioet_challenge"]

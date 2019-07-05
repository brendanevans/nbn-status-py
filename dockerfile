FROM python:3.6-alpine3.7

RUN python3 -m pip install requests
RUN mkdir /nbn-checker
WORKDIR /nbn-checker

CMD ["python","nbnStatus.py"]
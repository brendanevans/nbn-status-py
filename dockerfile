FROM python:3.6-alpine3.7

RUN python3 -m pip install requests
RUN mkdir /nbn-status-py
WORKDIR /nbn-status-py

CMD ["python","nbn-status.py"]
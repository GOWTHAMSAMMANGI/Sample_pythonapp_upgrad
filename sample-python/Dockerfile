FROM python:alpine3.10
WORKDIR /opt 
COPY . /opt/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python ./app.py
#ENTRYPOINT ["python", "./app.py"]

FROM python:3
COPY rest_app.py /
EXPOSE 5000
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./rest_app.py" ]

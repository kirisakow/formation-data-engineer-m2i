FROM python:3.11-alpine
RUN mkdir /my_flask_app
COPY main.py /my_flask_app
COPY requirements.txt /my_flask_app
WORKDIR /my_flask_app
RUN python -m pip install --upgrade pip ; \
    pip install --no-cache-dir -r requirements.txt
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD [ "python", "main.py" ]

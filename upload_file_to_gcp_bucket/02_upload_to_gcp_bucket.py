import datetime
from flask import Flask, request, render_template
from google.oauth2 import service_account
import os
import requests
import google.cloud.storage as storage
from werkzeug.utils import secure_filename

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

EXPIRATION = datetime.timedelta(hours=1)
FILE_TYPE = 'text/csv'
BUCKET = 'data_m2i/input'

def upload_via_signed(bucket_name, blob_name, filename, expiration, file_type):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(blob_name)

    signed_url = blob.generate_signed_url(version="v4", method='PUT', expiration=expiration, content_type=file_type)
    print(signed_url)
    requests.put(signed_url, open(filename, 'rb'), headers={'Content-Type': file_type})

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':

        diag = request.files['file_to_upload']
        filename_1 = secure_filename(diag.filename)
        diag.save(filename_1)
        print(diag)

        upload_via_signed(BUCKET, diag.filename, diag.filename, EXPIRATION, FILE_TYPE)
        return "done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

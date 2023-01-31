from sort import sort_func
from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def upload_file():
    doc_type = request.form.get('type')
    file = request.files.get('file')
    filename = secure_filename(file.filename)
    file_path = f'tmp/{filename}'
    file.save(file_path)
    result = sort_func(doc_type, file_path)
    os.remove(file_path)
    return result


if __name__ == '__main__':
    app.run()

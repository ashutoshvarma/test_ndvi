#!flask/bin/python
from flask import Flask, jsonify, request, redirect, flash, send_from_directory
from werkzeug.utils import secure_filename
from ndvi import get_ndvi as ndvi
from pathlib import Path

upload_dir = Path('upload/')
if not upload_dir.exists():
    upload_dir.mkdir(exist_ok=True)

app = Flask(__name__)
app.secret_key = "DUMMY_SECRET"
app.config['UPLOAD_FOLDER'] = upload_dir
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['jp2', 'tif', 'tiff'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/get_ndvi', methods=['POST'])
def get_ndvi():
    if 'file4' not in request.files and 'file8' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file4 = request.files['file4']
    file8 = request.files['file8']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file4.filename == '' or file8.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file4 and file8 and allowed_file(file4.filename) and allowed_file(file8.filename):
        filename4 = secure_filename(file4.filename)
        filename8 = secure_filename(file8.filename)
        dest = Path('static/NDVI.tiff')
        if ndvi(filename4, filename8, str(dest)):
            return send_from_directory('static', 'NDVI.tiff', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
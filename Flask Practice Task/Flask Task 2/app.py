import hashlib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_md5_hash():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return jsonify({'error': 'No file part in the request.'}), 400
            
            file = request.files['file']
            
            if file.filename == '':
                return jsonify({'error': 'No selected file.'}), 400
            
            im_bytes = file.read()
            im_hash = hashlib.md5(im_bytes).hexdigest()
            
            return jsonify({'md5_hash': im_hash}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

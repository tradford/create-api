import json
import pandas as pd
from flask import Flask, request
app = Flask(__name__)
@app.route('/get_json', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        provided_data = request.files.get('file')
        if provided_data is None:
            return 'Please enter valid excel format ', 400
        data = provided_data
        df = pd.read_csv(data)
        transformed = df.to_json()
        result = {
            'result': transformed,
        }
        json.dumps(result)
        return result
if __name__ == '__main__':
    app.run()
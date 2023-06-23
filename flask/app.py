import json
from flask import Flask
app = Flask(__name__)

@app.route('/version', methods=['GET'])
def version():
    return json.dumps({"version":"1.0.0"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

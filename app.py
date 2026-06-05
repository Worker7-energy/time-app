from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/time')
def get_time():
    current_time = int(time.time())
    return jsonify({"time": current_time})

if __name__ == '__main__':
    app.run(port=3000)

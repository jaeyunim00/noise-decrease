from flask import Flask, render_template, jsonify

# import
from ai_model import generate_array

app = Flask(__name__)
array_generator = generate_array();

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_array')
def get_array():
    return jsonify(next(array_generator));

if __name__ == '__main__':
    app.run(debug=True)
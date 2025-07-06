from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.files['image_data'].read()  # updated for file input
    result = util.classify_image(image_data)

    return jsonify(result)

if __name__ == "__main__":
    print("Starting Flask Server...")
    util.load_saved_artifacts()
    app.run(port=5000)

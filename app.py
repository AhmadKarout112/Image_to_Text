from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return "OCR API is running!"

@app.route('/ocr', methods=['POST'])
def ocr_image():
    data = request.get_json()
    image_data = base64.b64decode(data['image_base64'])
    image = Image.open(BytesIO(image_data))
    text = pytesseract.image_to_string(image)
    return jsonify({"text": text})

from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    # Get the text from the form
    text = request.form['text']
    
    # Create a QR code with the provided text
    features = qrcode.QRCode(version=1, box_size=40, border=8)
    features.add_data(text)
    features.make(fit=True)
    generate_image = features.make_image(fill_color="Purple", back_color="White")
    
    # Save the QR code image temporarily
    file_path = "static/qr_code.png"
    generate_image.save(file_path)
    
    return render_template('index.html', qr_code_path=file_path)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from ex01.cipher.caesar import CaesarCipher  # Sửa lại đường dẫn import

app = Flask(__name__)

# Router route for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router route for Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(debug=True)

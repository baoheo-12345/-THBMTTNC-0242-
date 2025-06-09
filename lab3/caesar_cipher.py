import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# 1. Cấu hình đường dẫn cho các plugin Qt
# Dựa trên cấu trúc thư mục của bạn, nếu main.py ở thư mục gốc
# thì 'platforms' là thư mục con trực tiếp.
current_dir = os.path.dirname(os.path.abspath(__file__))
platforms_path = os.path.join(current_dir, "platforms")
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = platforms_path
print(f"QT_QPA_PLATFORM_PLUGIN_PATH được thiết lập thành: {platforms_path}")

# 2. Import lớp giao diện người dùng từ tệp ui/caesar.py
# Đảm bảo bạn đã chạy lệnh này trước đó:
# pyuic5 -x ./ui/caesar.ui -o ./ui/caesar.py
from ui.caesar import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối các nút với các hàm tương ứng
        # Giả định có btn_encrypt và btn_decrypt trên UI của bạn
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plaintext.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Giả định API trả về "encrypted_message"
                self.ui.txt_ciphertext.setText(data.get("encrypted_message", "Error: No encrypted message"))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                QMessageBox.critical(self, "API Error", f"Error while calling API: Status Code {response.status_code}\n{response.text}")
                print(f"Error while calling API: Status Code {response.status_code}\nResponse: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Error connecting to API: {e}")
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_ciphertext.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Giả định API trả về "decrypted_message"
                self.ui.txt_plaintext.setText(data.get("decrypted_message", "Error: No decrypted message"))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                QMessageBox.critical(self, "API Error", f"Error while calling API: Status Code {response.status_code}\n{response.text}")
                print(f"Error while calling API: Status Code {response.status_code}\nResponse: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Error connecting to API: {e}")
            print(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):  # RGB có 3 kênh màu
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\xFE':  # Ký tự đánh dấu kết thúc (11111110)git checkout main
            break
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Cách sử dụng: python decrypt.py <encoded_image_path>")
        return
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Thông điệp được giải mã:", decoded_message)

if __name__ == "__main__":
    main()

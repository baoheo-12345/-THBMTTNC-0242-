def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các biến ban đầu
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Bước chuẩn bị dữ liệu (padding)
    original_length = len(message)
    message += b'\x80'  # thêm bit 1
    while (len(message) % 64) != 56:
        message += b'\x00'  # thêm các bit 0

    # Thêm độ dài message (bit) ở cuối (64-bit, little endian)
    message += (original_length * 8).to_bytes(8, byteorder='little')

    # Các hằng số dùng trong thuật toán
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
    K = [int(abs(__import__('math').sin(i + 1)) * (2**32)) & 0xFFFFFFFF for i in range(64)]

    # Xử lý từng block 512-bit
    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset:chunk_offset + 64]
        M = [int.from_bytes(chunk[i:i+4], byteorder='little') for i in range(0, 64, 4)]

        A, B, C, D = a0, b0, c0, d0

        for i in range(64):
            if 0 <= i <= 15:
                F = (B & C) | (~B & D)
                g = i
            elif 16 <= i <= 31:
                F = (D & B) | (~D & C)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                F = C ^ (B | ~D)
                g = (7 * i) % 16

            F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + left_rotate(F, s[i])) & 0xFFFFFFFF

        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    # Trả về kết quả dạng chuỗi hex
    return '{:08x}{:08x}{:08x}{:08x}'.format(a0, b0, c0, d0)

input_string = input("Nhập chuỗi căn bản: ")
md5_hash = md5(input_string.encode('utf-8'))
print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")

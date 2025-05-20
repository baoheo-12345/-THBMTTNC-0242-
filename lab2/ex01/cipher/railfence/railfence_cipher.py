class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Tạo danh sách các "thanh ray"
        rails = ['' for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: xuống, -1: lên

        for char in plain_text:
            rails[rail_index] += char
            # Đổi hướng nếu cần
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return ''.join(rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Xác định chiều dài của từng ray
        pattern = self._get_pattern(len(cipher_text), num_rails)
        rail_lengths = [pattern.count(i) for i in range(num_rails)]

        # Tách văn bản mã hóa thành các phần tương ứng với các ray
        rails = []
        index = 0
        for length in rail_lengths:
            rails.append(cipher_text[index:index + length])
            index += length

        # Ghép lại theo thứ tự pattern
        plain_text = ''
        rail_pointers = [0] * num_rails
        for i in pattern:
            plain_text += rails[i][rail_pointers[i]]
            rail_pointers[i] += 1

        return plain_text

    def _get_pattern(self, length, num_rails):
        """Tạo mẫu chỉ số ray theo thứ tự zigzag"""
        pattern = []
        rail_index = 0
        direction = 1

        for _ in range(length):
            pattern.append(rail_index)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return pattern

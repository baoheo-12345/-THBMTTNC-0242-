class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        seen = set()
        matrix = []

        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                matrix.append(char)

        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def prepare_text(self, text):
        text = text.replace("J", "I").upper()
        prepared = ""
        i = 0
        while i < len(text):
            char1 = text[i]
            char2 = text[i+1] if i + 1 < len(text) else 'X'
            if char1 == char2:
                prepared += char1 + 'X'
                i += 1
            else:
                prepared += char1 + char2
                i += 2
        if len(prepared) % 2 != 0:
            prepared += 'X'
        return prepared

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = self.prepare_text(plain_text)
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            a, b = plain_text[i], plain_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # Optionally remove 'X' padding here if needed.
        return decrypted_text

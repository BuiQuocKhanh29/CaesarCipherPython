def caesar_encrypt(plaintext, k):
    ciphertext = ""
    k = k % 26  # lấy k mod 26

    for ch in plaintext:
        if ch.isalpha():  # nếu là chữ cái
            # Xử lý chữ hoa
            if ch.isupper():
                ciphertext += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            # Xử lý chữ thường
            else:
                ciphertext += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        else:
            ciphertext += ch  # ký tự khác giữ nguyên
    return ciphertext

# Test
P = "BuiQuocKhanh"
k = 28
C = caesar_encrypt(P, k)
print("Ten :", P)
print("MaHoa:", C)

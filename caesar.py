def caesar_encrypt(plaintext: str, k: int) -> str:
    result = ""
    k = k % 26  # lấy dư để gói trong bảng chữ cái
    
    for char in plaintext:
        if char.isupper():  # chữ hoa
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        elif char.islower():  # chữ thường
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            result += char  # giữ nguyên ký tự không phải chữ
    return result

if __name__ == "__main__":
    k = 28
    plaintext = "BuiQuocKhanh"
    ciphertext = caesar_encrypt(plaintext, k)
    print("Plaintext :", plaintext)
    print("Key (k)   :", k)
    print("Ciphertext:", ciphertext)

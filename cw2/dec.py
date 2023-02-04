import datetime
import base64

def ceaser_cipher(ciphertext, term, total_chars):
    print("Total characters in the file:", total_chars)
    plaintext = ""
    for i, char in enumerate(ciphertext):
        shift = term[i % len(term)]
        if char.isalpha():
            if char.isupper():
                shift_char = chr((ord(char) - shift - 65 + 26) % 26 + 65)
                plaintext += shift_char
            else:
                shift_char = chr((ord(char) - shift - 97 + 26) % 26 + 97)
                plaintext += shift_char
        elif char.isdigit():
            shift_char = chr((ord(char) - shift - 48 + 10) % 10 + 48)
            plaintext += shift_char
        else:
            plaintext += char
    return plaintext

def read_file(filename):
    try:
        with open(filename, "r") as f:
            ciphertext = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        log_event(f"File {filename} was not found .")
        return None
    return ciphertext

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def log_event(event):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {event}\n")

def decrypt_file():
    filename = input("Enter the file name: ")
    ciphertext = read_file(filename)
    if ciphertext is None:
        return
    ciphertext = base64.b64decode(ciphertext.encode()).decode()
    total_chars = len(ciphertext)
    

    a = int(input("Enter the pin number: "))
    term = []
    for n in range(1, total_chars):
        if (ord(ciphertext[n]) >= 65 and ord(ciphertext[n]) <= 90) or (ord(ciphertext[n]) >= 97 and ord(ciphertext[n]) <= 122):
            t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + a*n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 25) % 50 - 25
        else:
            t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 10) % 18 - 9
        term.append(t)
    print("Term:", term)

    plaintext = ceaser_cipher(ciphertext, term, total_chars)
    write_file(filename, plaintext)
    log_event(f"Decrypted file {filename}")
    print("File decrypted successfully.")

decrypt_file()

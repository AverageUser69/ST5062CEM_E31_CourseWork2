import datetime
import base64

def ceaser_cipher(plaintext, term, total_chars):
    print("Total characters in the file:", total_chars)
    ciphertext = ""
    for i, char in enumerate(plaintext):
        shift = term[i % len(term)] # use the i-th term to shift the i-th character
        if char.isalpha():
            if char.isupper():
                shift_char = chr((ord(char) + shift - 65) % 26 + 65)
                ciphertext += shift_char
            else:
                shift_char = chr((ord(char) + shift - 97) % 26 + 97)
                ciphertext += shift_char
        elif char.isdigit():
            shift_char = chr((ord(char) + shift - 48) % 10 + 48)
            ciphertext += shift_char
        else:
            ciphertext += char
    b64_ciphertext = base64.b64encode(ciphertext.encode()).decode()
    return b64_ciphertext


def get_pin():
    pin = input("Enter the pin number (at least 4 digits, not more than 8 digits): ")
    while len(pin) < 4 or len(pin) > 8:
        if len(pin) < 4:
            print("Pin number should be at least 4 digits.")
        else:
            print("Pin number should not be more than 8 digits.")
        pin = input("Enter the pin number (at least 4 digits, not more than 8 digits): ")
    return int(pin)

def read_file(filename):
    try:
        with open(filename, "r") as f:
            plaintext = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        log_event(f"File {filename} was not found .")
        return None
    return plaintext

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def log_event(event):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {event}\n")

def encrypt_file():
    filename = input("Enter the file name: ")
    plaintext = read_file(filename)
    if plaintext is None:
        return
    total_chars = len(plaintext)
    backup_filename = f"{filename}.{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.backup"
    write_file(backup_filename, plaintext)
    log_event(f"Backed up file {filename} to {backup_filename}")

    a = get_pin()
    term = []
    for n in range(1, total_chars):
        if (ord(plaintext[n]) >= 65 and ord(plaintext[n]) <= 90) or (ord(plaintext[n]) >= 97 and ord(plaintext[n]) <= 122):
            t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + a*n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 25) % 50 - 25
        else:
            t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 10) % 18 - 9
        term.append(t)
    print("Term:", term)

    ciphertext = ceaser_cipher(plaintext, term, total_chars)
    write_file(filename, ciphertext)
    log_event(f"Encrypted file {filename}")
    print("File encrypted successfully.")

encrypt_file()

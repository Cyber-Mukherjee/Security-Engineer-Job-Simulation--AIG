# Gaurav Mukherjee (Security Analyst @AIG)

from zipfile import ZipFile
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        print(f"[+] Password found: {password}")
        return True
    except Exception as e:
        # Incorrect password
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('wordlist.txt', 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf, password):
                    break
            else:
                print("[+] Password not found in list")

if __name__ == "__main__":
    main()
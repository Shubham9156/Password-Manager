from cryptography.fernet import Fernet
import hashlib
import getpass

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message, key):
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    return cipher_suite.decrypt(encrypted_message).decode()

def hash_password(password):
    # Use a strong password hashing algorithm (e.g., bcrypt) in a production system
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("Password Manager with Multi-Factor Authentication")
    master_password = getpass.getpass("Enter your master password: ")

    # Hash the master password for storage and comparison
    hashed_master_password = hash_password(master_password)

    # Simulate MFA using a simple PIN
    mfa_pin = input("Enter your MFA PIN: ")

    # Compare the hashed PIN with a stored hashed PIN
    stored_mfa_pin = hash_password(mfa_pin)
    if stored_mfa_pin != hashed_master_password:
        print("MFA PIN is incorrect. Access denied.")
        return

    print("Access granted. You can now manage your passwords securely.")

    while True:
        choice = input("Enter '1' to store a password, '2' to retrieve a password, or 'q' to quit: ")

        if choice == '1':
            service = input("Enter the service or website name: ")
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            encrypted_password = encrypt_message(password, key)
            # Store the encrypted_password along with the service and username

        elif choice == '2':
            service = input("Enter the service or website name: ")
            # Retrieve the encrypted_password based on the service and username
            # Decrypt the password and display it
            decrypted_password = decrypt_message(encrypted_password, key)
            print(f"Password for {service}: {decrypted_password}")

        elif choice.lower() == 'q':
            break

if __name__ == "__main__":
    main()

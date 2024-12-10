from Labs.Lab_5 import root_ca, user_key_management, verify_signature
import os


def print_menu():
    print("\nChoose an option:")
    print("1. Generate CA (Root Certificate Authority)")
    print("2. Generate User Certificate")
    print("3. Sign a File")
    print("4. Verify File Signature")
    print("5. Exit")


def run():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                root_ca.generate_root_ca()
                print("Root Certificate Authority (CA) generated successfully.")

            elif choice == "2":
                username = input("Enter the username for the certificate: ")
                user_key_management.generate_user_key(username)
                print(f"User certificate for '{username}' generated successfully.")

            elif choice == "3":
                username = input("Enter the username for signing: ")
                file_path = input("Enter the file path to sign: ")
                if not os.path.exists(file_path):
                    # Automatically create the missing file
                    with open(file_path, "w") as f:
                        f.write("This is a placeholder document for signing.")
                    print(f"File '{file_path}' was missing and has been created.")
                user_key_management.sign_file(f"{username}_key.pem", file_path)
                print(f"File '{file_path}' signed successfully.")

            elif choice == "4":
                username = input("Enter the username for verification: ")
                file_path = input("Enter the file path to verify: ")
                signature_path = input("Enter the signature file path: ")
                if file_path == signature_path:
                    print("Error: The file path and signature path cannot be the same.")
                elif not all(map(os.path.exists, [file_path, signature_path])):
                    print("Error: One or more files do not exist.")
                else:
                    verify_signature.verify_signature(
                        f"{username}_public_key.pem", file_path, signature_path
                    )

            elif choice == "5":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    run()

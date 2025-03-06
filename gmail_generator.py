import random
import string

def generate_gmail(num=1):
    emails = []
    for _ in range(num):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        emails.append(f"{username}@gmail.com")
    return emails

def save_to_file(emails, filename="generated_gmails.txt"):
    with open(filename, "w") as file:
        for email in emails:
            file.write(email + "\n")
    print(f"\n✅ {len(emails)} Gmail addresses saved to {filename}")

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of Gmail addresses to generate: "))
        if count <= 0:
            print("❌ Please enter a positive number.")
        else:
            generated_emails = generate_gmail(count)
            for email in generated_emails:
                print(email)
            save_to_file(generated_emails)
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

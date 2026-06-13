import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Sender details
sender_email = "shahdivyang1998@gmail.com"
app_password = "your_app_password"

# Get receiver email from user
receiver_email = input("Enter Email Address: ")

# Check if email already exists
try:
    with open("registered_emails.txt", "r") as file:
        registered_emails = [line.strip().lower() for line in file.readlines()]
except FileNotFoundError:
    registered_emails = []

if receiver_email.lower() in registered_emails:
    print("❌ This email is already registered with us.")
    print("Please try with another email address.")
else:
    # Save new email
    with open("registered_emails.txt", "a") as file:
        file.write(receiver_email + "\n")

    # Create email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Welcome - Email Sent Using Python"

    body = """
Hello,

Thank you for registering.


Regards,
Divyang Shah
"""

    message.attach(MIMEText(body, "plain"))

    file_path = "da.pdf"

    server = None

    try:
        # Attach PDF
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename={file_path}"
            )

            message.attach(part)

        # Connect to Gmail SMTP Server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login
        server.login(sender_email, app_password)

        # Send Email
        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )

        print("✅ Email sent successfully.")
        print("✅ Email registered successfully.")

    except Exception as e:
        print("❌ Something went wrong:", e)

    finally:
        if server:
            server.quit()
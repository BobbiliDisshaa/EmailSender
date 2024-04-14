import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

def send_email(sender_email, sender_password, recipient_email, subject, message):

    smtp_server = 'smtp-mail.outlook.com'
    port = 587

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, sender_password)

    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = recipient_email
    email['Subject'] = subject

    email.attach(MIMEText(message, 'plain'))

    server.sendmail(sender_email, recipient_email, email.as_string())

    server.quit()

def send_email_from_gui():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end").strip()

    try:
        send_email(sender_email, sender_password, recipient_email, subject, message)
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

root = tk.Tk()
root.title("Email Sender")

sender_email_label = tk.Label(root, text="Sender Email:")
sender_email_label.grid(row=0, column=0, padx=5, pady=5)
sender_email_entry = tk.Entry(root)
sender_email_entry.grid(row=0, column=1, padx=5, pady=5)

sender_password_label = tk.Label(root, text="Sender Password:")
sender_password_label.grid(row=1, column=0, padx=5, pady=5)
sender_password_entry = tk.Entry(root, show="*")
sender_password_entry.grid(row=1, column=1, padx=5, pady=5)

recipient_email_label = tk.Label(root, text="Recipient Email:")
recipient_email_label.grid(row=2, column=0, padx=5, pady=5)
recipient_email_entry = tk.Entry(root)
recipient_email_entry.grid(row=2, column=1, padx=5, pady=5)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=3, column=0, padx=5, pady=5)
subject_entry = tk.Entry(root)
subject_entry.grid(row=3, column=1, padx=5, pady=5)

message_label = tk.Label(root, text="Message:")
message_label.grid(row=4, column=0, padx=5, pady=5)
message_text = tk.Text(root, height=5, width=30)
message_text.grid(row=4, column=1, padx=5, pady=5)

send_button = tk.Button(root, text="Send Email", command=send_email_from_gui)
send_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

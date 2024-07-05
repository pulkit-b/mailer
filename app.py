from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    sender_email = "kezaartech@gmail.com"  # Replace with your Gmail address
    sender_password = "wytl kiyd urrn eyns"  # Replace with your Gmail password
    receiver_email = "pulkit.b@outlook.com"
    subject = data.get('subject')
    body = "HELLO WORLD"

    if not receiver_email or not subject or not body:
        return jsonify({"error": "Missing required fields: 'to', 'subject', 'body'"}), 400

    try:
        # Create a MIMEText object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

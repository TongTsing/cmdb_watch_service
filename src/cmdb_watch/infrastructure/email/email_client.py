import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cmdb_watch.domain.services.eamil_sender_service import EmailSender


class SMTPEmailClient(EmailSender):
    def __init__(
        self,
        smtp_server: str,
        port: int,
        username: str,
        password: str,
        use_tls: bool = True,
        from_email: str | None = None,
    ):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.from_email = from_email or username

    def send_email(self, recipient: str, subject: str, body: str, html: bool = False):
        msg = MIMEMultipart()
        msg["From"] = self.from_email
        msg["To"] = recipient
        msg["Subject"] = subject

        if html:
            msg.attach(MIMEText(body, "html"))
        else:
            msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                if self.use_tls:
                    server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)

        except Exception as e:
            raise RuntimeError(f"Failed to send email: {e}")

import pytest
from cmdb_watch.infrastructure.email.email_client import SMTPEmailClient


@pytest.mark.skip(reason="This test sends an actual email. Uncomment to run.")
def test_email_client():
    email_client = SMTPEmailClient(
        smtp_server="smtp.163.com",
        port=25,
        username="dearhaly@163.com",
        password="AQh9wPnhb5bE8VUi",
        use_tls=False,  # 根据你的 SMTP 服务器配置调整
        from_email="dearhaly@163.com",
    )

    try:
        email_client.send_email(
            recipient="togqing@canway.net",
            subject="Test Email from SMTPEmailClient",
            body="This is a test email sent from the SMTPEmailClient in cmdb_watch.",
        )
        print("Email sent successfully.")
    except Exception as e:
        raise RuntimeError(f"Failed to send email: {e}")

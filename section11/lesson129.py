import logging.handlers

smtp_host = "smtp.gmail.com"
smtp_port = 587
from_email = "from@gmail.com"
to_email = "to@gmail.com"
username = "username"
password = "password"

logger = logging.getLogger("email")
logger.setLevel(logging.CRITICAL)

handler = logging.handlers.SMTPHandler(
    (smtp_host, smtp_port),
    from_email,
    to_email,
    subject="Admin test log",
    credentials=(username, password),
    secure=(),
    timeout=20
)
logger.addHandler(handler)

logger.info("this is a test log message.")
logger.critical("this is a critical log message.")

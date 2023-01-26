"""exemplo de envio de e-mail"""

import smtplib

SERVER = "localhost"
PORT = 8025


FROM = "teste@teste.com"
TO = ["thiagoabeppe@gmail.com"]
SUBJECT = "E-mail via python"
TEXT = """
Este é um e-mail enviado usando SMTP lib.
<b>Olá Mundo! </b>
""" 
message = f"""\
From: {FROM}
To: {"".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(
    host=SERVER, port= PORT
) as server:
    server.sendmail(FROM,TO, message.encode("utf-8"))
    
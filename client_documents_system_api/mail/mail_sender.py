from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from config.app_config import settings
from schemas import mail_schemas
from typing import List


def confirmation_html(docs: List[str] = None):
    html = """
                    <html> 
                    <body>
                    <h2>Peticion de archivos creada</h2>
                    <p>Hola se le solicita amablemente que ingrese a la plataforma de gestion de archivos 
                    de la inmobiliario y suba los archivos requeridos
                    <br>Gracias</p> 

                    <inputRequiredDocs>
                    </body> 
                    </html>
            """

    return html


class MailSender():
    def __init__(self):
        self.conf = ConnectionConfig(
            MAIL_USERNAME=settings.system_username,
            MAIL_PASSWORD=settings.system_mail_pw,
            MAIL_FROM=settings.system_mail,
            MAIL_PORT=settings.mail_server_port,
            MAIL_SERVER=settings.mail_server,
            MAIL_TLS=True,
            MAIL_SSL=False
        )

    async def send_confirmation_to_client(self, email_info: mail_schemas.RequestCreated, required_docs: List[str]):
        html = confirmation_html()
        message = MessageSchema(
            subject=email_info.dict().get("subject"),
            recipients=[email_info.dict().get("client_email"), ],
            body=html,
            subtype="html"
        )

        fm = FastMail(self.conf)
        await fm.send_message(message)

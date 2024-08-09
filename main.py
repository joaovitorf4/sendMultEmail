from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, textmessage, receiver_email):
    sender_email = os.getenv('SMTP_USER')
    #receiver_email = "ti@cedoc.net.br"
    password = os.getenv('SMTP_PASSWORD')

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(textmessage, "html"))

    with smtplib.SMTP_SSL(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT')) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

with open("teste.csv", 'r', encoding="utf-8") as f:
        data = f.read().splitlines()
    
datasplited = []

for i in range (len(data)):
    datasplited.append(data[i].split(";"))

for j in range (len(datasplited)):
    textmessage = f"""Segue abaixo as credenciais de acesso ao sistema.<br><br>

        Link: https://fd.cedoc.net.br/filedirector/web<br>
        Usuário: cohab\\{datasplited[j][0]}<br>
        Senha: {datasplited[j][2]}<br>

        Obs.: O sistema solicitará a mudança de senha após o primeiro acesso. Qualquer dúvida favor entrar em contato no email ti@cedoc.net.br<br><br>

        Este é um email automático, favor não responder a ele.<br><br>

        Atenciosamente,<br><br>

        CEDOC"""
    send_email("Acesso ao sistema", textmessage, datasplited[j][1])
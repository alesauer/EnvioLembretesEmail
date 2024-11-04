import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Configurações do servidor de e-mail
USUARIO = ""  # Somente o login, sem o domínio ou o @
SENHA = "" # Senha para o domínio REDE
SMTP_SERVER = ""
SMTP_PORT = 

# Função para enviar e-mail
def enviar_email(destinatario, assunto, mensagem):
    try:
        # Configuração da conexão com o servidor SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Inicia a conexão segura com STARTTLS
        server.login(USUARIO, SENHA)  # Autentica com o nome de usuário e senha
        
        # Criação do e-mail
        email = MIMEMultipart()
        email['From'] = USUARIO  # Envia apenas o login como remetente
        email['To'] = destinatario
        email['Subject'] = assunto
        email.attach(MIMEText(mensagem, 'plain'))
        
        # Envio do e-mail
        server.sendmail(USUARIO, destinatario, email.as_string())
        server.quit()
        
        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")


# Leitura e envio de e-mails com base no CSV
def processar_e_envia_emails():
    # Lê o arquivo CSV
    tarefas = pd.read_csv('tarefas.csv')
    
    for linha in tarefas.itertuples():
        tarefa = linha.tarefa
        data_prazo = linha.data_prazo
        hora_prazo = linha.hora_prazo
        email_destino = linha.email
        
        # Cria o assunto e o corpo do e-mail
        assunto = f"Lembrete de Tarefa: {tarefa}"
        mensagem = f"Olá!\n\nEste é um lembrete para a tarefa: {tarefa}\nData de prazo: {data_prazo}\nHora de prazo: {hora_prazo}\n\nBoa sorte e sucesso!"
        
        # Envia o e-mail
        enviar_email(email_destino, assunto, mensagem)

# Executa o envio dos e-mails
processar_e_envia_emails()


# 📧 Sistema de Envio de Lembretes por E-mail

Este projeto é um sistema de envio automático de lembretes por e-mail, desenvolvido em Python. Ele utiliza a biblioteca `smtplib` para enviar e-mails e a `pandas` para manipulação de dados a partir de um arquivo CSV contendo as informações das tarefas.

## 📝 Descrição do Projeto

O script `enviamail.py` lê um arquivo `tarefas.csv` contendo a lista de tarefas, prazos e os e-mails de destinatários. Com essas informações, o script envia e-mails personalizados com os detalhes de cada tarefa. O processo de envio de e-mails é feito de forma segura usando `STARTTLS` para criptografar a comunicação com o servidor SMTP.

## 📋 Funcionalidades

- Leitura de dados de tarefas de um arquivo CSV.
- Configuração e autenticação segura com um servidor SMTP.
- Criação e envio de e-mails personalizados para cada destinatário.
- Notificação no console indicando o sucesso ou falha no envio de cada e-mail.

## 🔧 Estrutura do Código

- **Bibliotecas Utilizadas**: 
  - `smtplib`: Para envio de e-mails.
  - `email.mime`: Para criar mensagens de e-mail no formato MIME.
  - `pandas`: Para manipulação e leitura do arquivo CSV.

- **Principais Funções**:
  - `enviar_email(destinatario, assunto, mensagem)`: Configura o servidor SMTP e envia um e-mail.
  - `processar_e_envia_emails()`: Lê o arquivo `tarefas.csv`, processa as informações, e chama a função de envio de e-mail para cada tarefa.

## 📁 Estrutura do Arquivo CSV

O arquivo `tarefas.csv` deve conter as seguintes colunas:
- `tarefa`: Descrição da tarefa.
- `data_prazo`: Data de prazo da tarefa.
- `hora_prazo`: Hora do prazo.
- `email`: Endereço de e-mail do destinatário.

### Exemplo de Estrutura do CSV

```csv
tarefa,data_prazo,hora_prazo,email
"Finalizar relatório", "2024-11-05", "14:00", "exemplo@dominio.com"
"Reunião de projeto", "2024-11-06", "09:00", "exemplo2@dominio.com"
```

## 🚀 Como Executar

1. **Instalação das Dependências**:
   - Certifique-se de ter as bibliotecas `pandas` instaladas.
   - Execute o comando:
     ```bash
     pip install pandas
     ```

2. **Configuração do Servidor SMTP**:
   - No código, substitua as informações `USUARIO`, `SENHA`, `SMTP_SERVER` e `SMTP_PORT` com as credenciais do seu servidor de e-mail.

3. **Execução do Script**:
   - Salve o arquivo `tarefas.csv` no mesmo diretório do script.
   - Execute o script `enviamail.py`:
     ```bash
     python enviamail.py
     ```

## ⚠️ Avisos Importantes

- **Segurança**: Tenha cuidado ao armazenar credenciais de e-mail no código. Considere o uso de variáveis de ambiente ou métodos seguros para gerenciar senhas.
- **Configuração SMTP**: Assegure-se de que as configurações SMTP estão corretas e o servidor permite conexões seguras.

## 📌 Contato

Para mais informações, entre em contato com:

- **Autor**: Prof. Sauer
- **E-mail**: sauer@simplificatreinamentos.com.br
- **Redes Sociais**:
  - [Instagram](https://www.instagram.com/prof.alesauer/)
  - [Facebook](https://www.facebook.com/prof.alesauer)
  - [YouTube](https://www.youtube.com/@prof.alesauer)
  - [LinkedIn](www.linkedin.com/in/alesauer)

---

Desenvolvido com ❤️ por Prof. Sauer. Confira mais conteúdos e aulas sobre Python em [www.sauer.pro.br](http://www.sauer.pro.br).

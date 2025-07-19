## ** StackSpot Agent Chat Script

Este script Python realiza autenticação via OAuth2 Client Credentials e envia perguntas para um agente StackSpot, retornando as respostas no terminal.


## Indice

- Python 3.7+
- Credenciais

## Introdução

1. Primeiro voce vai precisar das credenciais. 
- Use este markdown como guia [crendenciais](/credenciais.md) 
Clone este repositório ou copie o script para sua máquina.

Instale as dependências:

bash



pip install requests
Edite o script e preencha as variáveis:

token_url
client_id
client_secret
(Opcional) Edite a lista mensagens com as perguntas que deseja enviar ao agente.

Execute o script:

bash



python seu_script.py
Exemplo de uso
python



mensagens = [
    "Crie um README.md para um hello world em linguagem python.",
    "Crie um script em python que eu possar criar um agente no stackspot",
]
Funcionamento
O script obtém um access_token usando o fluxo OAuth2 Client Credentials.
Para cada mensagem em mensagens, faz uma requisição POST para o endpoint do agente StackSpot.
Exibe a resposta do agente no terminal.
Observações
Certifique-se de que suas credenciais estejam corretas e tenham permissão para acessar o agente.
O AGENT_ID deve ser válido para o seu ambiente StackSpot.
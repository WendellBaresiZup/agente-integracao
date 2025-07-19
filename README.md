## ** StackSpot Agent Chat Script

Este script Python realiza autenticação via OAuth2 Client Credentials e envia perguntas para um agente StackSpot, retornando as respostas no terminal.


## Indice

- Python 3.7+
- Credenciais

## Introdução

1. Primeiro voce vai precisar das credenciais. 
- Use este markdown como guia [crendenciais](/credenciais.md) 

2. Clone este repositório ou copie o script para sua máquina.

```shell
https://github.com/WendellBaresiZup/agente-integracao.git
```

3. Instale as dependências:

```shell
pip install requests
```

4. Edite o script e preencha as variáveis.

```shell
token_url
client_id
client_secret
```

5. Edite o prompt para buscar o resultado que deseja do agente.

#### Exemplo de input
```shell
mensagens = [
    "Crie um README.md para um hello world em linguagem python.",
    "Crie um script em python que eu possar criar um agente no stackspot",
]
```

6. Execute o script:

```shell
python agente.py
```

7. Resposta do agente.
#### Exemplo de output

```shell
Pergunta: Crie um README.md para um hello world em linguagem python.
Resposta do agente: {'message': 'Claro! Aqui está um exemplo simples de README.md para um projeto "Hello World" em Python:\n\n# Hello World em Python\n\nEste é um exemplo simples de um programa "Hello World" escrito em Python.\n\n## Requisitos\n\n- Python 3 instalado em seu sistema\n\n## Como executar\n\n1. Clone este repositório ou baixe o arquivo `hello.py`.\n2. Abra o terminal (prompt de comando).\n3. Navegue até o diretório onde está o arquivo `hello.py`.\n4. Execute o comando:\n\n```bash\npython hello.py\n```\n\n## Código\n\n```python\nprint("Hello, World!")\n```\n\n## Saída esperada\n\n```\nHello, World!\n```\n\n## Licença\n\nEste projeto está licenciado sob a licença MIT.\n\n---\n\nSinta-se à vontade para modificar este exemplo para aprender mais sobre Python!', 'stop_reason': 'stop', 'tokens': {'user': 13, 'enrichment': 16, 'output': 174}, 'knowledge_source_id': []
```
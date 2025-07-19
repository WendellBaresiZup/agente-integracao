---
title: Gerar Credencial e Token de Acesso
sidebar_position: 8
description: Confira como gerar credencial e token de acesso.
last_update:
  date: "06/16/2025"
  author: "StackSpot Team"
---

## **Como gerar o Token de Acesso**

**Passo 1.** [**Acesse o Portal da StackSpot**](https://app.stackspot.com/);

**Passo 2.** Clique no seu avatar e clique na seção **’Meu Perfil’**; 

![](/img/token1.png)

**Passo 3.** Clique na opção **’Token de Acesso’**; 

**Passo 4.** Clique no botão **’Gerar Client Key’** 

As chaves geradas são únicas: 

    - **`client_id`**: identificador do cliente.
    - **`client_key`**: segredo do cliente.
    - **`realm`**: ambiente de acesso.

![](/img/token2.png)

Salve todas as chaves e não compartilhe com ninguém.**

> Toda vez que você entrar nessa seção e clicar na opção **’Gerar Client Key’**, os Tokens anteriores se tornam inválidos.


## **Endpoint para gerar e automatizar o Token**

Envie suas credenciais de acesso no formato Form para receber um token de acesso. Esse token será usado para autenticar as próximas requisições.

- Endpoint:

```bash
/oauth/token
```
- URL completa:


```bash
https://idm.stackspot.com/itau/oidc/oauth/token
```

Confira um exemplo de response:

```bash
{
  "not-before-policy": 0,
  "session_state": "string",
  "scope": "attributes email profile roles",
  "refresh_token": "eyYOURTOKEN.",
  "refresh_expires_in": 1200,
  "access_token": "eyJYOURTOKEN",
  "token_type": "Bearer",
  "expires_in": 1199
}
```
Confira os campos no corpo da requisição via Form:

- **`client_id`**: identificador do cliente.
- **`client_key`**: segredo do cliente (mesmo que `client_secret`).
- **`grant_type`**: tipo de concessão de token.
- **`realm`**: escopo de autenticação.


- O valor retornado em **`access_token`** deve ser usado como Bearer Token no header de autenticação das próximas chamadas às APIs.
- Após obter o **`access_token`**, salve-o em uma variável global chamada **`_.access_token`**. Assim, o token será enviado automaticamente nas próximas requisições, sem precisar informar as credenciais novamente.

Exemplo:

```bash
_.access_token = "access_token";
```
:::tip Dicas!

- A URL base das APIs pode variar de acordo com o contexto e o ambiente do seu projeto. Por exemplo, você pode ver a URL **https://idm.stackspot.com/itau/oidc/oauth/token**. Faça os ajustes conforme o padrão adotado no seu projeto.

- Ferramentas como Insomnia e Postman são recomendadas para consumir as APIs. Com uma coleção pré-configurada, você pode automatizar a autenticação e gerenciar diferentes ambientes de forma mais fácil.

:::
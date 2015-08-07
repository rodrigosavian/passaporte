# Passaporte :)

## Visão Geral
**Passaporte** tem o  objetivo de coletar informações de usuários do Facebook, fornecendo posteriormente através de um serviço REST.

***

### Instalar Redis local
Usado para salvar as chaves do Facebook.

Ubuntu: `apt-get install redis-server`

OSX: `brew install redis`

### Criar nova/ativar env e instalar requirements.txt
`pip install -r requirements.txt`

### Configurar banco de dados no arquivo settings.py
`mysql://<user>:<password>@<host>/<db>`

### Criar banco de dados
`python -v createdb.py`

### Testes
`python -m apps.people.test`

`python -m apps.people.apis.v1.test`

`python -m tornado.test.runtests test`

### Setar `client_id` e `client_secret`
Crie uma app teste no Facebook para este passo:

`curl -X POST -F facebook_client_id=<client_id> http://localhost:8888/config/`

`curl -X POST -F facebook_client_secret=<client_secret> http://localhost:8888/config/`

***

## Rodando o projeto

`python app.py`

***

### Melhorias
 - cache de dados
 - serializer fields
 - remover `requests` e utilizar `AsyncHTTPClient` do tornado
 - autenticação e autorização

### Pontos positivos
 - aprendizado (tornado)
 - oportunidade

### Pontos negativos
 - tempo
 - pouco teste

### Balanço
 - optei por tentar desenvolver uma lib rest para utilizar no projeto e mostrar um pouco de codigo
 - poderia ter usado frameworks que resolveriam todo o trabalho: python-eve, flask-restful, django-restframework.
 - tornado bem fácil, rápido. Gostei bastante.
 - Obrigado!

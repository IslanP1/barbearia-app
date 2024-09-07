# Aplicação de Agendamentos para Barbeiros

Este projeto é uma aplicação de agendamentos para barbeiros, utilizando Django e PostgreSQL, todos configurados em contêineres Docker.

## Configuração Inicial

### Passo 1: Clonar o Repositório

Primeiro, clone este repositório para sua máquina local:

```bash
git clone https://github.com/IslanP1/barbearia-app.git
cd barbearia-app
```
### Passo 2: Criar um arquvo .env

Após clonar o repositório, você precisará configurar o arquivo .env com as credenciais do banco de dados. Crie um arquivo .env na raiz do projeto e adicione o seguinte conteúdo:

```bash
POSTGRES_DB="Seu BD"
POSTGRES_USER="Seu usuário"
POSTGRES_PASSWORD="Sua senha"

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Passo 3: Iniciar o docker e migrações

Inicie os contêineres Docker e com o contêiner em execução, aplique as migrações do banco de dados:
```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
```

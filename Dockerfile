# Usar a imagem oficial do Python como base
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /code

# Copiar o arquivo de requisitos
COPY requirements.txt /code/

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o código da aplicação para o diretório de trabalho do contêiner
COPY . /code/

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

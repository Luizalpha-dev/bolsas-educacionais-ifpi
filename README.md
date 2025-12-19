🎓 Bolsas Educacionais IFPI

Sistema web desenvolvido em Django para gerenciamento de bolsas educacionais do IFPI, permitindo cadastro, edição, listagem e exclusão de bolsas, com interface responsiva utilizando Bootstrap 5 e banco de dados PostgreSQL.


---

-Funcionalidades

1 Listar bolsas disponíveis

2 Cadastrar nova bolsa

3 Editar bolsa

4 Excluir bolsa

5 Interface responsiva com Bootstrap 5

6 CRUD completo

7 Banco de dados PostgreSQL



---

-Tecnologias Utilizadas

Python 3.12+

Django 5/6

PostgreSQL

Bootstrap 5 (via CDN)




---

 Configuração do Ambiente

1️⃣ Clone o repositório

git clone https://github.com/luizalpha-dev/bolsas-educacionais-ifpi.git


---

2️⃣ Crie e ative um ambiente virtual

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate


---

3️⃣ Instale as dependências

pip install -r requirements.txt


---

- Configuração do PostgreSQL

4️⃣ Crie o banco e o usuário no PostgreSQL

CREATE DATABASE bolsa_ifpi;
CREATE USER bloguser WITH ENCRYPTED PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE bolsa_ifpi TO bloguser;


---

5️⃣ Configure o banco no settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bolsa_ifpi',
        'USER': 'bloguser',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


---

-Executando o Projeto

6️⃣ Aplicar migrações

python manage.py makemigrations
python manage.py migrate


---

7️⃣ Criar superusuário

python manage.py createsuperuser


---

8️⃣ Rodar o servidor

python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000/


---

-Interface:

Desenvolvida com Bootstrap 5

Layout simples e responsivo

Navbar fixa com identificação do sistema



---

-Boas Práticas Aplicadas:

Separação de responsabilidades (MVC)

Uso de forms do Django

Validações automáticas

Uso de templates base

Banco de dados profissional (PostgreSQL)



---

- Autor

Projeto desenvolvido para fins acadêmicos – IFPI.


---

-Licença

Este projeto é apenas para fins educacionais.


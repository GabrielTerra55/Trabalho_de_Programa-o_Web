# Trabalho_de_Programa-o_Web
trabalho de web
<h2>Instalação</h2>
<p>para fazer a instalação da aplicação você deve ter o python 3 instalado na sua maquina, além de ser recomendável a criação de um ambiente virtual de desenvolvimento 'venv'</p>
Passo 1- instale as dependencias necessarias da aplicação.<br>
 SO Windows
	
```
pip install requirements.txt       
```
 SO Linux

```
pip install -r requirements.txt
```
Após essa configurações é necessario fazer as migrações, com os comandos:

```
python manage.py makemigrations
python manage.py migrate
```
Após essa configurações já sera possivel rodar a aplicação utilizando-o

```
python manage.py runserver
```

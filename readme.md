# Criando o projeto

Dentro do projeto execute: 'python3 -m venv venv'
Ative usando algum codigo abaixo

# Ativação no Linux

. venv/bin/activate

# Ativação no windows

. venv/script/activate

# Instalação do flask

pip install -U Flask

# Crie e nomeie um arquivo como 'app.py' na raíz dos arquivos
# Codigo base:

from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return <li>Hello, World!!</li>

if __name__ == "__main__":
    app.run(debug=True)
# Executando o projeto pelo terminal

"python3 -m venv venv"
# Linux

. venv/bin/activate
# Windows

. venv/script/activate

# Instalando Flask

pip install -U Flask

# Executar o servidor padrão

flask run
# Executar o servidor no modo 'development'

python app.py

# Dicas extras

- Deixe as páginas HTML dentro das pastas nomeadas de 'templates'
- Arquivos CSS dentro de pastas nomeadas de 'static'

# Documentação oficial

https://flask.palletsprojects.com/en/2.2.x/quickstart/
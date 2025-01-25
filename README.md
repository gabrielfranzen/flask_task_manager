
## Criar ambiente 
`python -m venv .venv`

## Alterar permissão de execução de scripts para Windows (se necessário)
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

## Ativar ambiente Windows
`.venv\Scripts\activate`

## Ativar ambiente Linux MacOs
`source ./.venv/bin/activate`

## Instalar dependências
`pip install -r requirements.txt`

## Configurar banco de dados
Crie o banco de dados no gerenciador de sua preferência, eu utilizei o XAMPP.

nome do BD: flask_task_manager <br>
usuário do BD (padrão do XAMPP): root <br>
(não utilizei senha) <br>

Altere as informações para conexão com o banco de dados no arquivo "config.py":

`SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/flask_task_manager'`


Caso tenha feito algo diferente, siga a padronização:

`SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<usuario>:<senha>@<host>/<nome_do_banco>'`

## Rodar
`python run.py`
 


## criar anbiente
python -m venv .venv

## ativar ambiente Windows
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\activate

## ativar ambiente Linux MacOs
source ./.venv/bin/activate

## instalar dependências
pip install -r requirements.txt 

## rodar
python run.py 
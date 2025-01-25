
## criar ambiente
python -m venv .venv

## alterar permissão de execução de scripts para Windows (se necessário)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

## ativar ambiente Windows
.venv\Scripts\activate

## ativar ambiente Linux MacOs
source ./.venv/bin/activate

## instalar dependências
pip install -r requirements.txt 

## rodar
python run.py 

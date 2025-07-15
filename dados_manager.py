import json
import os

arquivo_recorde = 'recorde.json'

def carregarPontuacao():
  if not os.path.exists(arquivo_recorde):
    return 0
  
  try:
    with open(arquivo_recorde, 'r') as f:
      dados = json.load(f)
      return dados.get('recorde', 0)
  except Exception:
    return 0
  
def salvarRecorde(pontuacao):
  try:
    with open (arquivo_recorde, 'w') as f:
      json.dump({'recorde': pontuacao}, f)
  except Exception as e:
    print(f'Erro ao salvar o recorde: {e}')
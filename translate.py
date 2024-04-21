# %%
import pandas as pd
import os
import dotenv
import openai
from tqdm import tqdm
import easygui

# %%
# Carrega a variável de ambiente com o API KEY da OpenAI
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# %%
# Função para prever o sexo usando a API da OpenAI
def traducao(frase):
    print(f"Processando a frase: {frase}")  # Adiciona um print para acompanhar o progresso
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente muito inteligente."},
            {"role": "user", "content": f"""
             Qual é a tradução para português da {frase}? O retorno ser somente o texto em porturguês.
             
             Exemplos:
             Olá
             Mudar idioma
             Faça login em sua conta
             """}
        ]
    )
    text = response.choices[0].message.content.strip().lower()
    return text
# %%
# Solicitar ao usuário selecionar o arquivo CSV
nome_arquivo = easygui.fileopenbox(title="Selecione o arquivo CSV contendo as frases", filetypes=["*.csv"])

if not nome_arquivo:
    print("Nenhum arquivo selecionado. Encerrando o programa.")
    exit()

# Ler o arquivo CSV
print(f"Lendo o arquivo '{nome_arquivo}' com as frases...")
frase = pd.read_csv(nome_arquivo, sep=',')

# %%
# Iniciar a barra de progresso
pbar = tqdm(total=len(frase), desc="Traduzindo frases")

# Aplicar a função de tradução a cada linha do DataFrame usando apply com axis=1
for index, row in frase.iterrows():
    frase.at[index, 'Portuguese'] = traducao(row['English'])
    pbar.update(1)  # Atualizar a barra de progresso

# Fechar a barra de progresso
pbar.close()

# %%
# Salvar o DataFrame atualizado de volta para um arquivo CSV
print("Salvando os resultados no arquivo CSV...")
frase.to_csv("traducao_gpt.csv", index=False)

print("Processamento concluído.")

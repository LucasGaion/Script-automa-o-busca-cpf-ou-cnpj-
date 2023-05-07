import pandas as pd
import requests


# requisição da api
def verificar_cadastro(documento):
    print(
        "\n--Gerando consulta Accounting (CPF): ---")
    url = f'https://banking.meu.cash/v2.0/fastcash-prd/clients/external-id/{documento}?active=true&fields=id&tiny=true'
    print("\nLink de url de api gerado com sucesso ->", url)
    headers = {
        'Authorization': 'Basic cmFmYWVsLmZyZWlyZTo5N3JhZmFlbA==',
        'Fineract-Platform-TenantId': 'default'
    }
    response = requests.get(url, headers=headers)  # validando a api
    if response.status_code == 200:
        return 'Documento encontrado'
    elif response.status_code == 404:
        return 'Documento nao encontrado'
    else:
        return 'Erro na requisicao'


# abrindo o arquivo -> entrada.csv e lendo o documento
df = pd.read_csv('entradaCpf.csv', header=None, names=['documento'])

# # removendo a pontuação dos números
# df['documento'] = df['documento'].str.replace('[./-]', '', regex=True)

# aplicando função na planilha de saida tendo o documento e se ele foi encontrado ou nao
df['resultado'] = df['documento'].apply(verificar_cadastro)

# ordenando o resultado pela coluna 'resultado'
df = df.sort_values('resultado')

# salvando na planilha de saida o resultado
df.to_csv('saidaCpf.csv', index=False, header=['documento', 'resultado'])

print(
    "\n---Finalizando a consulta Accounting (CPF) com sucesso: --")

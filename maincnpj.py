import json
import pandas as pd
import requests
import urllib.parse


# requisição da api
def verificar_cadastro(cnpj):
    print(
        "\n--Gerando consulta Accounting (CNPJ): ---")
    encoded_cnpj = urllib.parse.quote(cnpj)
    url = f'https://banking.meu.cash/v1.0/fastcash-prd/fineract-provider/api/v1/search?exactMatch=true&query={encoded_cnpj}&resource=clients'
    print("\nLink de url de api gerado com sucesso ->", url)
    headers = {
        'Authorization': 'Basic cmFmYWVsLmZyZWlyZTo5N3JhZmFlbA==',
        'Fineract-Platform-TenantId': 'default'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = json.loads(response.text)
        if len(result) > 0:
            return 'CNPJ encontrado'
        else:
            return 'CNPJ nao encontrado'
    elif response.status_code == 404:
        return 'CNPJ nao encontrado'
    else:
        return 'Erro na requisicao'



# abrir o arquivo -> entrada.csv e lendo o CNPJ/documento
df = pd.read_csv('entradaCnpj.csv', header=None, names=['cnpj'])

# aplicando função na planilha de saída tendo o CNPJ/documento e se ele foi encontrado ou não
df['resultado'] = df['cnpj'].apply(verificar_cadastro)

# salvando na planilha de saída o resultado
df.to_csv('saidaCnpj.csv', index=False, header=['cnpj', 'resultado'])

# ordenando o resultado pela coluna 'resultado'
df = df.sort_values('resultado')

# salvando na planilha de saida o resultado
df.to_csv('saidaCnpj.csv', index=False, header=['documento', 'resultado'])

print(
    "\n---Finalizando a consulta Accounting (CNPJ) com sucesso: --")
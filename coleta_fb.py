import requests
import json
import csv
# Opção 1
base_url = "https://graph.facebook.com/"
versao = "v3.1/"
objeto = "10155580409780079"
campos = "id,comments.limit(100),reactions"

access_token = "" \
               ""
url = "%s%s%s?fields=%s&access_token=%s" % (base_url, versao, objeto, campos, access_token)

dados = requests.get(url).json()
print(json.dumps(dados, indent=4))

with open("facebook_data.json", mode="a") as meu_arquivo:
    json.dump(dados, meu_arquivo, indent=4)

meu_arquivo_csv = open('facebook_data.csv', mode='a', encoding='utf-8')
writer = csv.writer(meu_arquivo_csv)
for dado in dados['comments']['data']:
    writer.writerow([dado['id'], dado['created_time'], dado['message']])
meu_arquivo.close()

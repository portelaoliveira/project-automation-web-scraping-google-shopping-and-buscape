from pathlib import Path

import pandas as pd

from functions import list_offers_found, send_email

# importar/visualizar a base de dados
table_products = pd.read_excel("data/buscas.xlsx")

# Gerar tabela de ofertas
table_offers = list_offers_found(table_products)

# enviar por e-mail o resultado da tabela
name = "Haroldo"
to = ["haroldo.santos@ruraltech.com.br"]
subject = "Produto(s) Encontrado(s) na faixa de preço desejada"
body = f"""
<!DOCTYPE html>
<html>
<p>Faaaaala, {name}</p>
<p>Encontramos alguns produtos em oferta dentro da faixa de preço desejada. Segue a tabela com detalhes</p>
{table_offers.to_html(index=False)}
<p>Qualquer dúvida estou à disposição</p>
<p>Att., Portela</p>
</html>
"""
path_file = Path(r"test\ofertas.xlsx")
attachment = [Path.cwd() / path_file]

send_email(attachment, to, subject, body)

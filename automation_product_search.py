import pandas as pd

from functions import list_offers_found

# importar/visualizar a base de dados
table_products = pd.read_excel("data/buscas.xlsx")
list_offers_found(table_products)

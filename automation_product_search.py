import time

import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome()

# importar/visualizar a base de dados
table_products = pd.read_excel("data/buscas.xlsx")
print(table_products)

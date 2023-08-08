from selenium import webdriver

import pandas as pd
import time

driver = webdriver.Chrome()

# importar/visualizar a base de dados
table_products = pd.read_excel("data/buscas.xlsx")
print(table_products)

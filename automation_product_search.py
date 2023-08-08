from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd
import time

driver = webdriver.Chrome()

# importar/visualizar a base de dados
table_products = pd.read_excel("data/buscas.xlsx")
print(table_products)

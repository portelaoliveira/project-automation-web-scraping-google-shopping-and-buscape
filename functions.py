from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def have_terms_banned_(list_terms_banned, name):
    have_terms_banned = False
    for word in list_terms_banned:
        if word in name:
            have_terms_banned = True

    return have_terms_banned


def have_all_terms_product_(list_terms_products, name):
    have_all_terms_product = True
    for word in list_terms_products:
        if word not in name:
            have_all_terms_product = False

    return have_all_terms_product


def formated_price(price):
    formated_price = (
        price.replace("R$", "")
        .replace(" ", "")
        .replace(".", "")
        .replace(",", ".")
    )

    return formated_price


def search_google_shopping(
    driver, product, terms_banned, price_min, price_max
):
    # entrar no google
    driver.get("https://www.google.com/")
    driver.maximize_window()

    # tratar os valores que vieram da tabela
    product = product.lower()
    terms_banned = terms_banned.lower()
    list_terms_banned = terms_banned.split(" ")
    list_terms_products = product.split(" ")
    price_max = float(price_max)
    price_min = float(price_min)

    # pesquisar o nome do produto no google
    driver.find_element(
        By.XPATH,
        '//*[@id="APjFqb"]',
    ).send_keys(product)
    driver.find_element(
        By.XPATH,
        '//*[@id="APjFqb"]',
    ).send_keys(Keys.ENTER)

    sleep(2)
    # clicar na aba shopping
    elements = driver.find_elements(By.CLASS_NAME, "GKS7s")
    for item in elements:
        if "Shopping" in item.text:
            item.click()
            break

    # pegar a lista de resultados da busca no google shopping
    list_results = driver.find_elements(By.CLASS_NAME, "sh-dgr__grid-result")
    sleep(5)

    # para cada resultado, ele vai verificar se o resultado corresponde a todas as nossas condicoes
    list_offers = []  # lista que a função vai me dar como resposta
    for results in list_results:
        name = results.find_element(By.CLASS_NAME, "tAxDx").text
        name = name.lower()

        # verificacao do nome - se no nome tem algum termo banido
        have_terms_banned = have_terms_banned_(list_terms_banned, name)

        # verificar se no nome tem todos os termos do nome do produto
        have_all_terms_product = have_all_terms_product_(
            list_terms_products, name
        )

        if (
            not have_terms_banned and have_all_terms_product
        ):  # verificando o nome
            try:
                price = results.find_element(By.CLASS_NAME, "a8Pemb").text
                price = formated_price(price)
                price = float(price)
                # verificando se o preco ta dentro do minimo e maximo
                if price_min <= price <= price_max:
                    element_link = results.find_element(
                        By.CLASS_NAME, "aULzUe"
                    )
                    element_father = element_link.find_element(By.XPATH, "..")
                    link = element_father.get_attribute("href")
                    list_offers.append((name, price, link))
            except:
                continue

    sleep(10)

    return list_offers


def search_buscape(driver, product, terms_banned, price_min, price_max):
    # tratar os valores da função
    price_max = float(price_max)
    price_min = float(price_min)
    product = product.lower()
    terms_banned = terms_banned.lower()
    list_terms_banned = terms_banned.split(" ")
    list_terms_products = product.split(" ")

    # entrar no buscape
    driver.get("https://www.buscape.com.br/")
    driver.maximize_window()

    # pesquisar pelo produto no buscape
    driver.find_element(
        By.XPATH,
        '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input',
    ).send_keys(product, Keys.ENTER)
    sleep(10)

    # pegar a lista de resultados da busca do buscape
    sleep(5)
    list_results = driver.find_elements(
        By.CLASS_NAME, "SearchCard_ProductCard_Inner__7JhKb"
    )
    sleep(5)

    # para cada resultado
    list_offers = []
    for results in list_results:
        try:
            price = results.find_element(
                By.CLASS_NAME, "Text_MobileHeadingS__Zxam2"
            ).text
            name = results.find_element(
                By.CLASS_NAME, "SearchCard_ProductCard_Name__ZaO5o"
            ).text
            name = name.lower()
            link = results.get_attribute("href")

            # verificacao do nome - se no nome tem algum termo banido
            have_terms_banned = have_terms_banned_(list_terms_banned, name)

            # verificar se no nome tem todos os termos do nome do produto
            have_all_terms_product = have_all_terms_product_(
                list_terms_products, name
            )

            if not have_terms_banned and have_all_terms_product:
                price = formated_price(price)
                price = float(price)
                if price_min <= price <= price_max:
                    list_offers.append((name, price, link))
        except:
            pass

    sleep(10)

    return list_offers


if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Chrome()
    # lista_google_shopping = search_google_shopping(
    #     driver, "iphone 12 64gb", "mini watch", "3000", "3500"
    # )
    # print(lista_google_shopping)

    lista_buscape = search_buscape(
        driver, "iphone 12 64gb", "mini watch", "3000", "3500"
    )
    print(lista_buscape)

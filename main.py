# Scraper do Comida di Buteco
# Autor: Matheus Pestana (matheus.pestana@iesp.uerj.br)

import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "http://www.comidadibuteco.com.br/category/butecos/rio-de-janeiro/page/"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s)

lista_links = []

for i in range(1, 10):
    # Abre o site
    driver.get(url + str(i))
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    # Busca o 'div' que estão na classe w-container
    posts = soup.find('div', {'class': 'row text-left'})

    # Dentro desse 'div', ou seja, um box, busca todos os links
    posts_links = posts.find_all('a')

    for links in posts_links:
        postagem = links.get('href')
        lista_links.append(postagem)
    print("Página " + str(i) + "...")

lista_links = [i for i in lista_links if 'page' not in i]
lista_links = [i for i in lista_links if 'google.com' not in i]
lista_links = [i for i in lista_links if 'category' not in i]

df = pd.DataFrame(data={'links': lista_links})

df.to_csv('links.csv')
print("Salvando arquivo de links e iniciando nova etapa...")

dados_restaurante = []

for link in df['links']:
    driver.get(link)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    restaurante = soup.find('h2', {'class': 'title'}).text

    print("Baixando dados de " + restaurante)

    coluna = soup.find('div', {'class': 'col-8 text-left'}).find_all('p')

    prato = coluna[0].strong
    prato_texto = prato.text
    descricao = prato.next.next.next
    endereco = descricao.next.next.next.next.next.next.next
    # bairro = endereco.split('|')[1]#.split(',')[0][1:]
    telefone = coluna[1].text
    horarios = coluna[2].text

    restaurante_linha = [restaurante, link, prato_texto, descricao, endereco, telefone, horarios]

    dados_restaurante.append(restaurante_linha)

print("Salvando em dataframe...")
restaurantes = pd.DataFrame(dados_restaurante,
                            columns=['Restaurante', 'Link', 'Prato', 'Descrição', 'Endereço', 'Telefone', 'Horários'])

print("Exportando para csv...")
restaurantes.to_csv("restaurantes.csv")

print("Tudo ok!")

driver.quit()

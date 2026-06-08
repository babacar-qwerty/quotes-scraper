from bs4 import BeautifulSoup
import sqlite3
import lxml
import requests
import os

# Script qui récupère les citations ainsi que les auteurs du site quotes.toscrape et qui les stocke dans une base de données.

# Création de la base de données
db = sqlite3.connect('Quotes.db')
print(os.path.abspath('Quotes.db'))
cursor = db.cursor()
# Unique comme ça ça ne prends pas les doublons vu qu'on peut avoir plusieurs auteurs mais pas plusieurs citations
cursor.execute("""CREATE TABLE IF NOT EXISTS Quotes(
               author TEXT,
               quote TEXT UNIQUE) """)


# Boucle pour parcourir toutes les pages
# page=1
# num_quotes=0
# while 1:
#     html_text = requests.get(f'https://quotes.toscrape.com/page/{page}/').text

#     soup=BeautifulSoup(html_text,'lxml')

#     quote_cards= soup.find_all('div', class_='quote')

# # Pour chaque card container ça récupère la citation + l'auteur et ça le met dans la base de données
#     for each in quote_cards:
#         quote= each.find('span', class_='text').text
#         # print(quote)
#         author=each.find('small', class_='author').text
#         # Si ya doublons alors ça skip
#         cursor.execute(""" INSERT OR IGNORE INTO Quotes(author,quote)
#                        VALUES(?,?)""",(author,quote))
#         num_quotes+=1
    
#     # Enregistrement:
#     db.commit()
#     print("!!!---Quotes successfuly saved---!!!")

#     # Après la dernière page ça casse la boucle
#     next_btn=soup.find('li', class_='next')
#     if next_btn is None:
#         break

#     page += 1

# db.close()
#Note : navigator.userAgent pour avoir le user agent quand tu as la flemme
import requests
import html_text
from bs4 import BeautifulSoup
Nbre = int(input("Combien voulez vous générer de nom et prénom : "))
from colorama import Back, Fore, Style, deinit, init
compteur = 0
while Nbre > compteur: 
    url = 'https://fr.fakenamegenerator.com/gen-random-fr-fr.php'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    features="html.parser"
    Rqt = requests.get(url, headers=headers)
    soup = BeautifulSoup(Rqt.text, features=features)
    Name = str(soup.find('h3'))
    
    Name = html_text.extract_text(Name)
    print(Style.BRIGHT + Fore.GREEN + str(Name))
    f = open("Nom.txt", "a")
    f.write(str(Name)+"\n")
    compteur +=1

# TP Annuaire d'avocat
#
# L'objectif est de récupérer les informations des différends avocats sur les 50 premières pages grâce à la librairie `BeautifulSoup`.
#
# Il faudra récupérer le nom, prénom, adresse, email, telephone de l'avocat.
#
# Si des informations sont manquantes, les remplacer par 'Introuvable'.
#
# Une fois les informations récupérées, il faudra les enregistrées au format CSV
#
# voici le lien de la première page --> https://www.barreaudenice.com/annuaire/avocats/?fwp_paged=1


import requests
from bs4 import BeautifulSoup
import csv
import re
from tqdm import tqdm, trange


def clean_html_content(s: str):
    s = s.replace('\n', ' ')
    s = re.sub(r'\s+', ' ', s)
    s = s.replace('Email :', '')
    s = s.replace('T .', '')
    s = s.strip()
    return s


if __name__ == '__main__':
    empty_str_placeholder = 'Introuvable'
    url_base = 'https://www.barreaudenice.com'
    how_many_pages = 50
    content_to_save = [['nom_prenom', 'adresse', 'email', 'telephone']]
    csv_filename = 'annuaire_avocats.csv'

    with open(csv_filename, 'w', encoding='utf8') as f_to_write:
        f_to_write.write('')

    for fwp_page in trange(1, how_many_pages + 1):
        url_path = f'/annuaire/avocats/?fwp_paged={fwp_page}'
        html_content = requests.get(url_base + url_path).text
        soup = BeautifulSoup(html_content, 'html.parser')
        for info_avocat in tqdm(soup.find_all('div', class_='annuaire-single'), leave=False):
            nom_prénom = info_avocat.find('h3')
            adresse = info_avocat.find('span', class_='adresse')
            email = info_avocat.find('span', class_='email')
            telephone = info_avocat.find('span', class_='telephone')
            tmp = []
            for v in [nom_prénom, adresse, email, telephone]:
                if v is None:
                    tmp.append(empty_str_placeholder)
                else:
                    tmp.append(clean_html_content(v.text))
            if tmp not in content_to_save:
                content_to_save.append(tmp)
        with open(csv_filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerows(content_to_save)
            content_to_save = []

    with open(csv_filename, 'r', encoding='cp1252') as f_to_read:
        lines_to_keep = [line for line in f_to_read.readlines()
                         if line != '\n']
        with open(csv_filename, 'w', encoding='utf8') as f_to_write:
            f_to_write.writelines(lines_to_keep)

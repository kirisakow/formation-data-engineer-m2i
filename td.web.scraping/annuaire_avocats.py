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


def clean_csv_file(csv_filename: str) -> None:
    """Fixes Windows-related encoding problems (CP1252 -> UTF8)
    and deletes empty lines in the CSV file"""
    with open(csv_filename, 'r', encoding='cp1252') as f_to_read:
        lines_to_keep = [line for line in f_to_read.readlines()
                         if line != '\n']
        with open(csv_filename, 'w', encoding='utf8') as f_to_write:
            f_to_write.writelines(lines_to_keep)


if __name__ == '__main__':
    EMPTY_DATA_PLACEHOLDER = 'Introuvable'
    URL_BASE = 'https://www.barreaudenice.com'
    URL_PATH = '/annuaire/avocats/?fwp_paged={0}'
    HOW_MANY_PAGES = 50
    CSV_FILENAME = 'annuaire_avocats.csv'

    with open(CSV_FILENAME, 'w', encoding='utf8') as f_to_write:
        f_to_write.write('')

    header = ['nom_prenom', 'adresse', 'email', 'telephone']
    page_data = [header]
    for fwp_page in trange(1, HOW_MANY_PAGES + 1):
        url_path = URL_PATH.format(fwp_page)
        html_content = requests.get(URL_BASE + url_path).text
        soup = BeautifulSoup(html_content, 'html.parser')
        for info_avocat in tqdm(soup.find_all('div', class_='annuaire-single'),
                                leave=False):
            nom_prénom = info_avocat.find('h3')
            adresse = info_avocat.find('span', class_='adresse')
            email = info_avocat.find('span', class_='email')
            telephone = info_avocat.find('span', class_='telephone')
            individual_contact_data = []
            for html_content in [nom_prénom, adresse, email, telephone]:
                if html_content is None:
                    individual_contact_data.append(EMPTY_DATA_PLACEHOLDER)
                else:
                    clean_html = clean_html_content(html_content.text)
                    individual_contact_data.append(clean_html)
            if individual_contact_data not in page_data:
                page_data.append(individual_contact_data)
        with open(CSV_FILENAME, 'a') as f:
            writer = csv.writer(f)
            writer.writerows(page_data)
            page_data = []

    clean_csv_file(CSV_FILENAME)

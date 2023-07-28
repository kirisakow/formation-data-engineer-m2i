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


import asyncio
import aiohttp
from bs4 import BeautifulSoup
import csv
import re
from tqdm.asyncio import tqdm_asyncio
from time import time


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


async def async_scrape_page(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def async_parse_html_content(html_content: str):
    EMPTY_DATA_PLACEHOLDER = 'Introuvable'
    page_data = []
    soup = BeautifulSoup(html_content, 'html.parser')
    for info_avocat in soup.find_all('div', class_='annuaire-single'):
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
    return page_data


async def async_save_to_csv(csv_filename: str, page_data: list):
    with open(csv_filename, 'a', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerows(page_data)


async def async_main():
    """Main coroutine"""
    URL_BASE = 'https://www.barreaudenice.com'
    URL_PATH = '/annuaire/avocats/?fwp_paged={0}'
    HOW_MANY_PAGES = 50
    CSV_FILENAME = 'annuaire_avocats.csv'
    HEADER = ['nom_prenom', 'adresse', 'email', 'telephone']

    with open(CSV_FILENAME, 'w') as f_to_write:
        header_row = ','.join(HEADER)
        f_to_write.write(header_row + '\n')

    scraping_tasks = []
    for fwp_page in range(1, HOW_MANY_PAGES + 1):
        url_path = URL_PATH.format(fwp_page)
        scraping_tasks.append(async_scrape_page(URL_BASE + url_path))
    html_content_list = await tqdm_asyncio.gather(*scraping_tasks)

    parsing_tasks = []
    for html_content in html_content_list:
        parsing_tasks.append(async_parse_html_content(html_content))
    page_data_list = await tqdm_asyncio.gather(*parsing_tasks)

    save_to_csv_tasks = []
    for page_data in page_data_list:
        save_to_csv_tasks.append(async_save_to_csv(CSV_FILENAME, page_data))
    await tqdm_asyncio.gather(*save_to_csv_tasks)

    clean_csv_file(CSV_FILENAME)


if __name__ == '__main__':
    start_time = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
    print(f"Total execution time: {round(time() - start_time, 3)}s")

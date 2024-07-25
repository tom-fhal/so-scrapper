import requests
from bs4 import BeautifulSoup
import concurrent.futures
import re
import json
from scrapping import initiate_beautifulsoup, get_questions_beautifullsoup
import time 
def parse_questions(content):
    # Récupérer les questions ainsi que leurs titres et liens
    get_id = re.compile(r'question-summary-\d+')
    questions_df = []

    for question in content.find_all('div', id=get_id):
        # Récupérer le titre, le lien, le résumé, les tags, l'auteur et le temps de publication
        title = question.find('a', class_='s-link').text
        link = question.find('a', class_='s-link')['href']
        summary = question.find('div', class_='s-post-summary--content-excerpt').text
        tags = [tag.text for tag in question.find_all('a', class_='post-tag')]
        details_author = question.find('div', class_='s-user-card--link').text
        publication_time = question.find('span', class_='relativetime')['title']
        question_data = {
            'title': title,
            'link': link,
            'summary': summary,
            'tags': tags,
            'details_author': details_author,
            'publication_time': publication_time
        }
        questions_df.append(question_data)
    return questions_df

def scrape_page(page_num):
    url = f'https://stackoverflow.com/questions?tab=newest&page={page_num}'
    content = initiate_beautifulsoup(url)
    time.sleep(2)  # Pause de 2 secondes, vous pouvez ajuster cette valeur

    # Extraire les questions de la page
    return parse_questions(content)


def set_parralelisation():
    pages = int(input("Entrez le nombre de pages que vous souhaitez scrapper !: "))
    all_questions = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Soumettre une tâche pour chaque page
        future_to_page = {executor.submit(scrape_page, page_num): page_num for page_num in range(1, pages + 1)}
        
        # Parcourir les tâches au fur et à mesure qu'elles se terminent
        for future in concurrent.futures.as_completed(future_to_page):
            page_num = future_to_page[future]
            try:
                # Récupérer le résultat de la tâche (les questions scrappées)
                questions = future.result()
                all_questions.extend(questions)
                print(f"Page {page_num} scrappée avec succès.")
            except Exception as e:
                print(f"Erreur lors du scraping de la page {page_num}: {e}")

    with open('stackquestions.json', 'w') as f:
        json.dump(all_questions, f, indent=4)

    return all_questions

set_parralelisation()
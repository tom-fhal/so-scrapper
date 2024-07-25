from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By #Permet d'accéder aux différents élements de la page web
from webdriver_manager.chrome import ChromeDriverManager #Assure la gestion du webdriver de Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
import re
import json

def initiate_beautifulsoup(url):
    #Récupérer le contenu de la page
    pageContent = requests.get(url)
    #Parser le contenu de la page
    content = BeautifulSoup(pageContent.content, 'html.parser')
    return content


def get_questions_beautifullsoup(content, pages):
    #Récupérer les questions ainsi que leurs titres et liens
    get_id = re.compile(r'question-summary-\d+')
    questions_df = []
    scrapped_page = 0
    while scrapped_page != pages:
        for question in content.find_all('div', id=get_id):
                #append title of questiona 'a' tag  
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
                        'publication_time': publication_time}
                    
                questions_df.append(question_data)
        scrapped_page += 1
        print(scrapped_page)
        if scrapped_page != pages:
            new_url = f'https://stackoverflow.com/questions?tab=newest&page={scrapped_page + 1}'
            content = initiate_beautifulsoup(new_url)
    with open('stackquestions.json', 'w') as f:
        json.dump(questions_df, f, indent=4)
    return questions_df

def initiate_selenium(url):
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver

def get_questions_selenium(driver, pages):
    questions_df = []
    scrapped_page = 0

    while scrapped_page != pages:
        questions = driver.find_elements(By.XPATH, "//div[starts-with(@id, 'question-summary-')]")
        for question in questions:
            title = question.find_element(By.CLASS_NAME, 's-link').text
            link = question.find_element(By.CLASS_NAME, 's-link').get_attribute('href')
            summary = question.find_element(By.CLASS_NAME, 's-post-summary--content-excerpt').text
            tags = [tag.text for tag in question.find_elements(By.CLASS_NAME, 'post-tag')]
            details_author = question.find_element(By.CLASS_NAME, 's-user-card--link').text
            publication_time = question.find_element(By.CLASS_NAME, 'relativetime').get_attribute('title')
            question_data = {
                'title': title,
                'link': link,
                'summary': summary,
                'tags': tags,
                'details_author': details_author,
                'publication_time': publication_time}
            questions_df.append(question_data)
        scrapped_page += 1
        if scrapped_page != pages:
            new_url = f'https://stackoverflow.com/questions?tab=newest&page={scrapped_page + 1}'
            driver.get(new_url)

    with open('stackquestions.json', 'w') as f:
        json.dump(questions_df, f, indent=4)

    driver.quit()

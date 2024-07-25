import sys
import os
from scrapping import initiate_beautifulsoup, get_questions_beautifullsoup
from scrapping_optimization_para import set_parralelisation
from stackapi import initiate_api_request, get_questions_api, get_questions_selenium, initiate_selenium

def main():
    pages = int(input("Entrez le nombre de pages que vous souhaitez scrapper !: "))

    print("Voulez-vous scraper avec l'API ?")
    print("1. Oui")
    print("2. Non")
    choice = int(input("Entrez votre choix: "))
    
    if choice == 1: 
        get_questions_api(pages)
    else:
        print("Voulez-vous scraper avec BeautifulSoup ou avec Selenium ?")
        print("1. BeautifulSoup")
        print("2. Selenium")
        choice = int(input("Entrez votre choix: "))

        url = 'https://stackoverflow.com/questions?tab=newest&page=1'
        
        if choice == 1:
            content = initiate_beautifulsoup(url)
            get_questions_beautifullsoup(content, pages)
        else:
            driver = initiate_selenium(url)
            get_questions_selenium(driver, pages)

    print("Voulez-vous scraper en parallélisation ?")
    print("1. Oui")
    print("2. Non")
    choice = int(input("Entrez votre choix: "))

    if choice == 1:
        set_parralelisation()
    else:
        print("Merci !")
        sys.exit(0)

if __name__ == "__main__":
    main()
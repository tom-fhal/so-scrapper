
from unittest.mock import patch
from bs4 import BeautifulSoup

# Importer les fonctions à tester
from scrapping import initiate_bautifulsoup, get_questions_beautifullsoup



def test_initiate_bautifulsoup():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = '<html></html>'
        
        content = initiate_bautifulsoup("https://stackoverflow.com/questions")
        assert content is not None
        assert content.find('html').name == 'html'

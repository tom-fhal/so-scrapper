from bs4 import BeautifulSoup

# Importer les fonctions à tester
from scrapping import initiate_bautifulsoup, get_questions_beautifullsoup



def test_get_questions_beautifullsoup():
    html_content = '''
    <div id="question-summary-123">
        <a class="s-link" href="/questions/123">Test Question</a>
        <div class="s-post-summary--content-excerpt">This is a summary.</div>
        <a class="post-tag">python</a>
        <div class="s-user-card--link">Test Author</div>
        <span class="relativetime" title="2024-07-22 06:46:59Z"></span>
    </div>
    '''
    content = BeautifulSoup(html_content, 'html.parser')
    questions = get_questions_beautifullsoup(content, 1)
    assert len(questions) == 1
    assert questions[0]['title'] == 'Test Question'
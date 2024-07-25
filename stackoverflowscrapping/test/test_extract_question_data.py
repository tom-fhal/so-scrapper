from bs4 import BeautifulSoup

from scrapping import initiate_bautifulsoup, get_questions_beautifullsoup




def test_extract_question_data():
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
    question_data = questions[0]
    assert question_data['title'] == 'Test Question'
    assert question_data['link'] == '/questions/123'
    assert question_data['summary'] == 'This is a summary.'
    assert question_data['tags'] == ['python']
    assert question_data['details_author'] == 'Test Author'
    assert question_data['publication_time'] == '2024-07-22 06:46:59Z'


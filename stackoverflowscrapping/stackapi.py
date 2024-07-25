import requests
import json

def initiate_api_request(page):
    url = "https://api.stackexchange.com/2.3/questions"
    params = {
        'page': page,
        'pagesize': 20,
        'order': 'desc',
        'sort': 'creation',
        'site': 'stackoverflow',
        'filter': 'withbody'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_questions_api(pages):
    questions_df = []
    scrapped_page = 0
    while scrapped_page != pages:
        data = initiate_api_request(scrapped_page + 1)
        for item in data['items']:
            title = item['title']
            link = item['link']
            summary = item.get('body', 'No summary available')
            tags = item['tags']
            details_author = item['owner']['display_name']
            publication_time = item['creation_date']
            question_data = {
                'title': title,
                'link': link,
                'summary': summary,
                'tags': tags,
                'details_author': details_author,
                'publication_time': publication_time
            }
            questions_df.append(question_data)
        scrapped_page += 1
        print(f"Page {scrapped_page} scrappée.")
    with open('stackquestions.json', 'w') as f:
        json.dump(questions_df, f, indent=4)
    return questions_df


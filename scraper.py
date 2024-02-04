import requests
from bs4 import BeautifulSoup


def get_data():
    url = 'https://www.norgesquizforbund.no/arrangementer/finn-din-pubquiz/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rows = soup.find_all('tr')

    listings = []

    for row in rows[1:]:
        columns = row.find_all('td')
        if len(columns) >= 6:
            location = columns[1].text.strip()
            venue = columns[2].text.strip()
            date = columns[3].text.strip()
            time = columns[4].text.strip()
            category = columns[5].text.strip()

            if location.lower() == 'oslo':
                listings.append({
                    'location': location,
                    'venue': venue,
                    'date': date,
                    'time': time,
                    'category': category
                })

    return listings




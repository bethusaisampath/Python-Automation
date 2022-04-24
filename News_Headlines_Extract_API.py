import requests


def get_news(country, api_key='5fb6d842d9584673816829600be24355'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE: {article['title']}, 'DESCRIPTION:', {article['description']}")
    #results.insert(position,"\n")
  return results

#results=get_news(country='us')
get_news(country='us')
from GoogleNews import GoogleNews

def get_news(query, num=10, period='7d'):
    googlenews = GoogleNews(lang='en', region='US', period=period)

    googlenews.get_news(query)

    return googlenews.results()[:num]


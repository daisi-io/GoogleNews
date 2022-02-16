from GoogleNews import GoogleNews

def get_news(query, num=10):
    print('paramters: ', query, num)

    googlenews = GoogleNews(lang='en', region='US', period="1d")

    googlenews.get_news(query)
    
    print(f"total results: {len(googlenews.results())}")
    
    return googlenews.results()[:int(num)]



if __name__ == "__main__":
    res = get_news("apple")
    print(res)
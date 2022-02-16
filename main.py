from GoogleNews import GoogleNews

def get_news(query, num=10):
    print('paramters: ', query, num)

    googlenews = GoogleNews(lang='en', region='US', period="1d")

    googlenews.get_news(query)
    
    print(f"total results: {len(googlenews.results())}")
    
    results = googlenews.results()[:int(num)]
    for r in results:
        r["datetime"] = r["datetime"].strftime("%m/%d/%Y, %H")
        
    return results

if __name__ == "__main__":
    res = get_news("apple")
    print(res)
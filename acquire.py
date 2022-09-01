from requests import get
import pandas as pd
from bs4 import BeautifulSoup 
import os
import json




# scraping articles from one topic
def scrape_one_page(topic):
    base_url = 'https://inshorts.com/en/read/'
    
    response = get(base_url + topic)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = soup.find_all('span', itemprop='headline')
    
    summaries = soup.find_all('div', itemprop='articleBody')
    
    summary_list = []
    
    for i in range(len(titles)):
        
        temp_dict = {}
        
        temp_dict['title'] = titles[i].text
        
        temp_dict['content'] = summaries[i].text
        
        temp_dict['category'] = topic
        
        summary_list.append(temp_dict)
        
    return summary_list    



#Define a function that will scrape information about an array of topics
def get_news_articles():
    
    file = 'news_articles.json'
    
    if os.path.exists(file):
        
        with open(file) as f:
            
            return json.load(f)
    
    topic_list = ['business', 'sports', 'technology', 'entertainment']
    
    final_list = []
    
    for topic in topic_list:
        
        final_list.extend(scrape_one_page(topic))
        
    with open(file, 'w') as f:
        
        json.dump(final_list, f)
        
    return final_list 



from requests import get
import pandas as pd
from bs4 import BeautifulSoup 
import os



def get_blog_articles():
    '''Takes in a list of url, parses it using Beautiful Soup and returns a list of dictionaries
    of title as key and content as value'''
    lst = []

    url = ['https://codeup.com/codeups-data-science-career-accelerator-is-here/',
      'https://codeup.com/data-science-myths/',
      'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
      'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
       'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/',
       'https://codeup.com/introducing-salary-refund-guarantee/',
      'https://codeup.com/new-scholarship/']
    for elem in url:
        headers = {'User-Agent': 'Codeup Data Science'}
        response = get(elem, headers = headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        article = soup.find('div', class_ = 'jupiterx-post-content')
        article_text = article.text
        item = {
            'title': title,
            'content': article_text
        }
        lst.append(item)

        df = pd.DataFrame(lst)
    return df



# Create a helper function that requests and parses HTML returning a soup object.

def make_soup(url):
    '''
    This helper function takes in a url and requests and parses HTML
    returning a soup object.
    '''
    headers = {'User-Agent': 'Codeup Data Science'} 
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup



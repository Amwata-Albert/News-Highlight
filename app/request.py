#import the module that will help create a connection to the API URL and send a request
#import json modules that will format the JSON response to a dict
import urllib.request, json
from .models import Source,Top_Headlines,Everything



#get the api key
api_key = None

#get the source base url
base_url = None

#get the top headlines url
headlines_url = None

#get everything url
everything_url = None

def configure_request(app) :
  global api_key, base_url, headlines_url, everything_url
  api_key =app.config['NEWS_HIGHLIGHT_API_KEY']
  base_url = app.config["NEWS_HIGHLIGHT_API_BASE_URL"]
  headlines_url = app.config["TOP_HEADLINES_URL"]
  everything_url = app.config['EVERYTHING_URL']

  
def get_sources() :
  '''
  get the json response to our url request 
  '''
  get_sources_url = base_url.format(api_key)

  with urllib.request.urlopen(get_sources_url) as url :
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    source_results =  None 

    if get_sources_response['sources'] :
      source_results_list = get_sources_response['sources']
      source_results = process_source_results(source_results_list)

  return source_results 

def process_source_results(source_list) :
  '''
  process source result and transform them to a list of objects
  '''
  source_results = []
  for source_item in source_list :
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    category = source_item.get('category')
    language = source_item.get('language')
    country = source_item.get('country')

    source_object = Source(id, name, description, url, category, language, country)
    source_results.append(source_object)

  return source_results

def get_top_headlines(source) :
  get_top_headlines_url = headlines_url.format(source, api_key)

  with urllib.request.urlopen(get_top_headlines_url) as url :
    top_headlines_data = url.read()
    top_headlines_response = json.loads(top_headlines_data)

    top_headlines_results = None 

    if top_headlines_response['articles'] :
      top_headlines_results_list = top_headlines_response['articles']
      top_headlines_results = process_top_headlines_results(top_headlines_results_list)

  return(top_headlines_results)

def process_top_headlines_results(top_headlines_results_list) :
  '''
  process Top_headlines results and transform them to a list of objects
  '''
  top_headlines_results = []
  for top_headlines_item in top_headlines_results_list :

    author = top_headlines_item.get('author')
    title = top_headlines_item.get('title')
    description = top_headlines_item.get('description')
    url = top_headlines_item.get('url')
    urlToImage = top_headlines_item.get('urlToImage')
    publishedAt = top_headlines_item.get('publishedAt')
    content = top_headlines_item.get('content')

    top_headlines_object = Top_Headlines(author, title, description, url, urlToImage, publishedAt, content)
    top_headlines_results.append(top_headlines_object)

  return top_headlines_results

def get_everything() :
  '''
  get the json response to our url request 
  '''
  get_everything_url = everything_url.format(api_key)

  with urllib.request.urlopen(get_everything_url) as url :
    get_everything_data = url.read()
    get_everything_response = json.loads(get_everything_data)

    everything_results =  None 

    if get_everything_response['articles'] :
      everything_results_list = get_everything_response['articles']
      everything_results = process_everything_results(everything_results_list)

  return everything_results 

def process_everything_results(everything_results_list) :
  '''
  process everything result and transform them to a list of objects
  '''
  everything_results = []
  for everything_item in everything_results_list :

    author = everything_item.get('author')
    title = everything_item.get('title')
    description = everything_item.get('description')
    url = everything_item.get('url')
    urlToImage = everything_item.get('urlToImage')
    publishedAt = everything_item.get('publishedAt')
    content = everything_item.get('content')

    everything_object = Everything(author, title, description, url, urlToImage, publishedAt, content)
    everything_results.append(everything_object)

  return everything_results

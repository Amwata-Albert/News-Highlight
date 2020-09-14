import os

class Config :
  '''
  General configuration parent class 
  '''
  NEWS_HIGHLIGHT_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
  TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apikey={}' 
  EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&apiKey={}'
  NEWS_HIGHLIGHT_API_KEY = os.environ.get('NEWS_HIGHLIGHT_API_KEY')


class ProdConfig(Config) :
  '''
  Production configuration child class
  
  Args: 
    config : The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(Config) :
  '''
  Development configuration child class 
  '''
  DEBUG = True #enable debug mode in my app 

config_options = {
  'development' : DevConfig,
  'production' : ProdConfig
}
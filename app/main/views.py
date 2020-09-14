from flask import render_template,request,redirect,url_for
from . import main 
from ..request import get_sources,get_top_headlines,get_everything

#create a route decorator
@main.route('/')
#define the view function
def index() :
  '''
  View root page function that returns the index page and its data
  '''

  #get sources
  sources = get_sources()
  Everything = get_everything()
  print(sources)
  title = 'News Highlights '
  return render_template('index.html', title = title, sources = sources, Everything = Everything)

# def Everything(trending) :
#   '''
#   view everything from the querry trending in english
#   '''
#   
#   print(Everything)

#   return render_template('index.html',  )

@main.route('/source/<source>')
def Top_Headlines(source) :
  '''
  view Top_Headlines page function that returns the Top_Headlines from a source details page and its data 
  '''
  sources = get_sources()
  Top_headlines = get_top_headlines(source)
  print(Top_headlines)

  return render_template('Top_headlines.html', sources = sources, Top_headlines = Top_headlines, source = source)
  
  
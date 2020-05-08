import urllib.request,json
from .models import Quotes

# Getting the quote base url
base_url = None

def configure_request(app):
  global base_url

  base_url = app.config["QUOTES_API_BASE_URL"]


def get_quote():
  '''
  Function that gets the json response to our url request
  ''' 
  with urllib.request.urlopen(base_url) as url:
    get_quote_data = url.read()
    get_quote_response = json.loads(get_quote_data)

    quote_results = None

    if get_quote_response:
      author = get_quote_response.get('author')
      quote = get_quote_response.get('quote')
      quote_results = Quotes(author,quote)

  return quote_results



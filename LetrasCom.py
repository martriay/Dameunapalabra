from bs4 import BeautifulSoup
import urllib

class LetrasCom:
  baseurl = 'https://www.letras.com'

  @classmethod
  def get_words(cls):
    words = [cls.get_lyric_words(path) for path in cls.get_index()]
    return sum(words, []) # hacky

  @classmethod
  def get_lyric(cls, path):
    r = urllib.urlopen(cls.baseurl + path)
    soup = BeautifulSoup(r)

    lyric = letters_only(replace_tildes(soup.find('article').getText()))

    return lyric.lower().split()

  @classmethod
  def get_index(cls):
    r = urllib.urlopen(cls.baseurl + '/luis-alberto-spinetta')
    soup = BeautifulSoup(r)

    for ul in soup.find_all('ul', {'class': 'cnt-list'}):
      return [a['href'] for a in ul.find_all('a')]


def letters_only(s):
  import re
  return re.sub("[^a-zA-Z]", " ", s)

def replace_tildes(s):
  import unicodedata
  return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

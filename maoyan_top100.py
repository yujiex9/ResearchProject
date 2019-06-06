import re, requests, time
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


# Defaults
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}


def get_urls():
  urls = ['https://maoyan.com/board/4']
  for cnt in range(10, 100, 10):
    urls.append('https://maoyan.com/board/4?offset={}'.format(str(cnt)))

  return urls


def get_response(url=''):
  try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      return response.text
    return None
  except RequestException:
    return None


def get_movie_info(bs=BeautifulSoup('', 'html.parser')):
  index_patt = re.compile('board-index board-index-[0-9]+')

  board = bs.find_all('dd')
  for _item in board:
    # _index = _item.find('i', class_=index_patt).text
    name = _item.find('p', class_='name').text.strip()
    star = _item.find('p', class_='star').text.strip()
    releasetime = _item.find('p', class_='releasetime').text.strip()
    score_num = _item.find('p', class_='score')
    score = '{}{}'.format(score_num.find('i', class_='integer').text.strip(), score_num.find('i', class_='fraction').text.strip())
    print(name, star, releasetime, score)


# Main
urls = get_urls()
for url in urls:
  response_text = get_response(url)
  if response_text:
    bs = BeautifulSoup(response_text, 'html.parser')
    get_movie_info(bs)
  time.sleep(1)

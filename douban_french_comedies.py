import codecs, csv, json, os, requests, time
from urllib.parse import quote


# Defaults
filename = 'french_comedies.csv'
if os.path.exists(filename):
  os.remove(filename)

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

kw = "电影,喜剧"
tags, genres = [quote(_kw) for _kw in kw.split(',')]
score_range = "6,10"
countries = quote('法国')

movies_info = []
flds = ['title', 'rate', 'directors', 'casts']


def get_movies_data(url=""):
  try:
    r = requests.get(url, headers)
    data = json.loads(r.text)
    if "data" in data.keys():
      return data['data']
    else:
      return None
  except:
    return None


def save_movies_info(movies_info={}):
  with open(filename, 'w', encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=flds)
    writer.writeheader()
    for movie_info in movies_info:
      casts = ",".join(movie_info.get('casts'))
      directors = ",".join(movie_info.get('directors'))
      rate = movie_info.get('rate')
      title = movie_info.get('title')
      writer.writerow(
        {
          'title': title, 'rate': rate, 'casts': casts, 'directors': directors
        }
      )


# Main
offset = 0
while True:
  url = "https://movie.douban.com/j/new_search_subjects?sort=S&range={}&tags={}&playable=1&start={}&genres={}&countries={}".format(
    score_range, tags, str(offset), genres, countries)
  data = get_movies_data(url)
  if data:
    for element in data:
      movies_info.append(element)
  else:
    break
  offset += 20
  time.sleep(5)

if movies_info:
  save_movies_info(movies_info)

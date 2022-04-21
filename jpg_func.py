import requests
import imdb
def search_and_down(name):
    CONFIG_PATTERN = f'http://api.themoviedb.org/3/configuration?api_key=9324d7496f33ca322c729223df7a8da4'
    KEY = '9324d7496f33ca322c729223df7a8da4'

    url = CONFIG_PATTERN.format(key=KEY)
    r = requests.get(url)
    config = r.json()
    base_url = config['images']['base_url']
    """
         'sizes' should be sorted in ascending order, so
         max_size = sizes[-1]
        should get the largest size as well.        
    """
    max_size = 'w500'
    # creating instance of IMDb
    ia = imdb.IMDb()
    # searching the name
    search = ia.search_movie(name)
    result = []
    movieName = []
    # loop for printing the name and id
    for i in range(len(search)):
        # getting the id
        id = search[i].movieID
        result.append(id)
        movieName.append(search[i]['title'])
    movieid = "tt" + result[0]
    print("1",movieName[0],":", "Movieid:", result[0])
    #print("2",movieid)
    IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
    r = requests.get(IMG_PATTERN.format(key=KEY, imdbid=movieid))
    api_response = r.json()
    posters = api_response['posters']
    poster_urls = []
    for poster in posters:
        rel_path = poster['file_path']
        url = "{0}{1}{2}".format(base_url, max_size, rel_path)
        poster_urls.append(url)
        wanted_poster = poster_urls[0]
    return wanted_poster
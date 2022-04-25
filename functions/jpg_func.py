import shutil
import requests
import imdb


def search_and_down(name): # difining a func that will take the name of the enterd movie and give is jpg link
    CONFIG_PATTERN = f'http://api.themoviedb.org/3/configuration?api_key=9324d7496f33ca322c729223df7a8da4' #api configur link
    KEY = '9324d7496f33ca322c729223df7a8da4' # api key

    url = CONFIG_PATTERN.format(key=KEY)
    r = requests.get(url)
    config = r.json()
    base_url = config['images']['base_url'] #finding vars from the json file
    """
        'sizes' should be sorted in ascending order, so
        max_size = sizes[-1]
        should get the largest size as well.        
    """
    max_size = 'w300'
    # creating instance of IMDb
    ia = imdb.IMDb() # starting the imdb api
    # searching the name
    search = ia.search_movie(name)  # searching for movies by the name from the app.py
    result = []
    movieName = []
    # loop for printing the name and id
    for i in range(len(search)): #from all of the movies the api found we taking one
        # getting the id
        id = search[i].movieID
        result.append(id)
        movieName.append(search[i]['title']) #adding movie names to the list
        movieid = "tt" + result[0] #combining words to create the api movie id for later
        print("1",movieName[0],":", "Movieid:", result[0]) #just for check and for flask console reaction
        #print("2",movieid)
        IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
        r = requests.get(IMG_PATTERN.format(key=KEY, imdbid=movieid)) #formatting the api key and movieid form search im tmdb
        api_response = r.json()
        posters = api_response['posters'] #locating the poster jpg name in the api_response json file
        poster_urls = [] #making a list that will contain the poster jpg
        for poster in posters: #listing the movie jpg links
            rel_path = poster['file_path']
            url = "{0}{1}{2}".format(base_url, max_size, rel_path)
            poster_urls.append(url)
            wanted_poster = poster_urls[0]
            #for now taking the first movie link future challange: give the user an chois from many options.
            return wanted_poster
        def none():
            download_url = wanted_poster
            r = requests.get(download_url)



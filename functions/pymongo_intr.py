import shutil
import requests
import gridfs
import pymongo
def down_req(name, url):
    content_temp_path="/app/temp_content/"
    download_url = url
    filetype = download_url.split("/")[-1]
    filename = 'poster_{0}.{1}'.format(name, filetype)
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(download_url, stream=True)
    # Check if the image was retrieved successfully
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    #Open a local file with wb ( write binary ) permission.
    with open(content_temp_path + filename, 'wb') as f:
        mongoupload(name, filetype)
        return shutil.copyfileobj(r.raw, f)




def mongoupload(name, type):
    # CONNECTION_STRING = "mongodb+srv://basbusa:16456145@cluster0.jvols.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient("mongodb://db_host:27017")
    db = client.get_database('Moviesproject')
    fs = gridfs.GridFS(db)
    file = '/app/temp_content/poster_{0}.{1}'.format(name, type)
    with open(file, 'rb') as w:
        contents = w.read()

    fs.put(contents, filename=name)
import requests
import shutil
from random import randrange
import urllib.request
import webbrowser
from PIL import Image
response = requests.get('https://randomfox.ca/floof')
fox=response.json() #saving a variable to the json object
image = fox['image'] #extracting the link
randNum = randrange(1000)  #random file name to avoid errors
webbrowser.open_new_tab(image)  #opens the url on standard web browser
res = requests.get(image, stream = True)
fileName = str(randNum) + '.jpg'  #correct file extension

if res.status_code == 200:   #if the url is working
    with open(fileName,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print(f'Image sucessfully Downloaded: {fileName})')
img = Image.open(fileName) #opens the picture on your computer
img.show()

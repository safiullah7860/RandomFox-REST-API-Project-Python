# download-random-fox-image
Before running the Python program, make sure to install Requests by typing the following in the terminal: \
\
`python -m pip install requests`\
\
In this program, I used RandomFox REST API to download and view random images of foxes and open that image's URL as well.\
I first got the JSON data by using RandomFox REST API. \
I then extracted the link from the JSON object and used UrlLib to automatically open the link. I then used the shutil library to download and later open the picture on the user's machine.

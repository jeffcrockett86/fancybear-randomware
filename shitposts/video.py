import requests 

open('youtube.html', 'w').write(requests.get('https://www.youtube.com/watch?v=IxBQ8Er8DYc').text)
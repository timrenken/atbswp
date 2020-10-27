#! python
# imgurDownloader.py - Searches for a term and downloads the resulting images

import requests, os, bs4

url = "https://imgur.com/search?q="
term = input("Search term: ")

os.makedirs(term, exist_ok=True)

res = requests.get(url+term)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

images = soup.find_all('img')

for url in soup.find_all('img'):
    imgur_url = f"https:{url.get('src')}"
    print(f"Downloading image {imgur_url}...")
    res = requests.get(imgur_url)
    res.raise_for_status()
    
    imgur_file = open(os.path.join(term, os.path.basename(imgur_url)),'wb')
    
    for chunk in res.iter_content(100000):
        imgur_file.write(chunk)
        
    imgur_file.close()

print('Done')
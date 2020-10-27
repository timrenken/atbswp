#! python3
# downloadXkcd.py = Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com/2053'            # starting url
os.makedirs('xkcd', exist_ok=True)  # stores comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print(f'Downloading page {url}')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        for elem in comicElem:
            if elem.get('src').split('/')[2].split('.')[0] == "imgs":
                comicUrl = f"https:{elem.get('src')}"   

        # Download the image.
        print(f'Downloading image {comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = f"https://xkcd.com{prevLink.get('href')}"

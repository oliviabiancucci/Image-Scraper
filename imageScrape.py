import requests
from bs4 import BeautifulSoup

import urllib.request
from urllib.parse import urljoin

print("Please enter a URL: ")
url = input() # take in a url from console

response = requests.get(url) # sends a get request to the url passed to get its contents

soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img") # find all of the images using the img tag

for i, img in enumerate(images): # download the images with unique names
    img_url = img.get("src")
    if img_url:
        img_url = urljoin(url, img_url)
        img_name = f"image{i}.jpg"
        urllib.request.urlretrieve(img_url, img_name)
        print(f"Downloaded image {img_name}")

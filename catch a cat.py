import urllib.request

response = urllib.request.urlopen("http://placekitten.com/200/300")
cat_img = response.read()

with open("cat.jpg", "wb") as f:
    f.write(cat_img)

import requests, hashlib
from bs4 import BeautifulSoup

url = 'http://206.189.23.108:31239'

sess = requests.session()
#extract the string
response = sess.get(url)
soup = BeautifulSoup(response.text, features="lxml")
string = soup.h3.string
#encrypt the string
hashed = hashlib.md5(string.encode()).hexdigest()
hash = {"hash" : hashed}
#post the hash and print the flag
post = sess.post(url, data=hash)
soup = BeautifulSoup(post.text, features="lxml")
print(soup.p.string)

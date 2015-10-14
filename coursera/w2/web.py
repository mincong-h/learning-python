# w2
"""
spyder
"""
import urllib
r = urllib.urlopen('https://mincong-h.github.io')
html = r.read()
print html

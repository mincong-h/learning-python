example = list('hello') # ['h', 'e', 'l', 'l', 'o']
example[2:] = list('wow') # ['h', 'e', 'w', 'o', 'w']
example[2:2] = list('llo') # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'w']
example[1:5] = [] # = delete # ['h', 'o', 'w', 'o', 'w']

# week 2
"""
file operations
2015.10.14
"""
# write
f = open(r'/Users/minconghuang/Desktop/w2.txt', 'w')
f.write("Hello world")
f.close()
# read
f = open(r'/Users/minconghuang/Desktop/w2.txt', 'r')
print f.read(5)
print f.read()
f.close()
# add
s = "ESIGELEC"
f = open(r'/Users/minconghuang/Desktop/w2.txt', 'a+')
f.writelines('\n')
f.writelines(s)
f.seek(0,0) # reset pointer to 0
print f.readlines()
f.close()

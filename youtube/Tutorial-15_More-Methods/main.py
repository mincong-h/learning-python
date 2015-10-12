say = ['hey', 'now', 'brown', 'cow']
say.index('brown') # 2
say.insert(2, 'hoss') # ['hey', 'now', 'hoss', 'brown', 'cow']

# .pop() & .remove()
say.pop(1) # 'now'
say # ['hey', 'hoss', 'brown', 'cow']
say.remove('brown') # NULL
say # ['hey', 'hoss', 'cow']

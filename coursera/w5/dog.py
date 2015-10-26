class Dog(object):
    counter = 0
    def __init__(self, name):
        self.name = name
        Dog.counter += 1
    def greet(self):
        print 'Hi, I am %s, my number is %d' % (self.name, Dog.counter)

if __name__ == '__main__':
    paul = Dog('Paul')
    paul.greet()
    sara = Dog('Sara')
    sara.greet()

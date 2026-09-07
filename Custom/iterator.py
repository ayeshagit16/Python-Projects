'''Writing custom iterator using __next__ and __iter__ function'''

class Countdown:
    '''An iterator that counts down from a start number to 1'''

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # An iterator must return itself when __iter__ is called
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        countdown_value = self.current
        self.current -= 1
        return countdown_value


timer = Countdown(4)
# The raised exception "StopIteration" is caught automatically by constructs such as for, list comprehensions, and tuple().
for num in timer:
    print(num)

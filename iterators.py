liste = [1,2,3,4,5]
iterator = iter(liste)
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
    
    
class MyNumbers:
    def __init__(self, start, stop) -> None:
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10, 20)

myiter = iter(list)
while True:
    try: 
        element = next(myiter)
        print(element)
    except StopIteration:
        break
    

# for x in list:
#     print(x)
    

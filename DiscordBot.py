import random

def randomDecorator(func):
    def wrapper():
        r = random.randint(0, 1)
        if r == 0:
            return "Functio n not executed"

        else:
            return func()
            
        
    return wrapper


        
    



def hello():
    return "Hello the func has been executed"

hello = randomDecorator(hello)
print(type(hello))

# for i in range(10):
#     print(hello())
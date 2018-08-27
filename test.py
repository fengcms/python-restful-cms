import json
import pickle
import timeit

a = {'i': 'love u', 'you': 'love me too', 'time': 123456, 'text': 'i want test this code'}

def jsonTest():
    b = json.dumps(a)
    c = json.loads(b)
    return c

def pickleTest():
    b = pickle.dumps(a)
    c = pickle.loads(b)
    return c

#t = timeit.timeit(stmt=jsonTest,number=1000000)
t = timeit.timeit(stmt=pickleTest,number=1000000)
print(t)

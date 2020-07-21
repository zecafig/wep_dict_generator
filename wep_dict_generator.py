from itertools import product

sequence = "0123456789abcdef"

def generate():
    for i in product(sequence, repeat=2):
        yield i

k = generate()

for p in k:
    listToStr = ''.join(map(str, p)) 
    print(listToStr) 
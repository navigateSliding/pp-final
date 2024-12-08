import os

with open('products.txt', 'r') as f:
    data1 = []
    data = f.read().splitlines()
    for line in data:
        data1.append(line.split(','))
    print(data1)

if os.path.exists('products.txt'):
    data = []
    with open('products.txt', 'r') as file:
        for line in file.readlines():
            data.append(line.strip().split(','))
    print(data)
# Your code here

# with open("applications\histo\robin.txt") as f:
#     words = f.read()

#     print(words)

# Read in all the words in one go
with open("applications\histo\dobin.txt") as f:
    words1 = f.read()
    words = words1.split()
   
cache = {}

for word in words:
    if word not in cache:
        cache[word] = '#'
    else:
        cache[word] += '#'

items = list(cache.items())

items.sort(key=lambda e:e[1], reverse=True)


for key, value in items:
    print(f'{key}            {value}')






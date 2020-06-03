import re

def word_count(s):
    # Your code here
    
    bbb = re.sub('\ |\?|\,|\"|\.|\!|\/|\;|\:', ' ', s)
    counts = dict()
    # fff = s.replace(".","")
    
    words = bbb.split()
    
    for word in words:
        ggg = word.lower()
        if ggg in counts:
            counts[ggg] += 1
        else:
            counts[ggg] = 1

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
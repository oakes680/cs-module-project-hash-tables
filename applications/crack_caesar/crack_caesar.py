# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
# # Your code here


def crack_ceaser(file):
    caeser_letters = {}
    letter_frequency = {}

    letter_frequency["E"] = 11.53
    letter_frequency["T"] = 9.75
    letter_frequency["A"] = 8.46
    letter_frequency["O"] = 8.08
    letter_frequency["H"] = 7.71
    letter_frequency["N"] = 6.73
    letter_frequency["R"] = 6.29
    letter_frequency["I"] = 5.84
    letter_frequency["S"] = 5.56
    letter_frequency["D"] = 4.74
    letter_frequency["L"] = 3.92
    letter_frequency["W"] = 3.08
    letter_frequency["U"] = 2.59
    letter_frequency["G"] = 2.48
    letter_frequency["F"] = 2.42
    letter_frequency["B"] = 2.19
    letter_frequency["M"] = 2.18
    letter_frequency["Y"] = 2.02
    letter_frequency["C"] = 1.58
    letter_frequency["P"] = 1.08
    letter_frequency["K"] = 0.84
    letter_frequency["V"] = 0.59
    letter_frequency["Q"] = 0.17
    letter_frequency["J"] = 0.07
    letter_frequency["X"] = 0.07
    letter_frequency["Z"] = 0.03

    with open(file) as f:
        data = f.read()
    total_no_of_letters = 0


    for c in data:
        if c.isalpha() and c in caeser_letters:
            caeser_letters[c] += 1
            total_no_of_letters += 1
        elif c.isalpha():
            caeser_letters[c] = 1
            total_no_of_letters += 1


    for letter in caeser_letters:
        caeser_letters[letter] = round(
            ((caeser_letters[letter]/total_no_of_letters)*100), 2)

    encrypted_letter_freq = list(caeser_letters.items())
    provided_letter_freq = list(letter_frequency.items())

    encrypted_letter_freq.sort(key=lambda e: e[1], reverse=True)
    provided_letter_freq.sort(key=lambda e: e[1], reverse=True)

    # print("known", provided_letter_freq)
    # print("caesar", encrypted_letter_freq)


   
    encrypt_array = []
    provided_array = []
    for i, (x, z) in enumerate(encrypted_letter_freq):
        encrypt_array.append(x)
   
    for i, (x, z) in enumerate(provided_letter_freq):
        provided_array.append(x)


    dict_map = dict(zip(encrypt_array, provided_array))
 
    content = ''

    for i in range(len(data)):
        if data[i].isalpha() and data[i] in dict_map:
            # data[i] = dict_map[data[i]]
            content += dict_map[data[i]]
        else:
            content += data[i]
    print(content)


            
  

print(crack_ceaser('applications\crack_caesar\ciphertext.txt'))

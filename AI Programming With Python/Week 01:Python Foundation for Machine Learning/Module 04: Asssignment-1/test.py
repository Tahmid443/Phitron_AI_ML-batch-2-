def most_frequent_word(filename):
    file = open(filename, "r")
    text = file.read()
    

    text = text.lower()

    freq = {}
    word = ""

    for ch in text:
        if ch.isalnum(): 
            word += ch
        else:
            if word != "":
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
                word = ""

    if word != "":
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    max_word = ""
    max_count = 0

    for w in freq:
        if freq[w] > max_count:
            max_count = freq[w]
            max_word = w

    return max_word

print(most_frequent_word("data.txt"))

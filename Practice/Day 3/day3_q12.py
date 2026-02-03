def longestWord  (words):
    max=len(words[0])
    lng=words[0]
    for word in words:
        if len(word)>max:
            max = len(word)
            lng = word

    print("Given Words: ",words)
    print("Longest word is: ",lng, " with ", max, " words")
    

longestWord(["Suraj", "Gautam", "Prakash", "haha", "MCa"])
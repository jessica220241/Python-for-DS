words=["model", "data", "python", "data", "model", "analysis", "data"]
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
repeated_words=[]
for word in frequency:
    if frequency[word]>1:
        repeated_words.append(word)
print("Frequency: ", frequency)
print("Repeated word", repeated_words)

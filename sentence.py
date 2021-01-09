sentences = []
valid = True

while valid:
    sentence = input("Sentence: ").split(" ")
    sentences.append(sentence)

    for c in sentences:
        for t in c:
            if t == "":
                sentences.pop()
                print("Shortest sentence is", " ".join(min(sentences, key=len)))
                valid = False



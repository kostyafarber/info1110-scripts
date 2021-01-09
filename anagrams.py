line = [x for x in input("Enter line: ").lower()]
anagram = [x for x in input("Enter anagram: ").lower()]

for c in "':,—...!-().?'';' ' ":
    while c in anagram:
        anagram.remove(c)

    while c in line:
        line.remove(c)

if len(line) != len(anagram):
    print("\n" + "Not an anagram.")

else:

    if set(line) == set(anagram):
        print("\n" + "Anagram!")

    else:
        print("\n" + "Not an anagram.")
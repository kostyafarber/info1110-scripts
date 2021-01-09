import sys

strand = [x for x in input("Enter strand: ")]

new_strand = []

for c in strand:
    if c == "A":
        new_strand.append("T")

    elif c == "T":
        new_strand.append("A")

    elif c == "G":
        new_strand.append("C")

    elif c == "C":
        new_strand.append("G")

    elif c == "a":
        new_strand.append("t")

    elif c == "t":
        new_strand.append("a")

    elif c == "g":
        new_strand.append("c")

    elif c == "c":
        new_strand.append("g")

    else:
        new_strand.append("x")

if len(new_strand) == 0:
    print()
    print("No strand provided.")
    sys.exit()

print()
print("Complementary strand is", "".join(new_strand))
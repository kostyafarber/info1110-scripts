ipv6 = [x for x in input("Please enter an IP address: ").split(":")]

hex_dig = "0123456789ABCDEFabcdef:"

Valid = True

for i in range(len(ipv6)):
    for c in ipv6[i]:
        if c not in hex_dig:
            Valid = False

        elif len(ipv6[i]) > 4:
            Valid = False

        elif len(ipv6) != 8:
            Valid = False

if Valid:
    print("It is a valid IPv6 address.")

else:
    print("It is not a valid IPv6 address.")


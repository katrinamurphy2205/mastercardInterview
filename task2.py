# Reverse a String iteratively and recursively
# we need to reverse a string. set up empty string and feed the letters back in backwards

def iterative_reverse(string1):
    x = len(string1)

    a = ''
    i = x-1
    while i >= 0:
        a += string1[i]
        i -= 1
    print(a)

# 
def recursive_reverse(string1, i=0):
    x = len(string1)

    if i == x//2:
        return

    string1[i], string1[x-i-1] = string1[x-i-1], string1[i]

    recursive_reverse(string1, x+1)
    print(string1)


if __name__ == "__main__":
    string1 = "katrinamurphy"
    iterative_reverse(string1)
    recursive_reverse(string1)


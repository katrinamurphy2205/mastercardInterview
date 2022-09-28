# Find most frequent integer in an array?
# for integers in array we need to count frequency of each integer, only store the greatest one

def most_frequent(array):
    counter = 0
    num = array[0]

    for x in array:
        frequency = array.count(x)
        if (frequency > counter):
            counter = frequency
            num = x

    return num


array = [1, 3, 3, 2, 1, 3]
print(most_frequent(array))

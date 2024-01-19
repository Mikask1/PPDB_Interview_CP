huruf = 'aaabcdefghijklmnopqrstuvwxyz'

while True:
    counter = int(input())
    pointer = 0

    for i in range(counter):
        for j in range(i + 1):
            if (j == counter-1) and counter != 1:
                print('+', end=' ')
            else:
                print(huruf[pointer], end=' ')

            pointer = int((pointer + 1) % len(huruf))
        print("")
    print("")

input = list(open("input.txt", "r"))
input = list(map(int, input[0].split()))

def func(a, b):
    output = open("output.txt", "w")
    output.write(str(a + b))
    output.close()
    return 0

func(input[0], input[1])

a = int(input())

b = input().split()

result = list(map(int, b))

counter = 0

for i, j in enumerate(result):

    if(i > 0 and result[i] > result[i - 1] and i < a):

        counter += 1



print(counter)
i = 1

while i < 10:
    j = 1
    while j <= i:
        if j != i:
            print(f"{j}*{i}={i * j}\t", end='')
        else:
            print(f"{j}*{i}={i * j}\t")
        j += 1
    i += 1

# 在输出台输出*，并且每一行的*数量+1
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("row * col = ", row * col, end="")
        col += 1
    print("")
    row += 1

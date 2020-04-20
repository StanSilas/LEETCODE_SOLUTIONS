n = int(raw_input("enter n for fib:"))
a = 0
b = 1
if (n == 1):
    return 0
if (n == 2):
    return 1

next_num = 0
for i in range(n-2):
    next_num = a + b
    a = b
    b = next_num
return next_num

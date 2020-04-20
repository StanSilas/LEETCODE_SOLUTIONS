def fizzbuzz(n):
    # print fizzbuzz until n
    # eg. 1, 2, fizz, 4, buzz, ...
    
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 != 0:
            print "Fizz, ",
        elif num % 3 != 0 and num % 5 == 0:
            print "Buzz, ",
        elif num % 3 == 0 and num % 5 == 0:
            print "FizzBuzz, ",
        else:
            print str(num) +", ",

def fbz(n):
    for num in range(1, n + 1):
        if num % 15 == 0:
            print "FizzBuzz, ",
        elif num %3 == 0:
            print "Fizz, ",
        elif num % 5 == 0:
            print "Buzz, ",
        else:
            print str(num) + ", ",

def palindrome(my_string):
    x = ""
    for i in my_string:
        x = i + x # form the string in reverse
       
    # for i in range(len(my_string)):
    #     x = x + my_string[-i]

    if x == my_string:
        print("palindrome")
        print(x)
    else:
        print("not palindrome")
        print(x)
    

palindrome("Hello, World")
# palindrome("AbbA")

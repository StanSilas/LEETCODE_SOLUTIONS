def palindrome(my_string):
    x = ""
    for i in range(len(my_string)+1):
        x = x + my_string[-i]

    if x == my_string:
        print("palindrome")
    else:
        print("not palindrome")
    

palindrome("Hello, World")

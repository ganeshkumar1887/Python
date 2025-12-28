def check_pass(num):
    password = "password123"
    if(num==password):
        print("correct password")
    else:
        print("Access Denied")


n = input("Please! Enter password ::")
check_pass(n)


def get_name():
    user_name = input("Enter your name: ")
    return user_name

def print_Msg(user_name):
    print("Hello",user_name)

def main():
    user_name = get_name()
    print_Msg(user_name)

main()




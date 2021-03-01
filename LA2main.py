import book_keeper as bk


def main():
    """
    The main function of the code, can also be seen as general outline of the program
    """
    control = bk.Controller()
    control.read_input("input.txt")
    response = ""
    quit_flag = False
    print('Before while-loop')
    while quit_flag is False:
        control.show_menu()
        response = input("Please choose an option: ")
        print()
        if response == "1":
            control.display_collection()
        elif response == "2":
            user_call_number = input('Enter a call number: ')
            user_call_number = user_call_number.replace(' ', '')
            print()
            control.check_out_materials(user_call_number)
        elif response == "3":
            quit_flag = True
        else:
            print("Invalid response!")

    print("Good bye!")


main()

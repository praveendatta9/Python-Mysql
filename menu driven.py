from main import DBHelper


def imp():
    while True:
        print('********WELCOME********')
        print()
        print('PRESS 1 to insert new user')
        print('PRESS 2 to display all user')
        print('PRESS 3 to delete user')
        print('PRESS 4 to update user')
        print('PRESS 5 to exit program')
        print()

        helper = DBHelper()
        try:

            choice = int(input())
            if choice == 1:
                helper.insert_user()
            elif choice == 2:
                helper.fetch_all()
            elif choice == 3:
                helper.delete_user()
            elif choice == 4:
                helper.update_user()
            elif choice == 5:
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")


if __name__ == '__main__':
    imp()


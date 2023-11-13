
def main():
    user = {}
    while True:
        user_input = input('>>>')
        if user_input in ['good bye', 'close', 'exit']:
            print('Good bye!')
            break
        elif user_input == 'hello':
            result = hello()
            print(result)
        elif user_input == 'add':
            result = add(user)
            print(result)
        elif user_input == 'change':
            change(user)
        elif user_input == 'phone':
            phone(user)
        elif user_input == 'show all':
            show_all(user)





def error_handle(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result 
        except KeyError:
            return 'No user found'
        except ValueError:
            return 'No user found'
        except IndexError:
            return 'Enter user name'
    return inner

@error_handle
def add(user):

    while True:
        name = input('Enter user name ( or enter "esc" to end operation ):')
        if name.lower() == 'esc':
            break
        phone = input('Enter phone number:')
        user[name] = phone
    return user

@error_handle
def change(user):
    name_to_update = input('Enter the name for which you want to change the phone number:')
    if name_to_update in user:
        new_phone = input('The number you want to change')
        user[name_to_update] = new_phone
        print('Phone number changed successfully')
    else:
        print("User not found")
    return user
@error_handle
def phone(user):
    show_number = input('Enter user name:')
    if show_number in user:
        phone_number = user[show_number]
        print(f"{show_number}'s phone number is {phone_number}")
    else:
        print('User not found')
    return user

@error_handle
def show_all(user):
    print(user)
def hello():
    return "How can I help you?"


if __name__ == "__main__":
    main()
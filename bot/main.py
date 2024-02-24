def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if not is_data_valid(args):
        return
    name, phone = args
    contacts[name] = phone
    print("Contact added.")

def change_username_phone(args, contacts):
    if not is_data_valid(args):
        return
    name, phone = args
    contacts[name] = phone
    print("Phone is updated for the user.")

def phone_for_username(args, contacts):
    (name, ) = args
    print(contacts[name])

def all(contacts):
    for name, phone in contacts.items():
        row = "{0:20}: {1:10}".format(name, phone)
        print(row)

def is_data_valid(args):
    if (len(args) < 2):
        print("You input wrong data, please try again.")
    return len(args) == 2

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, contacts)
        elif command == "change":
            change_username_phone(args, contacts)
        elif command == "phone":
            phone_for_username(args, contacts)
        elif command == "all":
            all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
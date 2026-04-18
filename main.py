
from api_phonebook import Phonebook, User

def main():
    
    p = Phonebook()

    def create():
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        phone = input("Enter phone: ")
        city = input("Enter city: ")

        user = User(name, surname, phone, city)
        p.create_entry(user)

    def update():
        phone_to_find = input("(4) - Enter the phone number to find: ")
        name = input("Enter new name: ")
        surname = input("Enter new surname: ")
        phone = input("Enter new phone: ")
        city = input("Enter new city: ")
        user = User(name, surname, phone, city)
        if not p.update_entry(user, phone_to_find):
            print("User not found.")

    commands = {
        '1': create,
        '2': lambda: p.delete_entry(input('(2) - Enter the phone number: ')),
        '3': lambda: p.read_entry(user_input=input('(3) - Enter the value: ')),
        '4': update
    }
    
    print('Welcome to CLI program "PhoneBook"\nYou can update/delete/read/create your entry.\nThere are commands how to use the CLI\n (1) - Create entry; (2) - Delete entry(by phone number); (3) - Read entry(by name/ surname/ phone number/ city); (4) - Update(by phone number)\nATTENTION! Exit from the program "EXIT"')
    
    while True:
        
        cmd = input("[Main]Enter the command: ").strip()
        
        if cmd.upper() == 'EXIT':
            break
        
        act = commands.get(cmd)
        if cmd in commands:
            act()
        else:
            print('Wrong command. Try again:')
        
        
    
if __name__ == '__main__':
        
       
    main()

                        

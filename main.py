
from api_phonebook import Phonebook, DataDecorators, User

def main():   
    p = Phonebook()

    commands = {
        '1': lambda: p.create(User(
            name=input('Enter name: '),
            surname=input('Enter surname: '),
            phone=input('Enter phone: '),
            city=input('Enter city: ')
        )),
        '2': lambda: p.delete(input('(2) - Enter the phone number: ')),
        '3': lambda: p.read(user_input=input('(3) - Enter the value: ')),
        '4': lambda: p.update(
            user=User(
                name=input('Enter name: '),
                surname=input('Enter surname: '),
                phone=input('Enter phone: '),
                city=input('Enter city: ')
            ),
            user_phone=input('(4) - Enter the phone number to update: ')
        )
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

                        

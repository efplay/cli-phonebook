import json
import os
from dataclasses import dataclass

@dataclass
class User:
    
    name: str
    surname: str
    phone: str
    city: str
    
    def transform_as_dict(self) -> dict:     
        
        return{
            "user": {                
                'name': self.name,
                "surname": self.surname,
                'phone': self.phone,
                'city': self.city,                
            }             
        }
    


class Data:
    
    def __init__(self):
        self.path_data = os.path.join(os.path.dirname(__file__), 'data_phonebook.json')

    def load_data(self) -> list:
        with open(self.path_data, 'r', encoding='utf-8') as f:
            return json.load(f)
    
   
    def save_data(self, data: list) -> None:
        with open(self.path_data, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
    def add_user_data(self, user):
        data = self.load_data()
        data.append(user)
        self.save_data(data)
        return user


class Phonebook(Data): 

           
    def create_entry(self, user: User) -> User:     
        user_data = user.transform_as_dict()        
        self.add_user_data(user_data)
        return user

            
    def update_entry(self, user: User, user_phone):
        data = self.load_data()

        for item in data:
            if item.get('user', {}).get('phone') == user_phone:
                item['user']['name'] = user.name
                item['user']['surname'] = user.surname
                item['user']['phone'] = user.phone
                item['user']['city'] = user.city

                self.save_data(data)
                return True

        return False        

                
    def delete_entry(self, user_phone):
        data = self.load_data()

        for i, item in enumerate(data):
            if item.get('user', {}).get('phone') == user_phone:
                del data[i]
                break
        else:
            return False

        self.save_data(data)
            
        return True


    def read_entry(self, user_input):
        data = self.load_data()

        fields = ['name', 'surname', 'city', 'phone']
        
        for item in data:
            user = item.get('user', {})
            
            for field in fields:
                if user.get(field) == user_input:
                    print (f"You find the {field}: {user.get(field)}")
                    return True
        return False
                    
            
    

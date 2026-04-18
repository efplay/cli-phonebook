import json
import os
from dataclasses import dataclass

path_data = os.path.join(os.path.dirname(__file__), 'data_phonebook.json')

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
    


class DataDecorators:
    @staticmethod 
    def load_data(func):
        def wrap(self, *args, **kwargs):
            with open(path_data, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return func(self, data, *args, **kwargs)
        return wrap
    
    @staticmethod 
    def save_data(func):
        def wrap(self, data, *args, **kwargs):
            result = func(self, data, *args, **kwargs)
            with open(path_data, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            return result
        return wrap
        
    def add_user_data(self, user):
        with open(path_data, 'r', encoding='utf-8') as f:
            data = json.load(f)
        data.append(user)
        with open(path_data, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return user


class Phonebook(DataDecorators): 
            
    def create(self, user: User) -> User:     
        user_data = user.transform_as_dict()        
        self.add_user_data(user_data)
        return user

    @DataDecorators.load_data
    @DataDecorators.save_data
    def update(self, data, user: User, user_phone):
        for item in data:
            if item.get('user', {}).get('phone') == user_phone:
                item['user']['name'] = user.name
                item['user']['surname'] = user.surname
                item['user']['phone'] = user.phone
                item['user']['city'] = user.city             
                return True
        return False        

    @DataDecorators.load_data
    @DataDecorators.save_data            
    def delete(self, data, user_phone):
        for i, item in enumerate(data):
            if item.get('user', {}).get('phone') == user_phone:
                del data[i]
                break
        else:
            return False           
        return True

    @DataDecorators.load_data
    def read(self, data, user_input):
        fields = ['name', 'surname', 'city', 'phone']       
        for item in data:
            user = item.get('user', {})         
            for field in fields:
                if user.get(field) == user_input:
                    print (f"You find the {field}: {user.get(field)}")
                    return True
        return False

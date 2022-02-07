
import json 

def save(file_name, data):
    try:
        with open(file_name,'wb') as file:
            json.dump(data, file)

    except Exception as e:
        print(e)

def load(file_name):
    try:
        with open(file_name,'rb') as file:
            data = json.load(file)
            return data
    
    except Exception as e:
        print(e)
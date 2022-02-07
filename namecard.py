from file_util import  load, save
import os


class NameCard:
    def __init__(self):
        self.book = []

    
        

    def load(self, file_path):
    
        if os.path.exists(file_path):  
            self.book = load(file_path)
        else:                          
            save(file_path, self.book)

    def save(self, file_path):
        save(file_path, self.book)








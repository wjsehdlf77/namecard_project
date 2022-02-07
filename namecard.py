
class NameCard:
    def __init__(self):
        self.book =[]

    
    def load(self, FILE_PATH):
        try:
            with open(FILE_PATH, 'rt', encoding='utf-8') as file:
                list = file.readlines()
                for line in list:
                    line = line.strip()
                    self.book.append(line)
                return self.book
        except Exception as e:
            print(e)










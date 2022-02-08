from namecard import NameCard



FILE_PATH = 'addressbook.txt'
NAME = 'addr.db'
def main():
    book = NameCard()
    book.load(FILE_PATH)

    #addressbook.txt를 순회하며 출력
    for ix in book.book:
        print(ix)

    #addr.db에 저장
    book.save(NAME)

main()






    


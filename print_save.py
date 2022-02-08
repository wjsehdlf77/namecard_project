from namecard import NameCard



FILE_PATH = 'addressbook.txt'
NAME = 'addr.db'
def main():
    book = NameCard()
    book.load(FILE_PATH)

    #addressbook.txt를 순회하며 출력
    for ix in book.book:
        list_book = ix.split(',')
        print('-' * 85)
        print(f'이름 : {list_book[0]}, 이메일 : {list_book[1]}, 휴대폰 : {list_book[2]}, 주소 : {list_book[3]}')
        print('-' * 85)

    #addr.db에 저장
    book.save(NAME)

main()






    


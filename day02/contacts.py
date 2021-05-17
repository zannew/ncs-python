# domain
class Contacts:

    name = ''
    phone = ''
    email = ''
    address = ''

    def __str__(self):
        return f'이름 : {self.name} \n' \
               f'연락처 : {self.phone} \n' \
               f'이메일 : {self.email} \n' \
               f'주소 : {self.address} \n'

class ContactsService:

    def print_menu(self):
        print("1. 연락처 입력\n2. 연락처 출력\n3. 연락처 삭제\n4. 종료")
        menu = input("메뉴 선택 : ")
        return int(menu)


    def set_contacts(self):
        obj = Contacts()
        obj.name = input("이름 : ")
        obj.phone = input("연락처 : ")
        obj.email = input("이메일 : ")
        obj.address = input("주소 : ")
        return obj


    def get_contacts(self, ls):
        for i in ls:
            print(i)


    def del_contacts(self, ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]


    @staticmethod
    def main():
        ls = []
        service = ContactsService()
        while 1:
            menu = service.print_menu()
            if menu == 1:
                t = service.set_contacts()
                ls.append(t)
            elif menu == 2:
                service.get_contacts(ls)
            elif menu == 3:
                name = input("삭제할 이름 : ")
                service.del_contacts(ls, name)
            elif menu == 4:
                break

if __name__=='__main__':
    ContactsService.main()
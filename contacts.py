print('contacts app')
my_contacts={}
while(True):
    print('1.Add\n 2.Delete\n 3.Search\n 4.Display\n 5.Update')
    print('enter your choice')
    choice=int(input())
    if choice==1:
        n = int(input("enter the no.of contacts you wana add"))
        for i in range(n):
            contact_name = input() 
            number = int(input())
            my_contacts[contact_name] = number
            print(my_contacts)
    elif choice==2:
        contact_name=input('enter the contact name')
        if contact_name not in my_contacts:
            print('your contact name is not in the list')
        else:
            my_contacts.pop(contact_name)
            print(my_contacts)
    elif choice==3:
        print('enter the contact name to search')
        contact_name=input()
        if contact_name in my_contacts:
            print(my_contacts[contact_name])
    elif choice==4:
        for contact_name,number in my_contacts.items():
            print(contact_name)
            print(number)
    elif choice==5:
        print('enter the contact name to update')
        contact_name=input()
        if contact_name in my_contacts:
            number=int(input('enter new contact number'))
            my_contacts[contact_name] = number
            print(my_contacts)

    else:
        break

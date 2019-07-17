print('contacts app')
print('1.Add\n 2.Delete\n 3.Search\n 4.Display\n 5.Update')
print('enter your choice')
choice=int(input())
my_contacts={'sai':532,'kru':456}
def add():
  n = int(input("enter the no.of contacts you wana add"))
  for i in range(n):
      contact_name = input() 
      number = int(input())
      my_contacts[contact_name] = number
  print(my_contacts)
def delete():
  print('enter the contact name')
  contact_name=input()
  if contact_name in my_contacts:
    my_contacts.pop(contact_name)
    print(my_contacts)
  else:
    print('your contact name is not in the list')
def search():
  print('enter the contact name to search')
  contact_name=input()
  if contact_name in my_contacts:
    print(my_contacts[contact_name])
def display():
  print(my_contacts)
def update():
  print('enter the contact name to update')
  contact_name=input()
  if contact_name in my_contacts:
    number=int(input('enter new contact number'))
    my_contacts[contact_name] = number
  print(my_contacts)
if choice==1:
 add()
elif choice==2:
  delete()
elif choice==3:
  search()
elif choice==4:
  display()
elif choice==5:
  update()
else:
  exit

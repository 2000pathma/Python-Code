class AddressBook:
    def __init__(self):
        self.contactName=""
        self.emailid=""

    def giveContactDetails(self):
        self.contactName = input("Enter person name ")
        self.emailid = input("Enter email id ")

    def display(self):
        print("Contact Name :", self.contactName)
        print("Email ID     :", self.emailid)
        print("\n")

contactList=[]
choice='y'
while(choice=='y'):
    print("1. Add New Contact \n 2. Display Contacts")
    response = int(input("Enter your choice"))

    if(response==1):
        contact = AddressBook()#object creation
        contact.giveContactDetails()#method calling
        contactList.append(contact)
    elif(response==2):
        for value in contactList:
            value.display()#method calling
    else:
        print("Please check your response")
    
    choice = input("Press 'y' to continue ")

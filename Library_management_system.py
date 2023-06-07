# Taking a dictonary to store all the book,user,rented item's 
library = {}

def add_book():
   bookname= input("Enter the bookname you want to add: ")
   library[bookname]= True
   #checking if book really added and has value True if not then try again
   if library.get(bookname) == True:
       print ("Book added successfully.")
   else:
       print("Try adding book again!!")
   
def add_username():
    username = input('Enter the username you want add: ')
    #Giving user a particular dictonary to store the rented book by this user
    library[username]= {}
    #Checking either user is added or not if user added and has value empty dictonary 
    if library.get(username)== {}:
        print("\nUser added successfully")
    else:
        print('\nTry again user not added')

def rent_book():
    username= input("\Enter your name : ")
    bookname = input ("\nEnter the book name you want to take: ")
    #matching if Book and user name present in the library or not(here using .keys because we used both bookname and user name as keys of diconary)
    if bookname in library.keys() and username in library.keys():
        #here deleting Book because Book goes on rent so should not be self present in library
        del library[bookname]
        #but it is actually in our library but on rent so we have to recorde who has taken so assiging the bookname inside the username dictonary
        library[username][bookname]= True
        print("\nBook rented successfully")
        
    #here showing if book isn't available or username not in library
    elif bookname in library.keys():
        print ("\nplease add the username first to take book on rent")

    elif username in library.keys():
        print("\nBook is not available")

    else:
        print('\nEntered the username and bookname is not available')



def delete_book():
    bookname = input ("\nEnter which book you want to delete: ")
    #checking book present in the library or not
    if bookname in library.keys():
        del library[bookname]
        if bookname not in library.keys():
            print("\nBook deleted successfully")
    else:
        print ("\nBook do not exist in the library")

def return_book():
    bookname = input("\nEnter the book name you want to return: ")
    username = input ('\nEnter the username by which book is taken: ')
    #checking user has present or not and does user has taken the Book
    if username in library.keys() and bookname in library[username].keys():
        #if yes user has taken the book againg adding book to library
        library[bookname]=True
        #deleting book from user dictonary
        del library[username][bookname]
    
    elif username not  in library.keys():
        print('\nUsername doesnot exist ') 
    elif bookname not in library[username].keys():
        print("\nBook is not on rent")
        
    if bookname in library.keys():
        print('\nBook return successfully')
    

print("\n\n\t\t\t\t##########################################################")
print ("\t\t\t\t\twelcome to our library management system:")
print("\t\t\t\t##########################################################")


def main():
    #running loop to allow user to choose their choice agaian
    while True:
        print ("\nchoose option for the following things:\n\n 1) Add book \n 2) Add username \n 3) Rent book \n 4) Return book \n 5) Delete book \n 6) Show library \n 7) Exit  ")
        
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            add_username()
        elif choice == 3:
            rent_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            delete_book()
        elif choice == 6:
            print(library)
        elif choice == 7:
            break
        else:  
            print ("wrong choice! please enter correct choice")
if __name__ == '__main__':
    main()


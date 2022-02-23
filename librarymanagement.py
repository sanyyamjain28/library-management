import datetime

class library:
    books = []
    issuebooks = dict()

    def __init__(self):
        self.issuebooks = dict()
        f = open("sampletext.txt", "r")
        file=f.read()
        self.books=file.split(",")
        f.close()

    def no_of_books(self):
        if len(self.books) == 0:
            print(f"The number of books in library is 0, library has opened today only. \nHope to see you soon.\n")
        else:
            print(
                f"In library currently there is {len(self.books)} books available. You can visit our store through feature page.")

    def store(self):
        for item in self.books:
            print(item , end=" ")
        print("\n")

    def add_book(self):
        c = input("Enter the name of the book to store : ")
        self.books.append(c)
        print(
            f"The book named \"{c}\" has been added Successfully!!\nThe final number of books now is {len(self.books)}. \n")
        print(f"Would you like to add more books ? \nType \"YES\" to add else \"NO\".")
        value2 = input()
        if (value2 == "YES" or value2 == "Yes" or value2 == "yes"):
            self.add_book()

        elif (value2 == "NO" or value2 == "No" or value2 == "no"):
            print(f"The books in library are \n", self.books)

        else:
            print("\t# Warning--- \nYou have entered wrong input.")

    def lend_book(self):
        issue_name_book = input("Enter the name of the book you want to issue : ")
        issue_name_person = input("Enter the name of the person who want to issue book : ")
        issue_date = input("Enter the date on which the book is being issue(dd-mm-yyyy) :")
        if issue_name_book in self.books:
            self.books.remove(issue_name_book)
            self.issuebooks.setdefault(issue_name_book,[]).append(issue_name_person)
            self.issuebooks.setdefault(issue_name_book,[]).append(issue_date)
            print(
                f"The book named \"{issue_name_book}\" is taken by {issue_name_person} on {issue_date} date.\nfinal number of books now is {len(self.books)}.")
        else:
            print(f"The book you are looking for in library is currently not available.\n\n ")

    def return_book(self):
        name_book = input("Enter the name of the book to return : ")
        name_person = input("Enter the name of the person by which the book issue : ")
        return_date = input("Enter the date on which you are returing the book(dd-mm-yyyy) : ")
        if (name_book in self.issuebooks.keys()) and (name_person in self.issuebooks[name_book]):
            self.books.append(name_book)
            self.issuebooks.setdefault(name_book,[]).append(name_person)
            self.issuebooks.setdefault(name_book,[]).append(return_date)
            print(
                f"The book named {name_book} has been returned by {name_person} on {return_date} date.\nThe final number of books now is {len(self.books)}. \n\n")
        elif (name_person not in self.issuebooks[name_book]) and (name_book in self.issuebooks.keys()):
            print("This book is not issued by this name.")
        else:
            print("This book is not issued from the library !!")


karan = library()
print(f"\nWelcome to demo library !!")
print("Would you like to explore library features ? Type \"YES\" to explore else \"NO\"")
value = input()
while value == "yes":
    print(
        f"\tFeature Page --\nType the number kept in front of the point which you want to opt for :\n 1. To see number of books available in library." \
        f"\n 2. To go to the store. \n 3. To add your book in the library.\n 4. To take book from library.\n " \
        f"5. To return a book which you have borrow from the library.\n 6. To Exit.")
    choice = input()
    if choice == "1":
        karan.no_of_books()
        print("If you want to visit to the feature page press \"YES\" else \"NO\".")
        value = input()
        if (value == "YES" or value == "Yes" or value == "yes"):
            continue
        elif (value == "NO" or value == "No" or value == "no"):
            print("Good Luck !!")
            break
        else:
            print("\t# Warning--- \nYou have entered wrong input.\nType \"YES\" to get back else \"NO\".")
            value = input()
            if (value == "YES" or value == "Yes" or value == "yes"):
                continue
            elif (value == "NO" or value == "No" or value == "no"):
                print("Good Luck !!")
                break

    elif choice == "2":
        karan.store()
        print("If you want to visit to the feature page press \"YES\" else \"NO\".")
        value = input()
        if (value == "YES" or value == "Yes" or value == "yes"):
            continue
        elif (value == "NO" or value == "No" or value == "no"):
            print("Good Luck !!")
            break
        else:
            print("\t# Warning--- \nYou have entered wrong input.\nType \"YES\" to get back else \"NO\".")
            value = input()
            if (value == "YES" or value == "Yes" or value == "yes"):
                continue
            elif (value == "NO" or value == "No" or value == "no"):
                print("Good Luck !!")
                break


    elif choice == "3":
        karan.add_book()
        print("If you want to visit to the feature page press \"YES\" else \"NO\".")
        value = input()
        if (value == "YES" or value == "Yes" or value == "yes"):
            continue
        elif (value == "NO" or value == "No" or value == "no"):
            print("Good Luck !!")
            break
        else:
            print("\t# Warning--- \nYou have entered wrong input.\nType \"YES\" to get back else \"NO\".")
            value = input()
            if (value == "YES" or value == "Yes" or value == "yes"):
                continue
            elif (value == "NO" or value == "No" or value == "no"):
                print("Good Luck !!")
                break

    elif choice == "4":
        karan.lend_book()
        print("If you want to visit to the feature page press \"YES\" else \"NO\".")
        value = input()
        if (value == "YES" or value == "Yes" or value == "yes"):
            continue
        elif (value == "NO" or value == "No" or value == "no"):
            print("Good Luck !!")
            break
        else:
            print("\t# Warning--- \nYou have entered wrong input.\nType \"YES\" to get back else \"NO\".")
            value = input()
            if (value == "YES" or value == "Yes" or value == "yes"):
                continue
            elif (value == "NO" or value == "No" or value == "no"):
                print("Good Luck !!")
                break

    elif choice == "5":
        karan.return_book()
        print("If you want to visit to the feature page press \"YES\" else \"NO\".")
        value = input()
        if (value == "YES" or value == "Yes" or value == "yes"):
            continue
        elif (value == "NO" or value == "No" or value == "no"):
            print("Good Luck !!")
            break
        else:
            print("\t# Warning--- \nYou have entered wrong input.\nType \"YES\" to get back else \"NO\".")
            value = input()
            if (value == "YES" or value == "Yes" or value == "yes"):
                continue
            elif (value == "NO" or value == "No" or value == "no"):
                print("Good Luck !!")
                break

    elif choice == "6":
        print("Good luck !!")
        break
    else:
        print("#Warning \nYou have entered wrong input !! \nType \"YES\" to get back else type \"NO\".")
        value = input()
        if value == "YES" or value == "Yes" or value == "yes":
            continue
        elif value == "NO" or value == "no" or value == "No":
            print("Good luck !!")
            break

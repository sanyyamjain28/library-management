class leave:
    name = None

    def __init__(self):
        self.data = dict()
        self.count = 0

    def details(self):
        f = open("leavedata.txt", "r")

        for line in f:
            key, value = line.split()
            self.data[key] = value

        for key, value in self.data.items():
            print(" ",key)

        f.close()

        print("\nEnter the name of person you want to check leave details : ")
        self.name= input()
        if (self.name in self.data.keys()) or (self.name.capitalize() in self.data.keys()):
            self.points()
        elif self.name not in self.data.keys():
            print( f"No data is registered with {self.name}.\nWould you want to go with another name ? ")
            c=input(f"Type \'Yes\' for another name else \'No\'\n")
            if c == "Yes" or c == "YES" or c == "yes":
                self.details()
            elif c == "NO" or c == "N" or c == "no":
                print("Good Luck !!")
            else:
                print("Warning --\nYou have choosen wrong input.")
                print("To go back Type \"Yes\" else \"No\".")
                value = input()
                if value == "Yes" or value == "YES" or value == "yes":
                    self.details()

                elif value == "NO" or value == "No" or value == "no":
                    print("Good Luck !")

        else:
            print(f"#Warning ---\nNo data is registered with {self.name}. kindly do the needful")
            self.details()

    def points(self):
        print(f"1. To check how many leave {self.name} can take in a year.")
        print("2. To check how many leaves remaining.")
        print(f"3. To check how many leaves {self.name} have taken.")
        # print("4. To check how many leaves got rejected.")
        print("4. To take leave.")
        print("5. To take exit.")

    def total_leave(self):
        print("Total number of leave allowed to take during a year is 45.")

    def leave_remaining(self):
        print(f"{self.name}, you can take {45 - int(self.data[self.name])} days leave more.")

    def leave_taken(self):
        print(f"{self.name} has taken {self.data[self.name]} leaves. \n")

    # def leave_rejected(self):
        # pass

    def take_leave(self):
        print(f"How many days leave you wish to take : ")
        self.count = int(input())
        f = self.count
        g = self.data[self.name]
        h = 45-int(g)
        j = h-(f)
        k = f + int(g)
        if f <= h:
            print(f"{self.name}, Leave granted !")
            print(f"{self.name}, you can take {j} more leave.")
            self.data.update( {self.name : k})
        else:
            print(f"{self.name}, you can't take leave for more than {(45 -k)} days.")



sanyyam = leave()
print("\nWelcome to the Leave Management System\nTo check how this system work. Press \"Yes\" to continue else any letter to exit.")
value = input()
print("\tLeave Management System ----")
print("Here is the data about people who have registered leave details : ")
while value == "YES" or value == "Yes" or value == "yes":
    sanyyam.details()
    choice = int(input())
    if choice == 1:
        sanyyam.total_leave()
        print("To go back to the system type \"Yes\" else \"No\".")
        value = input()
        if value == "Yes" or value == "YES" or value == "yes":
            continue

        elif value == "NO" or value == "No" or value == "no":
            print("Good Luck !")
            break
        else:
            print("#Warning -- \nSelected invalid choice.")
            print("To get back Type \"Yes\" else \"No\".")
            value = input()
            if value == "Yes" or value == "YES" or value == "yes":
                continue

            elif value == "NO" or value == "No" or value == "no":
                print("Good Luck !")
                break

            else:
                break

    elif choice ==2:
        sanyyam.leave_remaining()
        print("To go back to the system type \"Yes\" else \"No\".")
        value = input()
        if value == "Yes" or value == "YES" or value == "yes":
            continue

        elif value == "NO" or value == "No" or value == "no":
            print("Good Luck !")
            break
        else:
            print("#Warning -- \nSelected again invalid choice.")
            print("To get back Type \"Yes\" else \"No\".")
            value = input()
            if value == "Yes" or value == "YES" or value == "yes":
                continue

            elif value == "NO" or value == "No" or value == "no":
                print("Good Luck !")
                break

            else:
                break

    elif choice ==3:
        sanyyam.leave_taken()
        print("To go back to the system type \"Yes\" else \"No\".")
        value = input()
        if value == "Yes" or value == "YES" or value == "yes":
            continue

        elif value == "NO" or value == "No" or value == "no":
            print("Good Luck !")
            break
        else:
            print("#Warning -- \nSelected again invalid choice.")
            print("To get back Type \"Yes\" else \"No\".")
            value = input()
            if value == "Yes" or value == "YES" or value == "yes":
                continue

            elif value == "NO" or value == "No" or value == "no":
                print("Good Luck !")
                break

            else:
                break

    elif choice ==4:
        sanyyam.take_leave()
        print("To go back to the system type \"Yes\" else \"No\".")
        value = input()
        if value == "Yes" or value == "YES" or value == "yes":
            continue

        elif value == "NO" or value == "No" or value == "no":
            print("Good Luck !")
            break
        else:
            print("#Warning -- \nSelected again invalid choice.")
            print("To get back Type \"Yes\" else \"No\".")
            value = input()
            if value == "Yes" or value == "YES" or value == "yes":
                continue

            elif value == "NO" or value == "No" or value == "no":
                print("Good Luck !")
                break

            else:
                break

    elif choice ==5:
        print("Good Luck !")
        break

    else:
        print("#Warning --\nYou have not entered a valid choice.")
        print("To get back Type \"Yes\" else \"No\".")
        value = input()
        if value == "Yes" or value == "YES" or value == "yes":
            continue

        elif value == "NO" or value == "No" or value == "no":
            print("Good Luck !")
            break

        else:
            print("#Warning -- \nSelected again invalid choice.")
            print("To get back Type \"Yes\" else \"No\".")
            value = input()
            if value == "Yes" or value == "YES" or value == "yes":
                continue

            elif value == "NO" or value == "No" or value == "no":
                print("Good Luck !")
                break

            else:
                break


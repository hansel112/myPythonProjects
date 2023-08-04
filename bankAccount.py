class BankAccount:
    def __init__(self, name, faculty, course, YOS, university, contact, balance=0):
        self.name = name
        self.faculty = faculty
        self.course =course
        self.YOS = YOS
        self.university = university
        self.contact = contact
        self.balance = balance

    def withdraw(self,amount=0):
        amount = int(input("Enter withdraw amount: " ))
        self.info()
        if amount <= self.balance:
            print(f"Amount Withdrawn: Ush. {amount}")
            self.balance -= amount
        else:
            print("You have insufficient balance")
        print("**************************************")
        
    def deposit(self,amount1=0):
        amount1 = int(input("Enter the deposit amount: "))
        self.info()
        print(f"Amount deposited:  Ush. {amount1}")
        self.balance += amount1
        print("**************************************")

    def info(self):
        print("***********SAVINGS ACCOUNT***********")
        print(f"Name:              {self.name}")
        print(f"Faculty:           {self.faculty}")
        print(f"Course:            {self.course}")
        print(f"Year of study:     {self.YOS}")
        print(f"University:        {self.university}")
        print(f"Tel:               {self.contact}")

    def menu(self):
        print("=======MENU========")
        print("1. Balance inquiry.")
        print("2. Deposit.")
        print("3. Withdraw.")
        print("4. Exit.")
        print("===================")
        option='5'
        while option != '4':
            print()
            print()
            option = input("Choose from menu: ")
              
            if option == '1':
                self.info()
                print(f'Account balance:   Ush. {self.balance}')
                print("**************************************")
            elif option =='2':
                self.deposit()   
            elif option == '3':
                self.withdraw()
            elif option =='4':
                print("Thamk you for using our service. Good bye.")
            else:
                print("Invalid input. please try again")

        
Student_Account = BankAccount("Sempo", "Faculty of engineering", "BCT", "2020/2021", "Busitema University", "0786483424",0)
Student_Account.menu()




"""print(Student_Account.name)
Student_Account.deposit()
Student_Account.deposit()
Student_Account.withdraw()
#print(Student_Account.balance)
Student_Account.info()"""

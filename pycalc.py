class Operations:
    def add(self):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        return num1+num2
    
    def sub(self):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        return num1-num2
    
    def mul(self):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        return num1*num2
    
    def div(self):
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        return num1/num2
    
if __name__ == "__main__": 
    op = Operations()
    while(True):
        try:
            print("************************* CALCULATOR *************************")
            ch = int(input("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit \nEnter your choice: "))
            if ch == 1:
                print("Addition = " + str(op.add()))
            elif ch == 2:
                print("Subtraction = " + str(op.sub()))
            elif ch == 3:
                print("Multiplication = " + str(op.mul()))
            elif ch == 4:
                print("Division = " + str(op.div()))
            elif ch == 5:
                print("Exiting..!")
                break
            else:
                print("Invalid input, please check it")
            print()
        except Exception as e:
            print(e)

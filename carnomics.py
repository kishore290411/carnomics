
print("Welcome To DN Motors!")

rbs=input("Do you want to Buy or Rent?(B/R) : ")
if rbs == "R":
    print("B-A - 15,000")
    print("B-B - 20,000")
    budget = input("What is your budget to Rent your new car: ")

    if budget == "B-A":
        print("The cars available in this price range are:")
        print("RA - Ford Ecosport")
        print("RB - Hyundai Palisade")
        print("RC - Toyota Corolla")

        dn = input("Which of these would you like to rent?:")
        if dn == "RA" or "RB" or "RC":
            
            print("Thank you for shopping with DN Motors!")
            quit()
            
          

       
            

        

    if budget == "B-B":
        print("The cars available in this price range are:")
        print("2RA -  Toyota Camry")
        print("2RB - Mitsubishi Lancer")
        print("2RC - Nissan Altima")
        print("2RD - Toyota Prius")

        db = input("Which of these would you like to rent?:")
        if db == "2RA" or "2RB" or "2RC":
             print("Thank you for shopping with DN Motors!")
             quit()
print("*************************************************************************")
            

        

print("A - Toyota Highlander")
print("B - Tesla Model X")
print("C - Tesla Cybertruck")
print("D - Audi E-Tron GT")
print("E - Ferrari SF 90")
a=input("Enter your car from the options given above:")
print("*****************************************************************")

if a == "A":
    x =  input("the car you have preferred is a Toyota Highlander, and the price for the selected car is AED 179,000. Do you wish to proceed? (Y/N): ")
    if x == "Y":
        print("Thank you for shopping with DN Motors! We hope to see you again!")

    else:
        print("We hope to see you again next time!")

if a == "B":
    x =  input("the car you have preferred is a Tesla Model X, and the price for the selected car is AED 437,000 . Do you wish to proceed? (Y/N): ")
    if x == "Y":
        print("Thank you for shopping with DN Motors! We hope to see you again!")

    else:
        print("We hope to see you again next time!")

if a == "C":
    x =  input("the car you have preferred is a Tesla Cybertruck, and the price for the selected car is AED 253,000 . Do you wish to proceed? (Y/N): ")
    if x == "Y":
        print("Thank you for shopping with DN Motors! We hope to see you again!")

    else:
        print("We hope to see you again next time!")

if a == "D":
    x =  input("the car you have preferred is a Audi E-Tron GT, and the price for the selected car is AED 300,000. Do you wish to proceed? (Y/N): ")
    if x == "Y":
        print("Thank you for shopping with DN Motors! We hope to see you again!")

    else:
        print("We hope to see you again next time!")

if a == "E":
    x =  input("the car you have preferred is a Ferrari SF 90, and the price for the selected car is AED 1.7 Million. Do you wish to proceed? (Y/N): ")
    if x == "Y":
        print("Thank you for shopping with DN Motors! We hope to see you again!")

    else:
        print("We hope to see you again next time!")



    





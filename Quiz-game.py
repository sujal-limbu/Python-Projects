print("--------------------------------")
print("Welcome to the Quiz-Game")
print("--------------------------------")

Name = input("Enter your name: ")
print(f"Hi ,{Name}")
score = 0   
Q = input("Are you ready for the Question ?")

if Q.lower() == "yes":
    print("Let's Play")
else:
    quit()
 

Q1 = input("Q1: What is Capital of France ?")    
if Q1.lower() == "paris":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")    

Q2 = input("Q2: What is largest ocean ?")    
if Q2.lower() == "pacific":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")    

Q3 = input("Q3: What is Unit of electrical current? ?")    
if Q3.lower() == "ampere":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")    

Q4 = input("Q4: Which Country is known for kangaroos? ?")    
if Q4.lower() == "australia":
    print("Correct :)")
    score += 1
else:
    print("Incorrect :(")    

print(f"You got {score} Question Correct :)")



    

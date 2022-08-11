print("welcome to this mini quizz game developed by Benjamin Kuro")
choice = input("Do you want to play yes or no\n")
if choice  != "yes":
    quit()
user_name= input("Enter your name \n")
print(f"Welcome {user_name}")

# score
score = 0


print("Question 1")
question ="what is the full meaning of RAM\n"
answer = "random access memory"
question1 = input(question.lower())
if question1 == answer:
    print("correct")
    score += 1
    print(f"score: {score}")
else:
    print("wrong")

print("Question2")
question2 ="What is the full meaning CPU\n"
answer2 ="central processing unit"
question3 = input(question2.lower())
if question3 == answer2:
    print("correct")
    score +=1 
    print(f"score: {score}")
else:
    print("wrong")
    score
    print(f"score: {score}")

print("Question3")
question4 ="What is the full meaning of ROM\n"
answer3 = "read only memory"
question5 = input(question4.lower())
if question5 == answer3:
    print("correct")
    score += 1
    print(f"score: {score}")
else:
    print("wrong")
    score 
    print(f"score: {score}")

print(f"Your total score is {score}")
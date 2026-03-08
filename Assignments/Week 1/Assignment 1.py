"Question 1: Write a program that converts a temperature from Celsius to Fahrenheit"

Celsius = 25 

#formula 
Fahrenheit = (25 * 9/5) + 32
print("Temprature in fahrenheit is :",Fahrenheit)

# If we add some Logical conditions 
if Fahrenheit > 100:
    print("It's a warm day")
else :
    print(" It's a pleasant day")





"Question 2: Calculate Area of a Rectangle "

Length=10
width=5

#formula 
area=Length*width
print("Area of rectangle is :",area)

# If we add some Logical conditions 
if area > 80 :
    print("It's a large rectangle ")
else:
    print("It's a small rectangle")





"Question 3: Calculate Compound Interest"
" Use the formula: CI = P * (1 + R/100)**T - P"
" Where P = principal, R = rate, T = time"

P=500              #Principal amount
R=5                #Rate
T=3                #Time in years

#formula  
CI=P*(1+R/100)**T-P
print("Compound Interest is :",CI)





"Question 4: Perimeter of a Rectangle Take length and width as input and calculate the perimeter"

length=float(input("Enter length of rectangle: "))
Width=float(input("Enter width of rectangle:"))

#formula  
Perimeter=2*(length*Width)
print("The perimeter of rectangle is :",Perimeter)

# If we add some Logical conditions
if Perimeter < 26:
    print("It's a mini rectangle")
else:
    print("It's a normal size rectangle")





"Question 5: Average of Three Numbers - Input three numbers and print their average. "
 
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))

#formula  
Average=num1+num2+num3/3
print("The average is :",Average)

# If we add some Logical conditions
if Average<50:
    print("|Average is Low")
else:
    print("Average is high")

     



"Question 6: Square and Cube of a Number "
" Ask the user for a number and display its square and cube.  "

Number=float(input("Enter a number:"))

#squaring  number
Square=Number**2
Cube=Number**3

print("The square of ",Number,"is=",Square)
print("The cube of ",Number,"is",Cube)




"Question 7: Distribute Items Equally "
" You have n candies and k students. "
"Write a program to find: how many candies each student gets and how many are left "


N=int(input("Enter number of candies:"))
K=int(input("Enter number of students:"))

#formula  
candies_student_get=N//K
Left_over=N % K

print=("Each student get:",candies_student_get,"candies")
print=("Left over candies:",Left_over)





"Question 8: Calculate Profit or Loss Input cost price and selling price. "
"Display either: Profit and amount,"
" or Loss and amount, or No Profit No Loss"


CP=float(input("Enter cost price :"))
SP=float(input("Enter sale price :"))

#Profit

if SP>CP :
    Profit_Amount=SP-CP
    print("Profit is:",Profit_Amount)
#Loss
elif CP>SP:
  Loss_Amount=CP-SP
  print("Loss is: ",Loss_Amount)
else:
  print("No profit no loss .you sell at same price")






"Question 9: Total Marks and Percentage"
" Input marks of 5 subjects. Print: "
"Total marks "
"Percentage "
"Average"


English=("Enter marks of english paper:")
Maths=("Enter marks of maths paper:")
Computer=("Enter marks of computer paper:")
Geo=("Enter marks of geo paper:")
His=("Enter marks of his paper:")

#Total
Total_marks=English+Maths+Computer+Geo+His
print("Total marks are :",Total_marks)

#Average 
Average=Total_marks/5
print("Average of Marks is:",Average)

#Percentage
Percentage=Total_marks/500*100
print("Percentage is:",Percentage)





'Question 10: Salary Calculator. Input basic salary. Calculate'
'HRA = 20% of basic'
'DA = 15% of basic'
'Total Salary = Basic + HRA + DA'

Basic_Salary = int(input("Enter The Basic Salary: "))
HRA = Basic_Salary * 20/100
DA = Basic_Salary * 15/100

Total_Salary = Basic_Salary + HRA + DA
print("Total Salary Is: ", Total_Salary)






'Question 11: Age in Months and Days'
'Input your age in years.Calculate and print age in:'
'Months,Days (approximate)'

age = int(input("Enter Your Age: "))

#Months
Month = age * 12

#Days
Days = age * 365

print("Your Age in Months is: ", Month)
print("Your Age in Days is: ", Days)






'Question 12: Currency Converter (USD to PKR)'
'Input amount in USD. Convert using a fixed Exchange rate'

# The Current Fixed Exchange rate of 1 PKR to USD is 0.0035
#  (resource: Western Union Website current rate)

PKR = 0.0035
Amount_In_USD = float(input("Please Enter Amount In USD: "))

#formula
Converted_Amount = Amount_In_USD * PKR

print("Yout Converted Amount in PKR is: ", Converted_Amount)







'Question 13: Sum of First Natural Numbers'
'Input a number n, Calculate first n natural numbers. Formula n*(n+1)/2'

n = int(input("Enter The Number: "))

#formula
sum = n*(n+1)/2
print("Sum of First Natural Numbers: ", sum)




'Question 14: Percentage Of Correct Answers'
'Input total questions and correct answers and calculate the percentage score'

Total_Question = int(input("Enter The Number Of Total Question: "))
Correct_Answers = int(input("Enter The Number Of Correct answer: "))

#formula
Percentage_Score = (Correct_Answers/Total_Question)*100

print("The Percentage Score Is: ",Percentage_Score)




'Question 15: Speed, Distance and Time'
'Input Distance and Time and calculate Speed'

# Distance = d, Time = t
d = float(input("Enter The Distance Traveled: "))
t = int(input("Enter The Time Taken in mins: "))

#formula
speed = d/t

print("The Speed Is: ", speed)





'Question no 16:Calculate Body Max Index'
'Input weight(kg) and height(m),then calculate BMI = weight/(height**2)'

# weight = w, height = h

w = float(input("Enter The weight: "))
h = float(input("Enter The Height: "))

#formula
BMI = w/(h**2)

print("The BMI is: ", BMI)





'Question no 17:'
'Calculate Body Max Index'
'Input weight(kg) and height(m),then calculate BMI = weight/(height**2)'

# weight = w, height = h

w = float(input("Enter The weight: "))
h = float(input("Enter The Height: "))

#formula
BMI = w/(h**2)

print("The BMI is: ", BMI)














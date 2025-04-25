# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

def age_group_categorization():
    age = int(input("Enter your age : "))

    if (age < 13):
        print ("You're child.\n")

    elif (age < 19):
        print ("You're teenager.\n")

    elif (age < 59):
        print ("You're adult.\n")

    else:
        print ("You're senior.\n")

# age_group_categorization()


# 2. Movie ticket pricing 
# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

def movie_ticket_pricing():
    price = 12
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for i, day in enumerate (days, start=0):
        print (i,". ",day)

    day = int(input("Enter the day you want to book ticket for? : "))
    age = int(input ("Enter the age of user : "))

    if (age < 18):
        price = 8

    if (day == 3):
        price -= 2

    print("Your price is : ", price)

# movie_ticket_pricing()


# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).


def grade_calculator():
    score = int (input ("Enter your score : "))

    if (score>=90 and score<=100):
        grade = 'A'
    elif (score>=80 and score<=89):
        grade = 'B'
    elif (score>=70 and score<80):
        grade = 'C'
    elif (score>=60 and score<70):
        grade = 'D'
    elif (score>0 and score <60):
        grade = 'F'
    else:
        print ("Invalid score.")

    print ("You've got ", grade, " grade.")

# grade_calculator()


# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

def fruit_ripeness_checker():
    color = (input("Enter the color of fruit : ")).lower()

    if (color == "green"):
        print("Unripe")
    elif (color == "yellow"):
        print("Ripe")
    elif (color == "brown"):
        print("Overripe")
    else:
        print ("Invalid color")

# fruit_ripeness_checker()

# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

def weather_activity_suggestion():
    weathers = ["Sunny", "Rainy", "Snowy"]
    weather = (input("Enter the weather : ")).lower()

    if (weather == "sunny"):
        activity = "Go for a walk."
    elif (weather == "rainy"):
        activity = "Read a book."
    elif (weather == "snowy"):
        activity = "Build a snowman."
    else:
        message = "Invalid weather. Weather may be one of : "
        activity = message, weathers

    print(activity)        

# weather_activity_suggestion()


# Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

def leap_year_checker():
    year = int (input ("Enter the year : "))

    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        message = " is a leap year."
    else:
        message = " is not a leap year."

    print (str(year) + message)

leap_year_checker()
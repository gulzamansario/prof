# # age=int(input("Enter your age:- "))
# # if age >= 18:
# #     print("Yes")
# # else:
# #     print("not")

# # # Relations ships operators 
# # # ==: equals.
# # # > =: greater than/ equal to.
# # # < =: lesser than/ equal to.



# # # Logical operators 
# # # For Example:
# # # and – true if both operands are true else false.
# # # or – true if at least one operand is true or else false.
# # # not – inverts true to false & false to true.

# # # IMPORTANT NOTES:
# # # 1. There can be any number of elif statements.
# # # 2. Last else is executed only if all the conditions inside elifs fail.




# # # 1. Write a program to find the greatest of four numbers entered by the user.
# # # 2. Write a program to find out whether a student has passed or failed if it requires a
# # # total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# # # take marks as an input from the user.
# # # 3. A spam comment is defined as a text containing following keywords:
# # # “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# # # to detect these spams.

# # # 4. Write a program to find whether a given username contains less than 10
# # # characters or not.

# # # 5. Write a program which finds out whether a given name is present in a list or not.
# # # 6. Write a program to calculate the grade of a student from his marks from the
# # # following scheme:
# # # 90 – 100 => Ex
# # # 80 – 90 => A
# # # 70 – 80 => B
# # # 60 – 70 =>C
# # # 50 – 60 => D
# # # <50 => F
# # # 7. Write a program to find out whether a given post is talking about “Harry” or not.





# # # 1. Write a program to find the greatest of four numbers entered by the user.

# # num1 = float(input("Enter the number: "))
# # num2 = float(input("Enter the number: "))
# # num4 = float(input("Enter the number: "))
# # num3 = float(input("Enter the number: "))

# # if num1 > num2 and num3 and num1 > num4:
# #     print(f"{num1} is greater")
# # elif num2 > num1 and num3 and num2 > num4:
# #     print(f"{num2} is greater")
# # elif num3 > num1 and num2 and num3 > num4:
# #     print(f"{num3} is greater")
# # elif num4 > num1 and num2 and num4 > num3:
# #     print(f"{num4} is greater")
# # else:
# #     print("There is issue in the code or logic please check")




# # # 2. Write a program to find out whether 
# # # a student has passed or failed if it 
# # # requires a total of 40% and at least 33% 
# # # in each subject to pass.
# # #  Assume 3 subjects and take marks as an input from the user.




# # math = float(input("Enter your math marks: "))
# # eng = float(input("enter your eng marks: "))
# # urdu = float(input("Enter your urdu marks: "))
# # total = 300
# # percentage = ((math+eng+urdu) / total) * 100
# # if math >= 33 and eng >= 33 and urdu >= 33 and percentage >= 40:
# #     print("Pass")
# #     print("Percentage:", percentage)
# # else:
# #     print("Fail")
# #     print("Percentage:", percentage)




# # 3. A spam comment is defined as a text containing following keywords:
# # “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# # Write a program to detect these spams.


# # spams = ["Make a lot of money","buy now" , "subscribe this", "click this" ]

# # para = 'The Peoples Bus Service R9 buy now (Gulshan-e-Hadeed to Tower) operates daily. The first bus departs from the Al-Khidmat Make a lot of money stop at 5:45 AM, and the last bus departs at 7:00 PM. Buses arrive every 10 to 15 minutes, with a standard fare of PKR 80–120 depending on distance.The R9 route is a key Red Bus service stretching 42 km, linking the eastern suburb of Gulshan-e-Hadeed through major arteries to the city center at Tower. The fleet includes standard red buses, and some designated R9 Pink Bus services for women.Do you need the full list of stops along the R9 route, or would you like to know the timings for the Pink People"s Bus Service instead?'
# # for spam in spams:
# #     if spam in para:
# #         print(f"{para}\n ||=====s an scammed Email=====||")
# #         break
# #     else:
# #         print("Safe mail")


# # username = "Gul zaman   "
# # if len(username) <= 9:
# #     print(f"No not containes characters  {username}")
# # elif len(username) == 10:
# #     print("Yes exact 10 characters")
# # else:
# #     print(f"{username} is more than 10 ")


# # #  5. Write a program which finds out whether a given name is present in a list or not.

# # names = ["aslam", "afsha", "akram", "nimra"]
# # give = "aslam"
# # if give in names:
# #     print(f"Yes {give } is in the list ")
# # else:
# #     print(f"No {give} is not in a list ")


# # # 6. Write a program to calculate the grade of a student from his marks from the
# # # following scheme:
# # # 90 – 100 => Ex
# # # 80 – 90 => A
# # # 70 – 80 => B
# # # 60 – 70 => C
# # # 50 – 60 => D
# # # <50 =>     F

# student_mark = 56.0

# if student_mark >= 90:
#     print("Excellent")
# elif student_mark > 80 and student_mark < 90:
#     print("Grade A")
# elif student_mark > 70 and student_mark < 80:
#     print("Grade B")
# elif student_mark > 60 and student_mark < 70:
#     print("Grade C")
# elif student_mark > 50 and student_mark < 60:
#     print("Grade D")
# elif student_mark < 50:
#     print("FAIL")



# #  7. Write a program to find out whether a given post is talking about "Gul zaman" or not.

# names=["Gul zaman", "gulzaman", "gul", "gz", "gzdeveloper"]
# post = " gzdeveloper The Peoples Bus Service gz R9 (Gulshan-e-Hadeed to Tower) operates daily. The first bus departs from the Al-Khidmat stop at 5:45 AM, and the last bus departs at 7:00 PM. Buses arrive every 10 to 15 minutes, with a standard fare of PKR 80–120 depending on distance.The R9 route is a key Red Bus service stretching 42 km, linking the eastern suburb of Gulshan-e-Hadeed through major arteries to the city center at Tower. The fleet includes standard red buses, and some designated R9 Pink Bus services for women.Do you need the full list of stops along the R9 route, or would you like to know the timings for the Pink People's Bus Service instead?"
# for name in names:
#     for name in post:
#         print("Yes ")
#         break
#     else:
#         print("not")
#         break
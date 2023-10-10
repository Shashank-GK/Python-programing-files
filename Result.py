n = int(input("Enter the total number of Subject: \n"))
marks = []
for i in range(n):
    subject = input(f"Enter marks for subject {i+1}: ")
    marks.append(float(subject))
T_marks = sum(marks)
p = (T_marks / (n * 100)) * 100

if p >= 75:
    print(
        "you got totally {0} marks and your percentage is {1} % ".format(
            str(T_marks), str(p)
        )
    )
    print("You got Distinction in 1st class ")
elif p >= 65 and p < 75:
    print(
        "you got totally {0} marks and your percentage is {1} % ".format(
            str(T_marks), str(p)
        )
    )
    print("you got first class ")
elif p >= 35 and p < 65:
    print(
        "you got totally {0} marks and your percentage is {1} % ".format(
            str(T_marks), str(p)
        )
    )
    print("You got 2nd class ")
else:
    print(
        "you got totally {0} marks and your percentage is {1} % and you got failed".format(
            str(T_marks), str(p)
        )
    )

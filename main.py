print("Enter marks obtained in 4 subjects.")
math = int(input("Math: "))
Science = int(input("Science: "))
hin = int(input("Hindi: "))
eng = int(input("English: "))
sum = (math+Science+hin+eng)
percent = (  sum / 400)*100
print(percent, "%")
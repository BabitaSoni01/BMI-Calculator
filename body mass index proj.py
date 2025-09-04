# body mass index calculator
# bmi = weight / height**2 

w = int(input("Enter the weight in kg :"))
h = float(input("Enter the height in meter: "))

bmi = float(w)/h**2
if (bmi<=18.4):
    print('Under weight')
elif (bmi>=18.5 and bmi<=24.9):
    print("Normal")
elif (bmi>=25.0 and bmi<=39.9):
    print("overweight")
else:
    print("obese")

print(bmi)
correct = round(78.3873,2)
print(correct)
# round(data,3) it is used to display after decimal values

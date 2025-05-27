#  Asking the user for the first number
x = input("What is your first number? ")


#  Asking the user for the second number
y = input("What is your second number? ")

#  Calculating the result (using int as not set earlier)
z = int(x) + int(y)

#  Print the result
print(z)

#  Step 2: Rounding Results
print("Step 2: We will look at adding decimals and rounding them.")

#  Get the decimals
a = float(input("What is the first decimal you want to use? "))
b = float(input("What is the second decimal you want to use? "))

#  Add together and round
c = round(a + b)
print(c)

#  Step 3: rounding to decimal places
print("The number below is 2 thirds rounded to 2 decimal places.")
m = 2
n = 3
o = round(m/n, 2)
print(o)

# Step 4: present the findings in a different format
print(f"{o:.1f}")

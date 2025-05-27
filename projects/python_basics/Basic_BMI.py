# Demographic Data
first_name = "John"  # string: athlete's first name
last_name = "Smith"  # string: athlete's last name
age = 25  # integer: athlete's age
position = "Right Back"  # string: athlete's playing position
rtp = True  # boolean: return to play status
height_m_sq = 3.35  # float: players height in metres squared
weight_kg = 84.5  # float: players weight in kg


# BMI Calculator
def calculate_bmi(weight_kg, height_m_sq):
    bmi = weight_kg / height_m_sq
    return bmi


# Calculating BMI
user_bmi = calculate_bmi(weight_kg, height_m_sq)
print(f"Hello! Your BMI is {user_bmi:.2f}")
if user_bmi > 25:
    print("You are overweight.")
if user_bmi <= 25:
    print("You are not overweight.")

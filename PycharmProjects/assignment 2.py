# length of a zander in centimeter

length = float(input("Enter the length of the zander in centimeters: "))

if length < 42:
    difference = 42 - length
    print("Release the fish back into the lake.")
    print("The fish is", difference, "centimeters below the size limit.")
else:
    print("The fish meets the size limit. You can keep it.")



#cabin class of a cruise ship

cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


#  the hemoglobin value is low, normal or high

gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")

elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")

else:
    print("Invalid gender.")


# year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")









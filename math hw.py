import math


degree = float(input("Enter the angle in degrees: "))


rad = math.radians(degree)


sin_value = math.sin(rad)
cos_value = math.cos(rad)
tan_value = math.tan(rad)

# Display results
print("Sin(", degree, ") =", sin_value)
print("Cos(", degree, ") =", cos_value)
print("Tan(", degree, ") =", tan_value)
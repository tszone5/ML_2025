print("5-Day Temperature Average Calculator")
print("-----------------------------------")

temperatures = []  


for day in range(1, 6):
    temp = float(input(f"Enter temperature for Day {day}: "))
    temperatures.append(temp)


average_temp = sum(temperatures) / len(temperatures)


print("\nTemperature Record:")
print(f"All temperatures: {temperatures}")
print(f"Average temperature: {average_temp:.1f}°C")

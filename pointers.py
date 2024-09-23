num1 = {"val": 1}
num2 = num1
num2["val"] = 22

print(num1.values())
print("num1 points to ", id(num1), "\nnum2 points to ", id(num2))
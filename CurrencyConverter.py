# Currency Converter

with open("currencyData.txt") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    pasred = line.split("\t")
    currencyDict[pasred[0]] = pasred[1]
    

amount = int(input("Enter the amount: /n"))
print("Enter the name of currency want to convert this amount to? Available options: /n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values: /n")
print(f"Amount in INR is: {amount * float(currencyDict[currency])} {currency}")        
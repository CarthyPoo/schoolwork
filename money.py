x = input("type USD if you would like to convert USD to CAD or type CAD if you would like to convert CAD to USD. ")

if x == 'USD'.lower():
    c = float(input('how much money would you like to convert? '))
    z = c * .79
    print(f'${z} USD')

elif x == 'CAD'.lower():
    c = float(input('how much money would you like to convert? '))
    v = c * 1.26
    print(f'${v} CAD')

else:
    print("Sorry i don't understand. Please pick either USD or CAD")


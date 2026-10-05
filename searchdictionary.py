supplies= {"book": 20, "pen": 10, "pencil": 6}
find= input("Enter supply name: ").lower()
for key in supplies:
    if find in supplies:
        print("Supplies found")
        break
    else:
        print("Supplies not there")
        supplies[find]=input("Enter quantity: ")
        break
print(supplies)
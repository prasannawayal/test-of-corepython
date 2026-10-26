length = float(input("Enter length of room: "))
breadth = float(input("Enter breadth of room: "))
height = float(input("Enter height of room: "))
cost = float(input("Enter painting cost per sq.ft: "))

area = 2 * height * (length + breadth)

total_cost = area * cost

print("Area of four walls =", area)
print("Total painting cost =", total_cost)
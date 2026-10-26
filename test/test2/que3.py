radius=20
length=50
breadth=40
cost=35
circle = 3.14*radius
rectangle= 2*(length+breadth)
perimeter = circle + rectangle
total_wire = perimeter * 5
total_cost = total_wire * cost

print('total perimeter:',perimeter,'m')
print('total wire required:',total_wire,'m')
print('total fencing cost: ',total_cost)

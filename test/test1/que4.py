area = float(input('enter area of one wall'))
interior_cost=float(input('enter interior painting cost per unit area'))
exterior_cost=float(input('enter exterior painting cost of per unit area'))
interior_area=2*area
exterior_area=6*area
total_interior=interior_area*interior_cost
total_exterior=exterior_area*interior_cost
print('total interior painting cost',total_interior)
print('total exterior painting cost',total_exterior)
print('total painting cost',total_interior + total_exterior)
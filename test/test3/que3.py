n = int(input('enter no of employee:'))
total_salary = 0
for i in range(1,n+1):
    basic = int(input(f'enter basic salary of emplyee {i}:'))
    if basic < 20000:
        da = 10 * basic / 100
        ta = 12 * basic / 100
        hra = 15 * basic / 100
    else:
        da = 15 * basic / 100
        ta = 18 * basic / 100
        hra = 20 * basic / 100

    salary = basic + da + ta + hra
    print("Employee", i)
    print("Basic Salary =", basic)
    print("DA =", da)
    print("TA =", ta)
    print("HRA =", hra)
    print("Total Salary =", salary)


    total_salary = total_salary + salary
print('total salary of all empoyee',total_salary)

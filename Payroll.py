
# Description of Program: This program takes in factors of an employee's working hours. It then calculates different deductions from the given hours and pay rate to come out with a net pay.
def Payroll():
    name = input("Enter employee's name: ")
    hours = float(input("Enter number of hours worked in a week: "))
    rate = float(input("Enter hourly pay rate: "))
    fed = float(input("Enter federal tax witholding rate: "))
    state = float(input("Enter state tax witholding rate: "))
    gross = hours * rate
    fed = gross * .20
    state = gross * .09
    tot = fed + state
    net = gross - tot

    print(" ")

    print("Employee Name:", name)
    print("Hours Worked:", hours)
    print("Pay Rate: $" + format(rate, "4.2f"))
    print("Gross Pay: $" + format(gross, "4.2f"))
    print("Deductions:")
    print("    Federal Witholding (20.0%): $" + format(fed, "4.2f"))
    print("    State Witholding (9.0%): $" + format(state, "4.2f"))
    print("    Total Deduction: $" + format(tot, "4.2f"))
    print("Net Pay: $" + format(net, "4.2f"))


Payroll()

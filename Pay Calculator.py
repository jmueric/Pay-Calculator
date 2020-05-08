#Ask for all of the Inputs
name = input("Enter Employee's Name (first and last): ")
numHours = eval(input("Enter number of hours worked this week: "))
payRate = eval(input("Enter hourly pay rate: "))
fedRate = eval(input("Enter federal tax withholding rate (.10 for single or .15 for married) : "))
stateRate = eval(input("Enter the state tax withholding rate: "))

#PROCESSING SECTION
#Find the Gross Pay
grossPay = numHours * payRate

#Find Federal Withholding
fedWithhold = grossPay * fedRate

#Find State Withholding
stateWithhold = grossPay * stateRate

#Find Total Deductions
totalDeductions = fedWithhold + stateWithhold

#Find Net Pay Check
netPay = grossPay - totalDeductions


#Print Output
print("\n\nEmployee Name:", name, "\n")
print("Hours Worked:", numHours)
print("Pay Rate: ", format(payRate, ",.2f"), sep="$")
print("Gross Pay: ", format(grossPay, ",.2f"), sep="$")
print("Deductions:")
print("\tFederal Withholding " + "(" + format(fedRate, "2.0%") + "):" + "\t$ " + format(fedWithhold, ",.2f"))
print("\tState Withholding " + "(" + format(stateRate, "2.0%") + "):" + "\t$ " + format(stateWithhold, ",.2f"))
print("\tTotal Deductions:" + "\t\t$ " + format(totalDeductions, ",.2f"))
print("Net pay check: " + "\t\t$ " + format(netPay, ",.2f"))

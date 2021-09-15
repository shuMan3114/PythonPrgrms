principle = eval(input("Enter principle: "))
timePeriod = eval(input("Enter time period in years: "))
rateOfInterest = eval(input("Enter Rate of interest/ annum in %: "))

simpleInterest = principle*timePeriod*rateOfInterest/100
compoundInterestIntermediate = (1 + rateOfInterest/100)**timePeriod
compoundInterest = principle*compoundInterestIntermediate - principle

print("Simple Interest is", simpleInterest, "\n" "Compound Interest is", compoundInterest)

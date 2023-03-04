# read input
n = int(input())
records = []
for i in range(n):
    record = input().split()
    record[1] = record[1].lower() == 'true' # convert isValid to boolean
    records.append(record)

# check validity
allValid = True
errorCodes = []
for record in records:
    if not record[1]:
        allValid = False
        errorCodes.append(record[2])

# print result
if allValid:
    print("Yes")
else:
    print("No")
    print(" ".join(errorCodes))

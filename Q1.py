# read input
n = int(input())
tshirts = input().split()
m = int(input())
requests = input().split()

# create a dictionary to represent the available tshirts
# key: size, value: the corresponding tshirt object
tshirt_dict = {}
for tshirt in tshirts:
    size = tshirt.count("X")
    tshirt_dict[size] = tshirt

# iterate through requests and check if each can be fulfilled
for request in requests:
    request_size = request.count("X")
    found = False
    # iterate through tshirt sizes starting from the requested size
    for size in range(request_size, 1001):
        if size in tshirt_dict:
            found = True
            break
    if not found:
        print("No")
        break

else:
    print("Yes")

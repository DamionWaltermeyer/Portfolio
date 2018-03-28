#loop through numbers 1 through 20 inclusive
# #4 and 13 should be unlucky only.
#everything else is labeled as even or odd

for x in range(1,21):
    if x == 4 or x == 13:
        print(f"{x} is unlucky")
    elif (x % 2) != 0:
        print(f"{x} is odd")
    else:
        print(f"{x} is even")

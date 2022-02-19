# Find the cube root
x = int(input("Gimmy an int to find its cube root: \n"))
ans = 0
while ans ** 3 < x:
    ans += 1
if ans ** 3 != x:
    print(f"{x} is not a perfect cube")
else:
    print(f"The cube root of {x} is, {ans} ")
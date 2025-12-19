ticket = input()

a = int(ticket[0])
b = int(ticket[1])
c = int(ticket[2])

d = int(ticket[3])
e = int(ticket[4])
f = int(ticket[5])

first_sum = a + b + c
second_sum = d + e + f

if first_sum == second_sum:
    print("YES")
else:
    print("NO")

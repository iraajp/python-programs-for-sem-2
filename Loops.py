#
i = 1
while i <= 10:
    print(i)
    i += 1





i = 1
while i < 7:
    print(i)
    if i == 4:
        break
    i += 1




i = 0
while i < 7:
    i += 1
    if i == 4:
        continue
    print(i)


hardware = ["Monitor", "Printer", "Mouse"]
for x in hardware:
    print(x)

for x in range(7):
    print(x)



a = int(input("input any number for print table "))
for x in range(1, 11):
    b =  a * x
    print(a, "*", x, "=", b)

Loops in python
While Loop Example
i = 1
while i <= 10:
    print(i)
    i += 1




The break statement
i = 1
while i < 7:
    print(i)
    if i == 4:
        break
    i += 1



The continue statement
i = 0
while i < 7:
    i += 1
    if i == 4:
        continue
    print(i)



For Loop:
hardware = ["Monitor", "Printer", "Mouse"]
for x in hardware:
    print(x)


The range() Function
returns a sequence of numbers,
starting from 0 by default, and by default
increments by 1.
for x in range(7):
    print(x)



a = int(input("input any number for print table "))
for x in range(1, 11):
    b =  a * x
    print(a, "*", x, "=", b)

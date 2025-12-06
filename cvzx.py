l = [1,23,124, 1,5,135,3,3151,13576,88,353,5255,69686]
sum = 0
a= 1
if len(l) >=5:
    for i in l:
        sum +=i
    print("Сума",sum)
elif len(l) <=3:
    for i in l:
        a *=i
    print("Добуток",a)
else:
    print("Довжина списку",len(l))
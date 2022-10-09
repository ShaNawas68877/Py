#Exercise 13 : Making Change

topay = int(input('Enter the amount to be paid:'))
r2000 = 2000
r500 = 500
r100 = 100
r50 = 50
r20 = 20
r10 = 10
r5 = 5
r2 = 2
r1 = 1
print('2000 rupee notes: ', topay // r2000)
topay = topay % r2000
print('500 rupee notes: ', topay // r500)
topay = topay % r500
print('100 rupee notes: ', topay // r100)
topay = topay % r100
print('50 rupee notes: ', topay // r50)
topay = topay % r50
print('20 rupee notes: ', topay // r20)
topay = topay % r20
print('10 rupee notes: ', topay // r10)
topay = topay % r10
print('5 rupee notes: ', topay // r5)
topay = topay % r5
print('2 rupee notes: ', topay // r2)
topay = topay % r2
print('1 rupee notes: ', topay // r1)

    

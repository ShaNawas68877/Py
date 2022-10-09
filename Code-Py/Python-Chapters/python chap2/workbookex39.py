# Exercise 39 : Sound levels
db = int(input('Enter the sound level in dB: '))
if db == 130:
    top = "It is Jackhammer noise"
elif db == 106:
    top = "It is Gas lawnmower noise"
elif db == 70:
    top = "It is Alarm clock nois"
elif db == 40:
    top = "It is a Quiet room"
elif db > 130:
    top = "It is higher than jackhammer noise"
elif db < 40:
    top = "No noise"
elif db < 130 and db > 106:
    top = "Noise level is in between Jackhammer and Gas lawnmower"
elif db < 106 and db > 70:
    top = "Noise level is in between Gas lawnmower and Alarm clock"
elif db < 70 and db > 40:
    top = "Noise level is in between Alarm clock and Quiet room"
print(top)

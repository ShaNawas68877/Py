# Exercise 41 : Note to frequency       #challenging program , Alhamdulillah completed successfully only with the hint
n = str(input('Enter the note: '))
s = n[:1]                               #It holds the albhabet in the note
if n == 'C4' or s == 'C':
    t = 261.63
elif n == 'D4' or s == 'D':
    t = 293.66
elif n == 'E4' or s == 'E':
    t = 329.63
elif n == 'F4' or s == 'F':
    t = 349.23
elif n == 'G4' or s == 'G':
    t = 392.00
elif n == 'A4' or s == 'A':
    t = 440.00
elif n == 'B4' or s == 'B':
    t= 493.88
#print(t)
       #Hint: To complete this exercise you will need to extract individual characters
                #from the two-character note name so that you can work with the letter and theoctavenumberseparately.Onceyouhaveseparatedtheparts,computethe frequency of
                #the note in the fourth octave using the data in the table above. Then divide the frequency by 24−x, where x is the octave number entered by the user.
                #This will halve or double the frequency the correct number of times.
p = int(n[1:])  #It holds the integer of the note
if p > 8:
    print('Wrong note : Error')
d = t / 2**(4-p)    # This calculates the notes frequency by taking middle values i.e, 4 values
print(d)
#print(t)
#print(p)
#print(s)

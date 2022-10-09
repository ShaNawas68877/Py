#fun program copies image n number of times in a folder
import os, shutil
a = 1
while a != 25:
    shutil.copy('C://Users//Shanawas//Desktop//cartoon_birds_blue_flying_animation_clipart.gif','C://Users//Shanawas//Desktop//copiiies//00'+str(a)+'.gif')
    a = a + 1
print('done')

#Using Pickle to write Binary Files

#Pickle for serialization and de-serialization - not good for big files though - for which we use Shelves
import pickle
'''
import pickle
imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, 'Pulling the Rug'),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town Waltz")))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

with open("imelda.pickle", "rb") as Imelda_pickled:
    imelda2 = pickle.load(Imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

'''
##
##import pickle
##imelda = ("More Mayhem",
##          "Imelda May",
##          "2011",
##          ((1, 'Pulling the Rug'),
##           (2, "Psycho"),
##           (3, "Mayhem"),
##           (4, "Kentish Town Waltz")))
##
##even = list(range(0,10,2))
##odd = list(range(1,10,2))
##
##with open("imelda.pickle", "wb") as pickle_file:
##    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
##    pickle.dump(even, pickle_file, protocol=0)
##    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
##    pickle.dump(2998302, pickle_file)
##
##with open("imelda.pickle", "rb") as Imelda_pickled:
##    imelda2 = pickle.load(Imelda_pickled)
##    even_list = pickle.load(Imelda_pickled)
##    odd_list = pickle.load(Imelda_pickled)
##    x = pickle.load(Imelda_pickled)
##
##print(imelda2)
##
##album, artist, year, track_list = imelda2
##
##print(album)
##print(artist)
##print(year)
##for track in track_list:
##    track_number, track_title = track
##    print(track_number, track_title)
##
##print("="*40)
##
##for i in even_list:
##    print(i)
##
##print("="*40)
##
##for i in even_list:
##    print(i)
##
##print("="*40)
##
##print(x)



#SHOULD NOT USE A PICKLED FILE FROM AN UNTRUSTED SOURCE, THE ABOVE CREATED BINARY FILE FILE
#CAN BE DELETED BY RUNNING THE BELOW CODE

##pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")

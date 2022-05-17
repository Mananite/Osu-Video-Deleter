import os 
import time
import sys
osu_songs_folder = "" #Remember to add the \Songs after osu, otherwise it won't work, don't bother if you didn't change the install location
delfiles = [] #Define empty list to do stuff later

if os.path.exists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\osu!\\Songs") == False: #default osu install location
	pass
if os.path.exists(osu_songs_folder)==False: #gets custom osu folder
	print("Set your songs folder")
	time.sleep(5)
	sys.exit()
print("""Shouldn't be longer than 5 mins (maybe)""")

if osu_songs_folder != "":
	xdw = os.walk(osu_songs_folder) #gets all mp4 files
else:
	xdw = os.walk(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\osu!\\Songs") #gets all mp4 files

for root, dirs, files in xdw: #iterate thru all the files in your osu songs folder
	for file in files:
		if file.endswith(".mp4"):delfiles.append(os.path.join(root,file)) #if file is a mp4, add it to a list
		else:pass

print(f"Bouta delete {len(delfiles)} files")
for i in range(len(delfiles)):
	os.remove(delfiles[i]) #delete the .mp4 files
print("We're done")
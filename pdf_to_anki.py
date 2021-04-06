import pdf2image
from pdf2image import convert_from_path as cfp
import ntpath
import cv2
import os
import time
from glob import glob


try:
	os.mkdir("images")
except:
	pass

try:
	os.mkdir("images_final")
except:
	pass
	
def convert_to_image(path_to_pdf , deck_name):
	print("Devolped by ")
	print("      @@@       @@@.        @@@.   @@@@@@@@@@&     @@   @@@@@@@@@@@@@   ")
	print("     @@@@%      @@@@       @@@@.   @@        @@#   @@        @@         ")
	print("    @@  @@,     @@ @@     %@ @@.   @@        @@/   @@        @@         ")
	print("   @@    @@     @@  @@    @( @@.   @@@@@@@@@@/     @@        @@         ")  
	print("  @@@@@@@@@@    @@   @@  @@  @@.   @@        @@    @@        @@         ")
	print(" @@        @@   @@    @@@@   @@.   @@        @@    @@        @@         ")
	print(" @@        @@   @@    @@@@   @@.   @@        @@    @@        @@         ")
	print("[So that he can be spare himself from AKSHDEEP's tourture!] ")
	print()
	print()
	print()
	print("Starting to load pdf")
	images = cfp(path_to_pdf)
	print("pdf loaded to memory")

	for i in range(len(images)):
		images[i].save("./images/" +deck_name + str(i) + str(time.time()) + ".jpg" , "JPEG" )
		if i % 10 == 0:
			print("saved" , i)


convert_to_image( "sample.pdf" , "deck_name" )


file_list = glob('./images/*.jpg')
#print(file_list)

rand_int = time.time()
rand_int = round(rand_int)


complete_list = []



direct_copy = True


for filename in file_list: 
	image = cv2.imread(filename)

	def crop_doublet_anki_notes(image , x , y):
		a = int(x*(image.shape[0])/(x+y))
		img1 = image[ 0:a , 0:image.shape[0]]
		img2 = image[ a:image.shape[0] , 0:image.shape[0] ]
		return(img1 , img2 )

	img1 , img2 = crop_doublet_anki_notes(image , 14,13.5)

	#print(img1)
	#print(type(img1))
	filename = ntpath.basename(filename)

	a1 = filename[0:-4] + str(rand_int) + "_01" + ".jpg"
	a2 = filename[0:-4] + str(rand_int) + "_02" + ".jpg"
	name1 = "<img src='" + a1 + "'>"
	name2 = "<img src='" + a2 + "'>"
	cv2.imwrite( "./images_final/" + a1 , img1)
	cv2.imwrite("./images_final/" + a2 , img2) 
	#print("./images_final/" + a1 )
	
	complete_list.append([name1 , name2])

import pandas as pd
df = pd.DataFrame(complete_list)
#print(df)

df.to_csv("output.csv", index = None,header=False)
#Use this Output.csv file to load the anki deck to Anki software.

#Before loading the CSV file, copy the images generated in images_final folder to following path - 
# "./home/$$$$$YOUR USER NAME$$$$$$$$/.local/share/Anki2/User 1/collection.media/"     # in Ubuntu 
# e.g.  "./home/amrit/.local/share/Anki2/User 1/collection.media/"




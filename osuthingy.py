import os
import glob
import shutil

def copyMp3 ( src, dest):
	fileDir = [i for i in glob.glob(src + "\\Songs\\*\\*.mp3")]
	print(len(fileDir))
	for i in range(0,len(fileDir)):
		shutil.copyfile(fileDir[i],os.path.join(dest,os.path.split(fileDir[i])[1]))
		os.system('cls')
		print("Copying " + os.path.split(fileDir[i])[1])
		print("Copying %s"%(round((i/len(fileDir))*100,2)) + "% complete")
	print("Copying complete")


copyMp3('C:\\Program Files (x86)\\osu!','C:\\Users\\Sayed\\Desktop\\Songs')
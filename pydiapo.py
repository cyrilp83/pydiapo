import tkinter as Tk
import glob
import time
from PIL import ImageTk, Image
 
root = Tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

listeimage = []
j = 0
lbl = Tk.Label(root)

def souris(event):
    clic = event.keysym
    root.destroy()
lbl.focus_set()
lbl.bind("<Button-1>", souris)

## chargement de toutes les images dans une liste
def loadlist():
	global listeimage
	for i in glob.glob('./samples/*.*'):
		image = Image.open(i) 
		hratio = (h/float(image.size[1]))
		wsize = int((float(image.size[0]*float(hratio))))
		image = image.resize((wsize,h))
		photo = ImageTk.PhotoImage(image) 
		listeimage.append(photo)
	
 
## affichage des images
def diapo():
	jmax=len(listeimage)
	global j
	lbl.config(image = listeimage[j])
	j+=1
	time.sleep(5)
	if j < jmax:
		root.after(100, diapo)
	else:
		loadlist()
		root.after(100,diapo)
	

lbl.pack()
loadlist()
root.after(100, diapo)
root.mainloop()

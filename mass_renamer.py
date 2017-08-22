import glob
import os
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

ext = input('extension (e.x: .txt): ')
path = filedialog.askdirectory(title='Choose directory') + '/*'
filelist=sorted(glob.glob(path))
i=1

for oldname in filelist:
    if os.path.isfile(oldname):
        basepath=os.path.split(oldname)[0]
        newname=os.path.join(basepath, "{}{}".format(str(i), ext))
        i=i+1
        print("Renaming {} to {}".format(oldname, newname))
        os.rename(oldname, newname)

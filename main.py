from url import *
from gui import *
import stat

dataFolderPath = os.path.join(os.getcwd(), "Data_Sheets")
print(dataFolderPath)
if not os.path.isdir(dataFolderPath):
    os.mkdir(os.path.join(os.getcwd(),"Data_Sheets"))
    
os.chmod(dataFolderPath, stat.S_IWOTH)
os.chmod(dataFolderPath, stat.S_IXGRP)
os.chmod(dataFolderPath, stat.S_IRWXU)
os.chmod(dataFolderPath, stat.S_IRWXG)
    
createGUI()
#getURLInput()

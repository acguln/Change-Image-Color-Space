import sys
import os
import time
from PIL import Image
from PIL.ImageCms import profileToProfile

files = sys.argv[1]#drag and drop
if os.path.exists(files):
    filename = os.path.basename(files)
    DisplayP3_PROFILE = "icc/DisplayP3-v4.icc"
    Acer_X27_PROFILE = "icc/Acer_X27.icm"
    SRGB_PROFILE = "icc/sRGB.icm"

    #img_path = "c.png"
    oldImg = Image.open(sys.argv[1])

    newImg = profileToProfile(oldImg, Acer_X27_PROFILE,  DisplayP3_PROFILE)# path before after
    newImg_path = "DisplayP3_"+filename
    newImg.save(newImg_path)

    print(filename+" change successfully!")
    time.sleep( 2 )


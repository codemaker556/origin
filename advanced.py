import sys
import wget
import basc_py4chan
import requests 
import os,ntpath
import re
import pprint
import time
import ntpath

def main():
    
    mylist = []     #create an empty list
    s = basc_py4chan.Board('hr')
    thread = s.get_thread(4038558)
    dest_folder = os.path.realpath("C:\Users\Lukas\Desktop\fit\Whamen")
    xxx = set(os.listdir(dest_folder))
    for file in thread.files():
        #print(file)
        mylist.append(str(file))  
    
    converter=set(mylist)   #turns list into set 
    new_set = set()
    for item in converter:
        downloadable = item.replace("http://i.4cdn.org/hr/", "")
        new_set.add(downloadable)   #turns strings back into set
        # print(downloadables)
        # print(type(downloadable)) 
    pp = pprint.PrettyPrinter(width=41, compact=True)
    
    matches = new_set & xxx
    pp.pprint(matches)
    #print(xxx)
    
    for match in matches:
        new_set.remove(match)
        print(" removing %s" % match)

    pp.pprint(new_set)    #print out things that need downloading
   
    my_list = list(new_set)  #turn back into list
    string = "http://i.4cdn.org/hr/"   #make things into links
    my_new_list = [string + x for x in my_list]

    for pics in my_new_list:
        print(" attempting to download %s" % pics)
        image_filename = wget.download(pics, out=dest_folder)
        print('Image Successfully Downloaded: ', image_filename)
        time.sleep(2)

   

main()
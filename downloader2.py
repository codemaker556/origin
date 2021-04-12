import sys
import wget
import basc_py4chan
import requests 
import os
import re
import pprint
import time
import argparse

# Create the parser
my_parser = argparse.ArgumentParser(description='Download images from 4chan')

# Add the arguments
my_parser.add_argument('--thread',
                       #metavar='[-t] <thread number>',
                       type=int,
                       required=True,
                       help='Replace THREAD with the number of the thread in 4chan')

# Execute the parse_args() method
args = my_parser.parse_args()

thread_id = args.thread

print(thread_id)

def main():
    
    mylist = []     #create an empty list
    s = basc_py4chan.Board('s')
    print(thread_id)
    print(s)
    thread = s.get_thread(thread_id)
    print('the thread of s board is:', thread)
    dest_folder = os.path.realpath("/home/jonpu/4chan/images")
    print(dest_folder)
    xxx = set(os.listdir(dest_folder))
    for file in thread.files():
        print(file)
        mylist.append(str(file))  
    
    converter=set(mylist)   #turns list into set 
    new_set = set()
    for item in converter:
        downloadable = item.replace("http://i.4cdn.org/s/", "")
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
    string = "http://i.4cdn.org/s/"   #make things into links
    my_new_list = [string + x for x in my_list]

    for pics in my_new_list:
        print(" attempting to download %s" % pics)
        image_filename = wget.download(pics, out=dest_folder)
        print('Image Successfully Downloaded: ', image_filename)
        time.sleep(2)
   

main()
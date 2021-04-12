import sys
import wget
import basc_py4chan
import time
import requests 


def main():
    mylist = []
    s = basc_py4chan.Board('s')
    thread = s.get_thread(20593800)
    for file in thread.files():
        print(file)
        mylist.append(str(file)) # turns output into list so I could run for loop 

    for pics in mylist:
        image_filename = wget.download(pics)
        #time.sleep(5) #waits for 2 secs between every download because it crashes otherwise
        print('Image Successfully Downloaded: ', image_filename)

main()
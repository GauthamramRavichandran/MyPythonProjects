'''
    Name         :  TV Serials downloader
    Author       :  R Gautham Ram
    Tested on    :  Python 2.7
    Date created :  23 Sep 17
    Description  :  Opens a webpage for downloading tv serials
'''
    
import webbrowser as wb
from bs4 import BeautifulSoup as bs
import urllib

Base_URL=['http://dl2.my98music.com/Data/Serial/','http://dl.funsaber.net/serial/','http://dl.my-film.in/serial/','http://dl.dlfile.pro/2/','http://46.4.238.69/Series/','http://dl3.downloadoo.site/Tvshow/','http://dl2.film2movie.biz/serial/','http://dl2.downloado.site/dl2/TV%20Show/']

def main():
    tv=raw_input('Enter the name of the series(as such):')
    tv=tv.title()
    tv1=tv.replace(" ","%20")  #Default
    tv2=tv.replace(" ","-")    #Used only for some sites depending on their configurations
    ext=tv1
    i=-1
    found=0
    while(i<len(Base_URL)-1):
        i+=1
        ext=tv2 if i==4 else tv1
        '''Here,5th element in the list takes " "(space) as "-"(Hypen).While others take "%20" which is default'''
        URL=Base_URL[i]+ext
        a=urllib.urlopen(URL)
        rcode=a.getcode()
        if(rcode==404):
            continue
        else:
            print("Found your series -"+tv)
            wb.open_new_tab(URL)
            found=1
            break
    if(found==0):
        print("The requested series "+tv+" is not found")

if __name__ == '__main__':
    main()

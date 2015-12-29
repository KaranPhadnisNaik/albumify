#! /usr/bin/env python



#input is a single search querry
import os
import urllib2
import urllib
import json
import sys



def main():

#    if sys.argc != 2:
#       return("Incorrect number of arguments")

    #check for the number of arguemnts and check for the only argument is
    # a valid string
    
    

    url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"

    song = sys.argv[1]
    artist = sys.argv[2]

    query = song+" "+artist+" song youtube"
    video_URLS =[]
    video_ID = []
    query = urllib.urlencode( {'q' : query } )
    response = urllib2.urlopen (url + query ).read()
    data = json.loads ( response )
    results = data [ 'responseData' ] [ 'results' ]
    for result in results:
        #title = result['title']
        url = result['url']
        video_URLS.append(url)

    
    #now convert the URLS to yt video IDs
    for video in video_URLS:
        video = video[-11:]
        video_ID.append(video)
        #print video                       #remove

    song_URL="https://www.youtube.com/watch?v="+video_ID[0]
    print song_URL

    getmp3_cmd = "youtube-dl --extract-audio --audio-format mp3 "+song_URL
    
    os.system(getmp3_cmd)


if __name__ == "__main__":
    main()

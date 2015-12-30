#Albumify
  * Purpose: extract mp3 files from yotube through user input and organize them into an album OR simply extract a single song
  * Dependencies: __youtube-dl__, MORE TO COME

#Setup/Usage
* Clone repo and cd into directory
* To get single song:
```
	$ cd Albumify
	$ ./albumify "Often" "Weeknd"
```
* Getting a complete album:
```
	$ cd Albumify
	$ ./albumify -A "To Pimp a Butterfly" "Kendrick Lamar" tracks.txt
```
	

#Track Log / File description:
* search.py:
  * takes in song name and artist name as a querry 
  * gets the FIRST youtube URL via google search
  * the yt hash ID is found then processed and concatenated to the main youtube video url
  * calls youtube dl to specifiy the download of an mp3 file from the extracted url
* albumify:
  * == main program
  * has 2 options:
    * -h		contains help information
    * -A 		specifies the first media entry is an Album title
  * NEED TO DO:
    * query tracklist from Musicbrainz
    * query potential other metadata (song features, length)
* tracks.txt:
    * contains a list of track names from the corresponding input album name
    * ONLY temporary (this file will be removed when integration with musicbrainz api is complete)
      
# Todo
* write python script that will fully process and input the meta data into the mp3 files
* further test potential arguments
	    

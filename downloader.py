from pytube import YouTube
import sys
#print("Starting...")
links = sys.argv[1].split(',')
#print("Argument 1 Found")
filenamee = sys.argv[2]
#print("Argument 2 Found")
#print("Link valid")
#print("Downloading...")
for i in range(links.__len__()):
    ytVideo = YouTube(links[i])
    ytVideo.streams.get_highest_resolution().download('./',filename=f'{filenamee}{i}.mp4')
print("Done!")

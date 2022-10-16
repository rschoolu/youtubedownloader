from pytube import YouTube
import sys
def main():
    if sys.argv[1] == "help":
        print("Syntax: py downloader.py [yt_link] [output_name] [audio_only 0/1]")
        return
    #print("Starting...")
    links = sys.argv[1].split(',')
    #print("Argument 1 Found")
    filenamee = sys.argv[2]
    #print("Argument 2 Found")
    #print("Link valid")
    #print("Downloading..."
    for i in range(links.__len__()):
        ytVideo = YouTube(links[i])
        name = f'{filenamee.split(".")[0]}{i}.{filenamee.split(".")[1]}'
    print("Done!")
    return
# main function woohoo not retarded anymore!
main()
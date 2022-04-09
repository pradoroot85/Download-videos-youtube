from pytube import YouTube, streams

url = input(str('Colé ou digite uma url:'))

video = YouTube(url)
stream = video.streams.get_highest_resolution()
stream.download()
 

import youtube_dl
import argparse

''' Read/parse arguments from commandline'''

parser = argparse.ArgumentParser()
parser.add_argument(
    '--url',
    '-url',
    default='',
    help='Full URL of video. \n Ex: https://www.youtube.com/watch?v=iG9CE55wbtY')

input_arguments = parser.parse_args()


youtube_downloader = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

with youtube_downloader:
    result = youtube_downloader.extract_info( input_arguments.url )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

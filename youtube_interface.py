from ytmusicapi import YTMusic
from pyfzf.pyfzf import FzfPrompt
import yt_dlp
import json

ytmusic = YTMusic("oauth.json")

def select_song_from_home():
    entry_bundle = {}
    for entry in ytmusic.get_home():
        header = entry["title"].upper()
        #if header != "MIXED FOR YOU":
            #print(header + "\n==============")
        for sub_entry in entry["contents"]:
            if header == "LISTEN AGAIN":
                try:
                    #TODO: generate song radio instead
                    url_out = "https://music.youtube.com/watch?v=" + str(sub_entry["videoId"]) + "&list=" + str(sub_entry["playlistId"]) 
                    song_rep = "[" + sub_entry["artists"][1]["name"] + "] " + sub_entry["title"]
                    #print(link(url_out, song_rep))
                    entry_bundle[song_rep] = url_out
                except IndexError:
                    pass
                except KeyError:
                    pass
            elif header == "QUICK PICKS":
                qp_output = "[" + sub_entry["artists"][0]["name"] + "] " + sub_entry["title"]
                #print(qp_output)
                #TODO: construct links from json information
                qp_url = ""
                entry_bundle[qp_output] = qp_url
            elif header == "MIXED FOR YOU":
                pass
                #print("  " + sub_entry["title"])
        #print("\n")
    fzf = FzfPrompt()
    f_return= fzf.prompt(list(entry_bundle.keys()))
    #download_songs([entry_bundle[f_return[0]]])

def download_songs(URLS):
    '''
    URLS: list of urls to download
    '''
    ydl_opts = {
        'format': 'wav/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)

def search_for_song(query):
    print(ytmusic.search(query))

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

query = input("Enter Song\n")
search_for_song(query)
#mask_off = "https://www.youtube.com/watch?v=aWb8z-KhZdo" 
#download_songs([mask_off])
#select_song_from_home()
#print(link("www.google.com", "google"))
#print(link("www.google.com", "   [DJ Snake] U Are My High"))

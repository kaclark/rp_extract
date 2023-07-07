from ytmusicapi import YTMusic
ytmusic = YTMusic("oauth.json")

def get_home():
    for entry in ytmusic.get_home():
        header = entry["title"].upper()
        if header != "MIXED FOR YOU":
            print(header + "\n==============")
        for sub_entry in entry["contents"]:
            if header == "LISTEN AGAIN":
                try:
                    url_out = "https://music.youtube.com/watch?v=" + str(sub_entry["videoId"]) + "&list=" + str(sub_entry["playlistId"]) 
                    song_rep = "[" + sub_entry["artists"][1]["name"] + "] " + sub_entry["title"]
                    print(link(url_out, song_rep))
                except IndexError:
                    pass
                except KeyError:
                    pass
            elif header == "QUICK PICKS":
                print("[" + sub_entry["artists"][0]["name"] + "] " + sub_entry["title"])
            elif header == "MIXED FOR YOU":
                pass
                #print("  " + sub_entry["title"])
        print("\n")

def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)


get_home()
#print(link("www.google.com", "google"))
#print(link("www.google.com", "   [DJ Snake] U Are My High"))

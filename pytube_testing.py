from pytube import Playlist

def get_song_urls(playlist_url):
    p = Playlist(playlist_url)
    for url in p.video_urls:
         print(url)

#get song urls of random playlist found on youtube
get_song_urls("https://music.youtube.com/playlist?list=PL4d9vbZS8dO2AWjvNt3YvXZB0eDxdHX7Y&feature=share")
'''
https://www.youtube.com/watch?v=XqJosdWocto
https://www.youtube.com/watch?v=U2TPS-9oMtc
https://www.youtube.com/watch?v=q5go1dovoeM
https://www.youtube.com/watch?v=Wz_5AFguGCU
https://www.youtube.com/watch?v=yfrEMQgBc2Y
https://www.youtube.com/watch?v=NxxjLD2pmlk
https://www.youtube.com/watch?v=vgOTxZtlXys
https://www.youtube.com/watch?v=Ao81ziiXHhs
https://www.youtube.com/watch?v=MMitS8NgJHs
https://www.youtube.com/watch?v=CJe2qhAJjWM
https://www.youtube.com/watch?v=O5xwx_QzEFw
https://www.youtube.com/watch?v=yGHrBwQfsZM
https://www.youtube.com/watch?v=w4jOhmwZVAE
https://www.youtube.com/watch?v=lcX37Pzobxw
https://www.youtube.com/watch?v=WySekulZAoY
https://www.youtube.com/watch?v=15RuCIbXE8A
https://www.youtube.com/watch?v=_f1ypDfvjgM
https://www.youtube.com/watch?v=vXw6p08PrrY
https://www.youtube.com/watch?v=Istt2aXmWFg
https://www.youtube.com/watch?v=vtU3RchHf0E
https://www.youtube.com/watch?v=yHcBymQiNyU
https://www.youtube.com/watch?v=bId_8k1gfjA
https://www.youtube.com/watch?v=6Q9JSgxYLm0
'''

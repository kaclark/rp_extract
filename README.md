https://github.com/tuwien-musicir/rp_extract<br/>
===============================<br/>
Rennovated by: Keanu Clark<br/><br/>
This project was written in Python 2. I am porting this to work on termux for a pixel 6, meaning fortran in scipy will not work.<br/> 
I have imported numpy in place of scipy wherever I could. Scipy source code has been spliced in -- Luckily all normal python. Sklearn has been abandoned<br/>
The data analysis seems to proceed as it should, but I don't really have control data<br/>
As a result, I now need to look at a bunch of data and also find a way to collect songs from playlists generated from an inital song<br/>
The goal is that something in a pattern extracted from the data can filter or partition the playlist. Human input will probably be used for reinforcment learning<br/>
How to extract alluring features of songs and search through arbitrary playlists for matching motifs?<br/>
===============================<br/><br/>

Goals:<br/>
[ ] (Data Logs) Automate Slides; output folder of analysis<br/>
[x] Full YouTube Music API functionality secured<br/>
[x] (Search Function) Find way of interacting with youtube playlists<br/>
[x] Test Powerpoint output, load in google slides app<br/>
[x] Youtube Playlist song url retrieval<br/>
[x] Download youtube song in .wav format from url<br/>
[x] Plot Data<br/>
[x] Figure out Data<br/>
[x] Clean up files; delete what is not needed<br/>
[x] Python 3 syntax conversion<br/>
[x] scipy to numpy conversion<br/>
[x] Test load_audiofile.py<br/>
[x] Test rp_extract.py<br/>

===============================<br/>
Original Project Info<br/>
===============================<br/><br/>
RP_extract:<br/>
Rhythm Pattern Audio Feature Extractor<br/>
for Music Similarity, Music Classification and Music Recommendation<br/>

created by:

TU Wien<br>
[Music Information Retrieval Group](http://ifs.tuwien.ac.at/mir)<br>
Institute of Software Technology and Interactive Systems<br>
Vienna University of Technology, Austria

RP_extract is a Python library to extract semantic features (so called audio descriptors) from audio files (WAV, MP3, ...)
which can be used in tasks such as finding similar sounding music, creating playlists or recommender systems,
categorizing music into a custom set of categories such as genres, and detecting concepts such as moods and emotions in music.
Most of these tasks are achieved through employing Machine Learning, example implementations are provided in this
repository and the tutorials included.

Main Authors: Thomas Lidy (audiofeature), Alexander Schindler (slychief)


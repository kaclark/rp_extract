from rp_extract import *
from audiofile_read import *
from rp_plot import *

audiofile = "../../songs/Future_You_Are_My_High.wav"
samplerate, samplewidth, wavedata = audiofile_read(audiofile)
extracted_features = rp_extract(wavedata,                            # the two-channel wave-data of the audio-file
                                samplerate,                          # the samplerate of the audio-file
                                extract_rp          = True,          # <== extract this feature!
                                transform_db        = True,          # apply psycho-accoustic transformation
                                transform_phon      = True,          # apply psycho-accoustic transformation
                                transform_sone      = True,          # apply psycho-accoustic transformation
                                fluctuation_strength_weighting=True, # apply psycho-accoustic transformation
                                skip_leadin_fadeout = 1,             # skip lead-in/fade-out. value = number of segments skipped
                                step_width          = 1)
plotrp(extracted_features['rp'], savefp="../You_are_my_high_rp.png")

#This Equalizer can produce a filtered file with name new_file1.flac this can played using external playeys
#There are four equalizer buttons that can either be set high or low
#equlizer inputs are given like 0010, 0110 etc after running codes

import soundfile as sf
import sounddevice as sd
from matplotlib import pyplot as plt
import numpy as np
import filters as f

#reads the music
sig, fs = sf.read('recordings/s1.pcm', channels=2, samplerate=48000,format='RAW', subtype='PCM_16')

start_point=1
total_len=400000

ch1=[]
ch2=[]

# reduces and divides the file into two channal
for i in range(start_point,start_point+total_len):
	ch1.append(sig[i][0])
	ch2.append(sig[i][1])
	#print(ch1)
#sd.play(ch1,fs)

method = "SWITCHES"

if (method=="SWITCHES"):
	print("Please Enter the input of equalizer in binary form like 0100 or 0011")
	buttons = input()
# each switch represent (0-2500) (2500-5000) (5000-7500) (7500-)

	if buttons== "0011":
		#HIGHPASS FILTER REQUIRED
		filtered = f.fir_high_pass(ch1,fs,5000,419,np.float64)
		sf.write('new_file1.flac', filtered*2, fs)
	elif buttons=="1100":
		#LOWPASS FILTER REQUIRED
		filtered = f.fir_low_pass(ch1,fs,5000,419,np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="1000":
		#LOWPASS FILTER REQUIRED
		filtered = f.fir_low_pass(ch1,fs,2500,419,np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons== "0001":
		#HIGHPASS FILTER REQUIRED
		filtered = f.fir_high_pass(ch1,fs,7500,419,np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
			#sf.write("n1.pcm",filtered, fs,subtype='PCM_16')
		#data = sf.read('n1.pcm', fs, subtype='PCM_16')
		#sd.play(data, fs)
	elif buttons=="0100":
		#BANDPASS FILTER REQUIRED
		filtered = f.fir_band_pass(ch1, fs, 2500, 5000, 419, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="0010":
		# BANDPASS FILTER REQUIRED
		filtered = f.fir_band_pass(ch1, fs, 5000, 7500, 419, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="1001":
		#BANDREJECT FILTER REQUIRED
		filtered = f.fir_band_reject(ch1, fs, 2500, 7500, 419, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="1010":
		#TWO REJECTIONS WILL BE REQUIRED
		filtered = f.fir_band_reject(ch1, fs, 2500, 5000, 419, 419, np.float64)
		filtered = f.fir_low_pass(filtered, fs, 7500, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="0110":
		# BANDPASS FILTER REQUIRED
		filtered = f.fir_band_pass(ch1, fs, 2500, 7500, 419, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="0101":
		# TWO REJECTIONS WILL BE REQUIRED
		filtered = f.fir_band_reject(ch1, fs, 5000, 7500, 419, 419, np.float64)
		filtered = f.fir_high_pass(filtered , fs, 2500,419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="1110":
		filtered = f.fir_low_pass(ch1, fs, 7500, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="1101":
		filtered = f.fir_band_reject(ch1 , fs, 5000, 7500, 419, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="1011":
		filtered = f.fir_band_reject(ch1 , fs, 2500, 5000, 419, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="0111":
		filtered = f.fir_high_pass(ch1 , fs, 2500, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="0000":
		filtered = f.fir_low_pass(ch1, fs, 7500, 419, np.float64)
		filtered = f.fir_band_reject(ch1, fs, 0, 7500, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	elif buttons=="1111":
		filtered = f.fir_high_pass(ch1, 0, 419, np.float64)
		sf.write('new_file1.flac', filtered * 2, fs)
	else:
		print("Invalid input: please enter correct value")
print("Processed file saved as new_file.flac and can be played using external flac player")
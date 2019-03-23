import os
import sys

destination_folder = 'mono_wav_audio'
audio_file = sys.argv[1]

def convert_n_tune(audio_file):
	# ffmpeg -i 111.mp3 -acodec pcm_s16le -ac 1 -ar 16000 out.wav
	new_audio = os.path.splitext(os.path.split(audio_file)[1])[0] + '.wav'
	new_audio = os.path.join(destination_folder, new_audio)
	cmd = 'ffmpeg -i ' + audio_file + ' -acodec pcm_s16le -ac 1 -ar 16000 ' + new_audio
	os.system(cmd)

if not os.path.exists(destination_folder):
	os.makedirs(destination_folder)

print(audio_file)
if os.path.exists(audio_file):
	if ' ' in audio_file:
		audio_file = audio_file.replace(' ', '_')
		os.rename(sys.argv[1], audio_file)
	convert_n_tune(audio_file)


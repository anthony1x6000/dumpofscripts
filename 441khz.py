import os
import subprocess

input_dir = input("indir")
output_dir = input_dir + "/wav"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in os.listdir(input_dir):
    if file.endswith(".wav"):
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, f"{os.path.splitext(file)[0]}_44.1khz.wav")
        subprocess.run(["ffmpeg", "-i", input_file, "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", output_file])

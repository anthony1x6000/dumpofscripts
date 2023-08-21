import os
import subprocess

directory = input("enter directory")
extension = input("file extension with period (.mp3, .flac)")
try: 
    os.mkdir(directory + '/wav/')
except:
    print("/wav/ already exists probably")

for filename in os.listdir(directory):
    if filename.endswith(extension):
        input_path = os.path.join(directory, filename)
        output_path = os.path.join(directory + '/wav/', os.path.splitext(filename)[0] + '.wav')
        subprocess.run(['ffmpeg', '-i', input_path, '-ac', '2', output_path])

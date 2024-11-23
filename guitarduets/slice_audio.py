from pydub import AudioSegment
import os

# slices long audio files into shorter clips

INPUT_PATH = "synth_mono"
OUTPUT_PATH = "synth_mono_3s"

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

clip_length = 3000 # in milliseconds

for dirpath, dirname, filenames in os.walk(INPUT_PATH):

    if dirpath is not INPUT_PATH:

        for f in filenames:

            file_path = os.path.join(dirpath, f)
            file = AudioSegment.from_wav(file_path)
            file_length = len(file)
            filename = os.path.splitext(f)[0]
            extension = os.path.splitext(f)[1]

            new_sub_dir = dirpath.split("\\")[-1]
            new_sub_dir = os.path.join(OUTPUT_PATH, new_sub_dir)
            if not os.path.exists(new_sub_dir):
                os.makedirs(new_sub_dir)

            i = 0
            while i < file_length:
                new_file = file[i:i+clip_length]
                new_filename = filename + '_' + str(int(i/clip_length)) + extension
                sliced_sound_path = os.path.join(new_sub_dir, new_filename)
                new_file.export(sliced_sound_path, format='wav')
                i += clip_length
                print(f"Exported {new_filename} to {new_sub_dir}")


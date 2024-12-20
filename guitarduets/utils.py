import soundfile as sf

def print_wav_info(audio_file):

    ob = sf.SoundFile(audio_file)
    print('Sample rate: {}'.format(ob.samplerate))
    print('Channels: {}'.format(ob.channels))
    print('Subtype: {}'.format(ob.subtype))

if __name__ == '__main__':
    print_wav_info('dataset/train/mono-pickup/00_BN1-129-Eb_solo_mix.wav')


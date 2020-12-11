# coding: utf-8
import os
import cv2
import sys
import numpy as np
from pydub import AudioSegment 
import moviepy.editor as mp


class Test:
    def __init__(self):
        # Set video names.
        #self.input_video = sys.argv[1]
        self.input_video = 'video1.mp4'
        #self.add_audio = sys.argv[2]
        self.add_audio = 'bomb1.mp3'


    def main(self):
        self.output_video = 'output.avi'
        self.make_video()
        self.set_audio()
        #os.remove('audio.mp3')
        #os.remove('output.avi')


    def make_video(self):
        # Get input video information.
        cap = cv2.VideoCapture(self.input_video)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        frame_num = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        play_time = int(frame_num / fps)

        print("WIDTH[pixel]:", width)       # 幅
        print("HEIGHT[pixel]:", height)     # 高さ
        print("FPS:", fps)                  # frame par second
        print("FRAME NUM:", frame_num)      # フレーム数
        print("PlAY TIME[sec]:", play_time) # 時間

        # Set output video infomation.
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #fourcc = cv2.VideoWriter_fourcc(*'MP4S')
        # Set the above information.
        vw = cv2.VideoWriter(self.output_video, fourcc, fps, (width, height))

        # Make the output video.
        print('Making a video...')
        while(True):
            ret, img = cap.read()
            if ret == True:
                # Flip
                img_flip = img #cv2.flip(img, 1) "frip horizonal"
                # Add frame
                vw.write(img_flip)
            else:
                break
            
        # Post processing.
        cap.release()
        cv2.destroyAllWindows()


    def set_audio(self):
        # Extract audio from input video.
        clip_input = mp.VideoFileClip(self.input_video).subclip()
        clip_input.audio.write_audiofile('audio.mp3')

        # 音声取得
        sound = AudioSegment.from_file('audio.mp3')
        plus_sound = AudioSegment.from_file(self.add_audio)

        # 音声を配列に
        sound_array = np.array(sound.get_array_of_samples())
        plus_sound_array = np.array(plus_sound.get_array_of_samples())
        
        #追加音声の長さ(int)
        plus_sound_time = int(plus_sound.duration_seconds)

        #sampling rate
        sr = plus_sound.frame_rate
        
        #print
        print("TIME[sec]:", plus_sound_time)
        print("ADD SAMPLING RATE[Hz]:", sr)
        print("SAMPLING RATE[Hz]:", sound.frame_rate)
   
        #元音声と同じ長さの配列を生成
        plus_sound_extend = np.zeros_like(sound_array)
        
        #追加音声を入れる時間
        start_time = 0

        #元動画の長さの追加音声
        plus_sound_extend[start_time*sr*2:(plus_sound_time+start_time*2)*sr] = plus_sound_array[:plus_sound_time*sr]

        #音声を重ねる
        sound_array = sound_array + plus_sound_extend

        #動画出力
        song = AudioSegment(sound_array.tobytes(), frame_rate=sound.frame_rate, sample_width=2, channels=2)
        song.export('audio.mp3', format="mp3")

        # Add audio to output video.
        clip_output = mp.VideoFileClip(self.output_video).subclip()
        clip_output.write_videofile(self.output_video.replace('.avi', '.mp4'), audio='audio.mp3')


Test().main()
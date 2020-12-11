import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    play_time = frame_num / fps
    print("fps:",fps)
    print("frame_num:",frame_num)
    print("play_time:",play_time)

    n = 0

    while True:
        ret, frame = cap.read()
        #frame=cv2.resize(frame,(450,750))
        frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
        #frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            print("n:",n)
            print("1枚あたりの時間:",play_time/n)
            print("1秒あたりの枚数:",n/play_time)
            return

save_all_frames('movie/clap1.avi', 'clap', 'clap', 'png')
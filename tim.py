import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    play_time = frame_num / fps
    
    global n
    global ttime
    n=0
    while True:
        ret, frame = cap.read()
        #frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
        frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(5), ext), frame)
            n += 1 #nは画像になった枚数
        else:
            time=play_time/n
            ttime='{:.3f}'.format(time)
            break

def count():
    return n

def second():
    return ttime


save_all_frames('sample.MOV', 'sample-photo', 'sample', 'png')
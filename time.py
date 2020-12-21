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

    n = 0

    while True:
        ret, frame = cap.read()
        #frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
        frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            time=play_time/n
            ttime='{:.3f}'.format(time)
            return

save_all_frames('sample.MOV', 'sample-photo', 'sample', 'png')
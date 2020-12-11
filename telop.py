import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

# 画像に文字を入れる関数
def telop(img, message, W, H):
    font_path = 'C:\Windows\Fonts\meiryo.ttc'        # Windowsのフォントファイルへのパス
    font_size = 24                                   # フォントサイズ
    font = ImageFont.truetype(font_path, font_size)  # PILでフォントを定義
    img = Image.fromarray(img)                       # cv2(NumPy)型の画像をPIL型に変換
    draw = ImageDraw.Draw(img)                       # 描画用のDraw関数を用意

    w, h = draw.textsize(message, font)              # .textsizeで文字列のピクセルサイズを取得

    # テロップの位置positionは画像サイズと文字サイズから決定する
    # 横幅中央、縦は下
    position = (int((W - w) / 2), int(H - (font_size * 1.5)))

    # 中央揃え
    #position = (int((W - w) / 2), int((H - h) / 2))

    # テキストを描画（位置、文章、フォント、文字色(BGR+α)を指定）
    draw.text(position, message, font=font, fill=(255, 255, 255, 0))

    # PIL型の画像をcv2(NumPy)型に変換
    img = np.array(img)
    return img

# 動画を読み込み1フレームずつ画像処理をする関数
def m_slice(path, dir, step, message):
    in_path = os.path.join(*[dir, path])                # 読み込みパスを作成
    out_path = os.path.join(*[dir, 'out_' + path])      # 書き込みパスを作成
    movie = cv2.VideoCapture(in_path)                   # 動画の読み込み
    Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))       # 動画の全フレーム数を計算
    fps = movie.get(cv2.CAP_PROP_FPS)                   # 動画のFPS（フレームレート：フレーム毎秒）を取得
    W = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))        # 動画の横幅を取得
    H = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))       # 動画の縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # 動画保存時のfourcc設定（mp4用）

    # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    video = cv2.VideoWriter(out_path, fourcc, int(fps / step), (W, H))
    ext_index = np.arange(0, Fs, step)  # 動画から静止画（フレーム）を抽出する間隔

    j = 0                               # message配列から文章と時間を抜き出す指標番号
    section = message[j]                # フレームに書き込む文章と時間の初期値
    for i in range(Fs):                 # フレームサイズ分のループを回す
        print(i)
        flag, frame = movie.read()      # 動画から1フレーム読み込む
        check = i == ext_index          # 現在のフレーム番号iが、抽出する指標番号と一致するかチェックする
        time = i / int(fps/step)        # 抽出したフレームの動画内経過時間

        if flag == True: # フレームを取得できた時だけこの処理をする
            # もしi番目のフレームが静止画を抽出するものであれば、ファイル名を付けて保存する
            if True in check:
                # ここから動画フレーム処理と動画保存---------------------------------------------------------------------
                # 抽出したフレームの再生時間がテロップを入れる時間範囲に入っていれば文字入れする
                if section[1] <= time <= section[2]:
                    frame = telop(frame, section[0], W, H)  # テロップを入れる関数を実行
                # 再生時間がテロップ入れ開始時間より小さければ待機する
                elif section[1] > time:
                    pass
                else:
                    # 用意した文章がなくなったら何もしない
                    if j >= len(message) - 1:
                        pass
                    # 再生時間範囲になく、まだmessage配列にデータがある場合はjを増分しsectionを更新
                    else:
                        j = j + 1
                        section = message[j]
                video.write(frame)                          # 動画を1フレームずつ保存する
            # ここまでが動画フレーム処理と保存---------------------------------------------------------------------
            # i番目のフレームが静止画を抽出しないものであれば、何も処理をしない
            else:
                pass
        else:
            pass
    return

dir = 'movie'               # 動画が保存されているディレクトリ
path = 'clap1.avi'   # ファイル名
step = 1                    # 動画内で処理するフレーム間隔（1より大きい整数だと動画が間引かれる）

# [文章, 開始時間, 終了時間]:ここで指定した動画内時間の範囲にテロップ文章を入れる
message = [['拍手', 0, 0.227]]

# 動画処理の関数を実行
m_slice(path, dir, step, message)
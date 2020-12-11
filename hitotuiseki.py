import cv2
#処理したい画像を選択
img_name = 'clap2-photo/clap2_000.png'
 
im = cv2.imread(img_name)
# HoG特徴量の計算
hog = cv2.HOGDescriptor()
 
# サポートベクタマシンによる人検出
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.2}
 
# 人を検出した座標
human, r = hog.detectMultiScale(im, **hogParams)
 
# バウンディングボックス
for (x, y, w, h) in human:
    cv2.rectangle(im, (x, y),(x+w, y+h),(0,50,255), 3)
     
# 検出した画像を保存
cv2.imwrite('out_default_'+img_name,im)
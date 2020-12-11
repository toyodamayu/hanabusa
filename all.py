import cv2
import argparse
import chainer
import hand
from entity import params
from pose import PoseDetector, draw_person_pose
from hand import HandDetector, draw_hand_keypoints


chainer.using_config('enable_backprop', False)

if __name__ == '__main__':

    # load model
    pose_detector = PoseDetector("posenet", "models/coco_posenet.npz")
    hand_detector = HandDetector("handnet", "models/handnet.npz")

    # read image
    img = cv2.imread('data/dinner.png')

    # inference
    print("Estimating pose...")
    person_pose_array, _ = pose_detector(img)
    res_img = cv2.addWeighted(img, 0.6, draw_person_pose(img, person_pose_array), 0.4, 0)

    # each person detected
    for person_pose in person_pose_array:
        unit_length = pose_detector.get_unit_length(person_pose)

        # hands estimation
        print("Estimating hands keypoints...")
        hands = pose_detector.crop_hands(img, person_pose, unit_length)
        if hands["left"] is not None:
            hand_img = hands["left"]["img"]
            bbox = hands["left"]["bbox"]
            hand_keypoints = hand_detector(hand_img, hand_type="left")
            res_img = draw_hand_keypoints(res_img, hand_keypoints, (bbox[0], bbox[1]))
            cv2.rectangle(res_img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 255, 255), 1)
            al=bbox[0]
            bl=bbox[1]
            cl=bbox[2]
            dl=bbox[3]
            #print(hand_detector(xmax))
            #xlmax=hand.xmax
            #xlmin=hand.xmin
            #ylmax=hand.ymax
            #ylmin=hand.ymin
            #print("xn:",xlmax,xlmin,ylmax,yimin)
            print("bbox[0]:",bbox[0])
            #print("bbox[1]:",bbox[1])
            #print("bbox[2]:",bbox[2])
            #print("bbox[3]:",bbox[3])

        if hands["right"] is not None:
            hand_img = hands["right"]["img"]
            bbox = hands["right"]["bbox"]
            hand_keypoints = hand_detector(hand_img, hand_type="right")
            res_img = draw_hand_keypoints(res_img, hand_keypoints, (bbox[0], bbox[1]))
            cv2.rectangle(res_img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 255, 255), 1)
            ar=bbox[0]
            br=bbox[1]
            cr=bbox[2]
            dr=bbox[3]
            #print("bbox[0]:",bbox[0])
            #print("bbox[1]:",bbox[1])
            #print("bbox[2]:",bbox[2])
            #print("bbox[3]:",bbox[3])

        x=abs(al-cr)
        y=abs(bl-br)

        if cr<al:
            al=al-x
            cl=cl-x
        else:
            al=al+x
            cl=cl+x

        if bl<br:
            bl=bl+y
            dl=dl+y
        else:
            bl=bl-y
            dl=dl-y

        

        print("l:",al,bl,cl,dl)
        print("r:",ar,br,cr,dr)
        print('Saving result into result.png...')
        cv2.imwrite('result.png', res_img)

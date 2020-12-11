import cv2
import argparse
import chainer
from entity import params
from pose import PoseDetector, draw_person_pose
from hand import HandDetector, draw_hand_keypoints

chainer.using_config('enable_backprop', False)

if __name__ == '__main__':

    for photo in range(1542):
        # load model
        pose_detector = PoseDetector("posenet", "models/coco_posenet.npz")
        hand_detector = HandDetector("handnet", "models/handnet.npz")

        # read image
        img = cv2.imread('sun-photo/sun_{0:04d}.png'.format(photo))

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

            if hands["right"] is not None:
                hand_img = hands["right"]["img"]
                bbox = hands["right"]["bbox"]
                hand_keypoints = hand_detector(hand_img, hand_type="right")
                res_img = draw_hand_keypoints(res_img, hand_keypoints, (bbox[0], bbox[1]))

        print('Saving result into result.png...')
        cv2.imwrite('sun-bone/sun_bone_{0:04d}.png'.format(photo), res_img)

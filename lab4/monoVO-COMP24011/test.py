import numpy as np 
import cv2
import argparse

from visual_odometry import PinholeCamera, VisualOdometry

cam = PinholeCamera(1241.0, 376.0, 718.8560, 718.8560, 607.1928, 185.2157)
#Change the path below as needed
vo = VisualOdometry(cam, '/home/horia/Documents/Intro to AI Workplace/lab4/KITTI/poses/00.txt')

max_frame = 4541
test_frame_id = -1
matching_algorithm = 1

parser = argparse.ArgumentParser()
parser.add_argument("--frame_index", "-f", help="set frame_index to test")
parser.add_argument("--matching", "-m", help="set matching algorithm")

args = parser.parse_args()

if args.frame_index:
    test_frame_id = int(args.frame_index)
    max_frame = test_frame_id + 1
if args.matching:
    matching_algorithm = int(args.matching)


traj = np.zeros((600,600,3), dtype=np.uint8)

for img_id in range(max_frame):
    #Change the path below as needed
    img = cv2.imread('/home/horia/Documents/Intro to AI Workplace/lab4/KITTI/gray/00/image_0/'+str(img_id).zfill(6)+'.png', 0)

    vo.update(img, img_id, test_frame_id, matching_algorithm)

    cur_t = vo.cur_t
    if(img_id > 2):
        x, y, z = cur_t[0], cur_t[1], cur_t[2]
    else:
        x, y, z = 0., 0., 0.
    draw_x, draw_y = int(x)+290, int(z)+90
    true_x, true_y = int(vo.trueX)+290, int(vo.trueZ)+90

    cv2.circle(traj, (draw_x,draw_y), 1, (0, 255, 0), 1)
    cv2.circle(traj, (true_x,true_y), 1, (0, 0, 255), 1)
    cv2.rectangle(traj, (10, 20), (600, 60), (0,0,0), -1)
    text = "Coordinates: x=%2fm y=%2fm z=%2fm"%(x,y,z)
    cv2.putText(traj, text, (20,40), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, 8)

    cv2.imshow('Trajectory', traj)
    cv2.waitKey(1)

cv2.imwrite('map.png', traj)

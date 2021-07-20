global hcnt
hcnt = 0
import cv2
import dlib
import face
import headpose
import blink
import eye
import csv
from imutils.face_utils import shape_to_np
from pprint import pprint
import matplotlib.pyplot as plt

def main():
    print('ok')
    cap = cv2.VideoCapture(0) #instead of 0 put some variable
    if not cap.isOpened():
        print('Error: Unable to initialize Video Source.')
        return
    predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
    COUNTER = BLINK_COUNT = 0
    hbottom=htop=hleft=hleft_tilt=hright=hright_tilt=hstraight=0
    eye_stats = { "ebottom":0,"ebottom_right":0,"ebottom_left":0,"etop":0,"etop_right":0,"etop_left":0,"estraight":0,"eleft":0,"eright":0 }
   
    i = 1
    while cap.isOpened():

        ok, frame = cap.read()


        if ok:
            i = (i+1)%3

            face_rects = face.detect_faces(frame)

            for rect in face_rects:
                shape = predictor(frame, rect)
                shape = shape_to_np(shape)
                rot_vec, trans_vec, euler_angle = headpose.get_head_pose(shape)
                headpose.paint_axes(frame, rot_vec, trans_vec)
                X, Y, Z = headpose.extract_coords(euler_angle)
                headpose.paint_coords(frame, X, Y, Z)
                l, t, r, b = face.get_rect_pos(rect)
                m = int((l+r)/2)
                lhalf_face = frame[t:b, m:r]


                if blink.eye_is_closed(shape):
                    COUNTER += 1
                else:
                    if COUNTER is not 0:
                        COUNTER = 0
                        BLINK_COUNT += 1
                        print('Blinked', BLINK_COUNT)

                # print('----------------------')

                if(i==0):
                    hbottom,htop,hleft,hright,hstraight,hleft_tilt,hright_tilt = headpose.print_head_dir(X,Y,Z,hbottom,htop,hleft,hright,hstraight,hleft_tilt,hright_tilt,hcnt)
                    
                    is_straight,hstraight = headpose.head_straight(X,Y,Z,hstraight)
                    if is_straight and COUNTER is 0:
                        eye.print_eye_dir(lhalf_face,eye_stats)
                    print('--------------------')

            cv2.imshow('Output', frame)
            # cv2.imshow('Output2', lhalf_face)
            key = cv2.waitKey(10)
            if key in [27, ord('q')]:
                break
    head_stats={"bottom":hbottom,"top":htop,"right":hright,"left":hleft,"straight":hstraight,"left tilt":hleft_tilt,"right tilt":hright_tilt}
    h_total = sum(head_stats.values())
    e_total = sum(eye_stats.values())

    #percentage calc change in code:
    for k,v in head_stats.items():
        head_stats_perc=v*100.0/h_total
        print(k,head_stats_perc)

    #for k,v in eye_stats.items():
        #eye_stats_perc=v*100.0/e_total
        #print(k,eye_stats_perc)
    #head_stats_perc = {k:v/h_total*100 for k,v in head_stats.items()}

   # eye_stats_perc = { k:v/e_total*100 for k,v in eye_stats.items()}
   # pprint(head_stats_perc)
   # print('\n')
    #pprint(eye_stats_perc)

    # print("herekiuyrjjti987yihy")
    print("blinks",BLINK_COUNT)
    print("HEAD:straight",hstraight)
    #exec(open('button.py').read())
    print("top",htop)
    print("bottom",hbottom)
    print("right",hright)
    print("left",hleft)
    print("left tilt",hleft_tilt)
    print("right tilt",hright_tilt)
    pprint(eye_stats)

    print("EYE:straight",eye_stats["estraight"])
    print("top",eye_stats["etop"])
    print("bottom",eye_stats["ebottom"])
    print("right",eye_stats["eright"])
    print("left",eye_stats["eleft"])
    print("bottom right",eye_stats["ebottom_right"])
    print("bottom left",eye_stats["ebottom_left"])
    print("top right",eye_stats["etop_right"])
    print("top left",eye_stats["etop_left"])

    #eye_move = sum([1 if v>=15 else 0 for v in eye_stats_perc.values()])
    #print("eyemove",eye_move)
    if head_stats_perc > 30:

        #if eye_stats_perc['estraight']>10 and eye_move<3:

           print("confident")
        #elif eye_move>=3 :

            #print("nervous")
    else :

        print("restless")


    #if h_total > 15:
        #print("restless")    

    cap.release()
    cv2.destroyAllWindows()

    #plt.subplot(2,1,1)
    plt.figure(figsize=(13, 3))
    plt.bar(eye_stats.keys(), eye_stats.values(), width=0.2, color="blue", align='edge')
    #plt.show()

    #plt.subplot(2,1,2)
    plt.figure(figsize=(13, 3))
    plt.bar(head_stats.keys(), head_stats.values(), width=0.2, color="red", align='edge')
    plt.show()

if __name__ == "__main__":
    main()

        	




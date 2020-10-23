import os
import cv2
import sys

ix = -1
iy = -1
drawing = False
imgLoc=''


def draw_reactangle(event, x, y, flags, param):
    # Compiler chak la jawi dayma :|
    global ix, iy, drawing, imgL, pt1X, pt1Y, pt2X, pt2Y
    #awkatay clicky lay chap dadagrin
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    #awkatay mouse dajullenin dabet chwargoshakash ba dway mouse'akay da bet
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            #imread xwendnaway wenayaka ka la dir haya datwani bikaya URL yan la Camera awa frame by frame warbgri lo camera dabet VideoCapture() bakar beni...
            img2 = cv2.imread(imgLoc)
            # img2 mabastman la wenakaya w pt1 w pt2 sh shweni chwar goshakaya color awayan rangi RGB a w thickness asturi xatakaya...
            cv2.rectangle(img2, pt1=(ix,iy), pt2=(x, y),color=(0,255,255),thickness=2)
            pt1X=ix
            pt1Y=iy
            pt2X=x
            pt2Y =y
            imgL = img2
    #Final .. katek dast lasar click'aka la dabain damanawe anjamikotaye la x,y man bdate
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        img2 = cv2.imread(imgLoc)
        # ==
        cv2.rectangle(img2, pt1=(ix,iy), pt2=(x, y),color=(0,255,255),thickness=2)
        pt1X=ix
        pt1Y=iy
        pt2X=x
        pt2Y =y
        imgL = img2
    #agar chwar goshakat ba dll nabu clickeki xera bka chwargoshaka delete dabet(wenaka reset dabet)
    elif event == cv2.EVENT_FLAG_ALTKEY:
        imgL = cv2.imread(imgLoc)
    #agar clicky lay rasty krd barnamaka dabxatawa
    elif event == cv2.EVENT_RBUTTONDOWN:
        sys.exit()

#pos400x400 awa nawi aw folder'aya ka wena positive'akani tedaya
for Dir in ['pos400x400']:
    for img in os.listdir(Dir):
        if Dir == 'pos400x400':
            imgLoc = Dir+'/'+img
            #dabet naw la window'akan bneyn lo away mouse event esh bkat lasar aw window'a
            cv2.namedWindow("KRD Drawing")
            cv2.setMouseCallback("KRD Drawing", draw_reactangle)
            imgL= cv2.imread(Dir+'/'+img)
            while True:
                cv2.imshow('KRD Drawing', imgL)
                #agar dast bney ba dugmay N awa dacheta sar wenay dwatr
                if cv2.waitKey(30)==0xFF&ord('n'):
                    print('pt1X: '+str(pt1X)+" pt1Y: "+str(pt1Y)+" pt2X: "+str(pt2X)+" pt2Y: "+str(pt2Y))
                    #lerada lo har filek path 'akay wardagrin la tanishtishi aw raqam 1 a wata chand object la wenakada haya w
                    # away dikash shweni chwargoshaka balam labar away ba file txt save dakain dabet ba string waribgrin
                    line = 'pos400x400'+'/'+imgLoc+' 1 '+str(pt1X)+" "+str(pt1Y)+" "+str(pt2X)+" "+str(pt2Y)+'\n'
                    with open('recLoc.txt','a') as f:
                        f.write(line)
                    cv2.destroyAllWindows()
                    break


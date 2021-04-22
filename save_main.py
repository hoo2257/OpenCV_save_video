import cv2
import os
import datetime as dt
import time

x = dt.datetime.now()
save_dir = '{}_{}_{}_{}_{}'.format(x.year, x.month, x.day, x.hour, x.minute)
print(os.path.isdir(save_dir))

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)
else:
    pass
past_cur_time = 0
cap = cv2.VideoCapture(0)
i=0
while(cap.isOpened()):
    st_time = time.time()
    x_ = dt.datetime.now()
    cur_time = '{}_{}_{}'.format(x_.hour, x_.minute, x_.second)
    title = cur_time + '_' +str(i)

    if cur_time == past_cur_time:
        i+=1
    else:
        i=0

    ret, frame = cap.read()
    if ret:
        cv2.imshow('video_stream', frame)
        cv2.imwrite(save_dir+'/' + title + '.jpg', frame)
        past_cur_time = cur_time
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    else:
        print('Error')

cap.release()
cv2.destroyAllWindows()
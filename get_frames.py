import cv2

def get_frames(path):
    cap = cv2.VideoCapture("sample1.mp4")
    i = 0
    # a variable to set how many frames you want to skip
    frame_skip = 10
    # a variable to keep track of the frame to be saved
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i > frame_skip - 1:
            frame_count += 1
            cv2.imwrite(path + 'test_'+str(frame_count*frame_skip)+'.jpg', frame)
            i = 0
            continue
        i += 1

    cap.release()
get_frames("./test/")
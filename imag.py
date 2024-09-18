import os
import cv2

DATA_DIR = 'C:\\Users\\HP\\Desktop\\GOD\\pythonProject\\PRO'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

cap = cv2.VideoCapture(0)  # Changed the camera index to 0
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Please check your camera connection.")
            break

        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Please check your camera connection.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
            cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)
            counter += 1
        else:
            print("Invalid frame dimensions. Skipping frame capture.")

cap.release()
cv2.destroyAllWindows()

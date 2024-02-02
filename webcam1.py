import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import cv2
import cvzone
import math
import time


def webcam():
    rospy.init_node('object_detector')
    pub = rospy.Publisher('/object_detection', Image, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    cap = cv2.VideoCapture(0)  # For Webcam
    cap.set(3, 1280)
    cap.set(4, 720)

    model = YOLO("best.pt")

    classNames = ["BlueRing", "RedRing"]

    bridge = CvBridge()

    while not rospy.is_shutdown():
        success, img = cap.read()
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding Box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 5)
                w, h = x2 - x1, y2 - y1

                # Confidence
                conf = math.ceil((box.conf[0] * 100)) / 100

                # Class Name
                cls = int(box.cls[0])
                currentClass = classNames[cls]

                # Draw text on image
                cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)), scale=0.6, thickness=1, offset=3)

                # Publish image with bounding boxes
                pub.publish(bridge.cv2_to_imgmsg(img, "bgr8"))

        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        webcam()
    except rospy.ROSInterruptException:
        pass

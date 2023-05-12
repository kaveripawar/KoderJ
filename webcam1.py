# from ultralytics import YOLO
# import cv2
# import cvzone
# import math
# import time


# def webcam():
#     cap = cv2.VideoCapture(0)  # For Webcam
#     cap.set(3, 1280)
#     cap.set(4, 720)


#     model = YOLO("best.pt")

#     classNames = ["BlueRing", "RedRing"
            

#     prev_frame_time = 0
#     new_frame_time = 0

#     while True:
#          new_frame_time = time.time()
#          success, img = cap.read()
#          results = model(img, stream=True)
#          for r in results:
#              boxes = r.boxes
#              for box in boxes:
#             # Bounding Box
#                  x1, y1, x2, y2 = box.xyxy[0]
#                  x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#                  cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 5)
#                  w, h = x2 - x1, y2 - y1

#             # Confidence
#                  conf = math.ceil((box.conf[0] * 100)) / 100
#             # Class Name
#                  cls = int(box.cls[0])
#                  currentClass = classNames[cls]
#                  cvzone.putTextRect(img, f'{currentClass} {conf} {c1,c2}', (max(
#                 0, x1), max(35, y1)), scale=0.6, thickness=1, offset=3)

#          fps = 1 / (new_frame_time - prev_frame_time)
#          prev_frame_time = new_frame_time
#     # print(fps)

#          cv2.imshow("Image", img)
#          cv2.waitKey(1)
# #!/usr/bin/env python3

# import rospy
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge, CvBridgeError
# from ultralytics import YOLO
# import cv2
# import cvzone
# import math
# import time

# class YoloRos:

#     def __init__(self):
#         # Initialize ROS node
#         rospy.init_node('yolo_ros', anonymous=True)
        
#         # Set up subscriber for image topic
#         self.bridge = CvBridge()
#         self.image_sub = rospy.Subscriber('subsciber', Image, self.callback)

#         # Set up publisher for annotated image topic
#         self.annotated_pub = rospy.Publisher('publisher', Image, queue_size=10)

#         # Load YOLO model
#         self.model = YOLO("best.pt")

#         # Define class names
#         self.classNames = ["BlueRing", "RedRing"]

#     def callback(self, data):
#         try:
#             # Convert ROS Image message to OpenCV image
#             img = self.bridge.imgmsg_to_cv2(data, "bgr8")
#         except CvBridgeError as e:
#             print(e)
#             return
        
#         # Run YOLO model on image
#         results = self.model(img, stream=True)
        
#         for r in results:
#             boxes = r.boxes
#             for box in boxes:
#                 # Bounding Box
#                 x1, y1, x2, y2 = box.xyxy[0]
#                 x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 5)
#                 w, h = x2 - x1, y2 - y1

#                 # Confidence
#                 conf = math.ceil((box.conf[0] * 100)) / 100
                
#                 # Class Name
#                 cls = int(box.cls[0])
#                 currentClass = self.classNames[cls]
#                 cvzone.putTextRect(img, f'{currentClass} {conf} {c1,c2}', (max(
#                 0, x1), max(35, y1)), scale=0.6, thickness=1, offset=3)

#         # Publish annotated image
#         try:
#             self.annotated_pub.publish(self.bridge.cv2_to_imgmsg(img, "bgr8"))
#         except CvBridgeError as e:
#             print(e)

# def main():
#     # Create YoloRos object
#     yolo_ros = YoloRos()

#     # Spin ROS node
#     rospy.spin()

# if __name__ == '__main__':
#     try:
#         main()
#     except rospy.ROSInterruptException:
#         pass
#!/usr/bin/env python3

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

import socket
import cv2
import os
import numpy

UDP_IP = os.environ.get('SRV_HOST')
if(not UDP_IP):
    print("Host set to default localhost")
    UDP_IP = "127.0.0.1"
UDP_PORT = 5012

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

def video_to_mjpeg(video_file):
    # Open the video file
    # video = cv2.VideoCapture(video_path)
    
    video = cv2.open(video_file)

    # Read the first frame to get video properties
    ret, frame = video.read()
    if not ret:
        raise ValueError("Failed to read video file")

    # Get video properties
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    # Create the MJPEG stream object
    mjpeg_stream = cv2.VideoWriter_fourcc(*"MJPG")
    mjpeg_file = cv2.VideoWriter("output.mjpeg", mjpeg_stream, 30, (frame_width, frame_height))

    while True:
        # Read a frame from the video
        ret, frame = video.read()
        if not ret:
            break

        # Write the frame to the MJPEG file
        mjpeg_file.write(frame)

        # Display the frame (optional)
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    # Release resources
    video.release()
    mjpeg_file.release()
    cv2.destroyAllWindows()

# Call the function and provide the path to your video file
while (True):
    video_to_mjpeg(sock.recv(1024))
import socket,cv2, pickle,struct
import pyshine as ps # pip install pyshine
import imutils # pip install imutils
camera = input("[0/1/2] webcam/IPCamera/Video: ")
if camera == '0':
	vid = cv2.VideoCapture(0)
elif camera == '1':
	vid = cv2.VideoCapture('http://192.168.43.1:8080/video')
elif camera == '2':
	vid = cv2.VideoCapture('videos/flask.mp4')
else:
	print("\n[ Device is not available] ")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.99.1' # Here according to your server ip write the address

port = 9999
client_socket.connect((host_ip,port))

if client_socket:
	while (vid.isOpened()):
		try:
			img, frame = vid.read()
			frame = imutils.resize(frame,width=380)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			cv2.imshow(f"SENDING TO: {host_ip}",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				client_socket.close()
		except:
			print('VIDEO FINISHED!')
			break

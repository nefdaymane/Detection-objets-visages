import os
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import threading

class CameraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Detection Application")
        self.master.geometry("1900x1200")
        self.master.configure(bg="#263238")
        # Set the window icon
        self.master.iconbitmap('icon.ico')

        # Create a frame to hold the camera feed
        self.frame = tk.Frame(self.master, bg="#FFFFFF", bd=5)
        self.frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.6, anchor="n")

        # Create a label for the detection object
        self.label_detection = tk.Label(self.master, text="Detection Objects And Faces", bg="#263238", fg="#FFFFFF",
                                         font=("Arial", 16, "bold"))
        self.label_detection.place(relx=0.5, rely=0.02, anchor="n")

        # Create a label to display the camera stream
        self.label = tk.Label(self.frame, bg="#FFFFFF")
        self.label.pack(fill="both", expand=True)

        # Create a button to activate the camera
        self.start_button = tk.Button(self.master, text="Start Camera", command=self.start_camera,
                                bg="#4CAF50", fg="#FFFFFF", font=("Arial", 14, "bold"), bd=0, pady=10)
        self.start_button.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.1, anchor="n")
        #Create a button to detecte objects
        self.detection_objet_button = tk.Button(self.master, text="Detection Object", command=self.detectionObjet,
                                      bg="#0355FF", fg="#FFFFFF", font=("Arial", 14, "bold"), bd=0, pady=10)
        self.detection_objet_button.place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.1, anchor="n")
        # Create a button to detecte Faces
        self.detection_faces_button = tk.Button(self.master, text="Detection Faces", command=self.detectionFace,
                                                bg="#F9B900", fg="#FFFFFF", font=("Arial", 14, "bold"), bd=0, pady=10)
        self.detection_faces_button.place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.1, anchor="n")
        # Create a button to stop the camera
        self.stop_button = tk.Button(self.master, text="Stop Camera", command=self.stop_camera,
                                bg="#F44336", fg="#FFFFFF", font=("Arial", 14, "bold"), bd=0, pady=10)
        self.stop_button.place(relx=0.9, rely=0.8, relwidth=0.2, relheight=0.1, anchor="n")

        # Create a flag to indicate if the camera is running
        self.camera_running = False

    def start_camera(self):
        if not self.camera_running:
            # Create a new thread to run the camera
            self.camera_thread = threading.Thread(target=self.process_camera)
            self.camera_thread.start()
            self.camera_running = True
    def detectionObjet(self):
        os.popen('python detection_objet.py')
       # root.destroy()
    def detectionFace(self):
        os.popen('python identifie.py')
        #root.destroy()
    def process_camera(self):
        cap = cv2.VideoCapture(0)

        while self.camera_running:
            ret, frame = cap.read()

            # Convert the image from OpenCV's BGR format to RGB and resize it to fit the label
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (1100, 750))

            # Convert the image to a Tkinter-compatible format and display it on the label
            photo = ImageTk.PhotoImage(image=Image.fromarray(image))
            self.label.config(image=photo)
            self.label.image = photo

        cap.release()
        cv2.destroyAllWindows()

    def stop_camera(self):
        self.camera_running = False

root = tk.Tk()
app = CameraApp(root)
root.mainloop()


from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition



class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognisation system")
        
        #------------------background image-----------------
        img3=Image.open(r"C:\Users\my pc\Desktop\current_project\images\background.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=1540)


        #-------------background label-----------------
        title_lbl=Label(bg_img,text="FACE RECOGNISATION ATTANDANCE SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        #-------------student button------------------
        img4=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)


        #-------------detect face------------------
        img5=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img5=img5.resize((1530,710),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)

        #-------------Attandance face button------------------
        img6=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img6=img6.resize((1530,710),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attandance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)

        #-------------Train data button------------------
        img8=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img8=img8.resize((1530,710),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=550,width=220,height=40)

        #-------------Photo face button------------------
        img9=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img9=img9.resize((1530,710),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photo Face ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=580,width=220,height=40)

        #-------------About Developer button------------------
        img10=Image.open(r"C:\Users\my pc\Desktop\current_project\images\square1.jpg")
        img10=img10.resize((1530,710),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg9)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=580,width=220,height=40)

    #-------------------image opening--------------------
    def open_img(self):
        os.startfile("data")  


    #------------------------function buttons----------------

    def student_details(self):
           self.new_window=Toplevel(self.root)
           self.app=Student(self.new_window)

    def train_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Train(self.new_window)

    def face_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Face_Recognition(self.new_window)        
       














if __name__ == "__main__":
        root=Tk()
        obj=Face_recognition_system(root)
        root.mainloop()

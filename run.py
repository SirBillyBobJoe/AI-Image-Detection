import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from keras.models import load_model

def load_image(img_path):
    img = Image.open(img_path)
    img = img.resize((32, 32)) 
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def predict_image(img_path):
    img = load_image(img_path)
    prediction = model.predict(img)
    index = np.argmax(prediction)
    sign = class_names[index]
    label.configure(foreground='#011638', text='Prediction: ' + sign)

def upload_image():
    global last_uploaded_img_path
    try:
        file_path = filedialog.askopenfilename()
        last_uploaded_img_path = file_path
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((window.winfo_width() / 2.25), (window.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        sign_image.pack()
        
        predict_image(file_path)
    except:
        pass

def load_selected_model():
    global model, class_names
    model_choice = model_var.get()
    if model_choice == 'CIFAR-10':
        model = load_model('image_classifier.model')
        class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
    else:
        model = load_model('cifar100_image_classifier.model')
        class_names = [
            'apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 
            'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 
            'can', 'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock', 
            'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup', 'dinosaur', 
            'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 
            'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion',
            'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse',
            'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear',
            'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine',
            'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose',
            'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake',
            'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table',
            'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout',
            'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman',
            'worm'
        ]
    
    if last_uploaded_img_path:
        predict_image(last_uploaded_img_path)



window = tk.Tk()
window.geometry("500x500")
window.title('Image Classification')

last_uploaded_img_path = None 

model_var = tk.StringVar(window)
model_var.set('CIFAR-10') 

model_options = ['CIFAR-10', 'CIFAR-100']
model_menu = tk.OptionMenu(window, model_var, *model_options, command=lambda _: load_selected_model())
model_menu.pack()

upload_button = tk.Button(window, text='Upload Image', command=upload_image, padx=10, pady=5)
upload_button.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload_button.pack()

sign_image = tk.Label(window)
sign_image.pack()

label = tk.Label(window, text='Prediction will appear here', width=60, height=4, fg="blue", font=('arial', 12, 'bold'))
label.pack()

load_selected_model()  
window.mainloop()
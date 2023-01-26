# dataset
# built with help from "https://towardsdatascience.com/loading-custom-image-dataset-for-deep-learning-models-part-1-d64fa7aaeca6"
import numpy as np
import os
import cv2


def dataset_loader(data_path):

    img_data_array=[]
    class_name=[]
    cars=[]
    car_class=[]
    mris=[]
    mris_class=[]
    shoe=[]
    shoe_class=[]


    for dir1 in os.listdir(data_path):
        for file in os.listdir(os.path.join(data_path, dir1)):
            image_path= os.path.join(data_path, dir1, file)
            image= cv2.imread(image_path, cv2.COLOR_BGR2RGB)
            image=cv2.resize(image, (100, 100))
            image=np.array(image)
            image = image.astype('float32')
            image /= 255 
            if len(image.shape) < 3:
                continue
            elif dir1 =="Cars":
                img_data_array.append(image)
                cars.append(image)
                class_name.append(dir1)
                car_class.append(dir1)
            elif dir1 =="MRIs":
                img_data_array.append(image)
                mris.append(image)
                class_name.append(dir1)
                mris_class.append(dir1)
            elif dir1 =="Shoe":
                img_data_array.append(image)
                shoe.append(image)
                class_name.append(dir1)
                shoe_class.append(dir1)

    img_data_array = np.stack(img_data_array, axis=0)
    cars = np.stack(cars, axis=0)
    mris = np.stack(mris, axis=0)
    shoe = np.stack(shoe, axis=0)
    class_name = np.stack(class_name, axis=0)
    car_class = np.stack(car_class, axis=0)
    mris_class = np.stack(mris_class, axis=0)
    shoe_class = np.stack(shoe_class, axis=0)


    return img_data_array, class_name, cars, car_class, mris, mris_class, shoe, shoe_class



# def test_dataset(testdata_path):
#     img_data_array=[]
#     class_name=[]
#     cars=[]
#     car_class=[]
#     mris=[]
#     mris_class=[]
#     shoe=[]
#     shoe_class=[]


#     for dir1 in os.listdir(testdata_path):
#         for file in os.listdir(os.path.join(testdata_path, dir1)):
#             image_path= os.path.join(testdata_path, dir1, file)
#             image= cv2.imread(image_path, cv2.COLOR_BGR2RGB)
#             image=cv2.resize(image, (100, 100))
#             image=np.array(image)
#             image = image.astype('float32')
#             image /= 255 
#             if len(image.shape) < 3:
#                 continue
#             elif dir1 =="Cars":
#                 img_data_array.append(image)
#                 cars.append(image)
#                 class_name.append(dir1)
#                 car_class.append(dir1)
#             elif dir1 =="MRIs":
#                 img_data_array.append(image)
#                 mris.append(image)
#                 class_name.append(dir1)
#                 mris_class.append(dir1)
#             elif dir1 =="Shoe":
#                 img_data_array.append(image)
#                 shoe.append(image)
#                 class_name.append(dir1)
#                 shoe_class.append(dir1)

#     img_data_array = np.stack(img_data_array, axis=0)
#     cars = np.stack(cars, axis=0)
#     mris = np.stack(mris, axis=0)
#     shoe = np.stack(shoe, axis=0)
#     class_name = np.stack(class_name, axis=0)
#     car_class = np.stack(car_class, axis=0)
#     mris_class = np.stack(mris_class, axis=0)
#     shoe_class = np.stack(shoe_class, axis=0)



#     return img_data_array, class_name, cars, car_class, mris, mris_class, shoe, shoe_class
               



















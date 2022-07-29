from PIL import Image
import io
import os
import cv2 as cv



def save_file_image(id, file, type='avatar'):
    img = Image.open(file)
    if os.path.exists(f"./common/users/{id}") == False:
        os.makedirs(f"./common/users/{id}")
    img = img.convert('RGB')
    img.save(f"./common/users/{id}/{type}.jpg")


def save_list_files_post(post_id, data, num_files):
    """ print(data['media.0'].file) """
    """ if os.path.exists(f"./common/posts/{post_id}") == False:
        os.makedirs(f"./common/posts/{post_id}")
    img = Image.open(data[f"media.0"])
    img = img.convert('RGB')
    img.save(f"./common/posts/{post_id}/0.jpg") """
    if os.path.exists(f"./common/posts/{post_id}") == False:
        os.makedirs(f"./common/posts/{post_id}")
    for i in range(num_files):
        img = Image.open(data[f"media.{i}"])
        img = img.convert('RGB')
        img.save(f"./common/posts/{post_id}/{i}.jpg")

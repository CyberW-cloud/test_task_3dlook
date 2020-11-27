import os
from io import BytesIO
from datetime import datetime

from PIL import Image


# Universal timer wrapper function
def time_spent(func):
    def time_wrapper(*args, **kwargs):
        start = datetime.now()
        output = func(*args, **kwargs)
        finish = datetime.now()
        result = (finish - start).total_seconds()
        return output, result
    return time_wrapper


@time_spent
def rotate_logo(file):
    logo = Image.open(BytesIO(file.read()))
    logo = logo.rotate(180, expand=True)

    output = BytesIO()
    logo.save(output, format='JPEG')
    output.seek(0)
    return output


def upload_location(instance, filename):
    dir_path = os.path.normpath('images/product/')
    file_path = os.path.join(dir_path, filename)
    return file_path



# @time_spent
# def rotate_logo(filepath):
#     image = Image.open(filepath)
#     image = image.rotate(180)
#     image.save(filepath)
#     image.close()
import os
from icrawler.builtin import GoogleImageCrawler as gic


# func processing input to get a number of downloading pictures
def only_int():
    try:
        a = int(input("How many images do you want to download: "))
    except ValueError:
        print("TypeError. It must be a number. Try again")
        return only_int()
    return a



image_title = input("Specify kind of images you want to download: ")
nums = only_int()

user_profile = os.environ["USERPROFILE"]+"\Downloads"


# func processing input of the path manually if the path to Downloads folder can not be found authometically
def type_path():
    try:
        print("The path could not be found. Please type the path bellow")
        path = os.chdir(input("Paste the path: "))
        return path
    except FileNotFoundError:
        type_path()


try:
    os.chdir(user_profile)
except FileNotFoundError:
    type_path()
finally:
    os.mkdir(image_title)

path_ = f"{user_profile}\{image_title}"

google = gic(storage={"root_dir":  path_})
google.crawl(keyword=image_title, max_num=nums)

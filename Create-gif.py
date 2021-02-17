import imageio
import os

gif_path = "test4_big.gif"
frames_path = "img4"


def read_files_in_path(path):
  return sorted([file for file in os.listdir(path)])


def make_gif(file_list):
  with imageio.get_writer(gif_path, mode="I") as writer:
    for file in file_list:
      print(file)
      #writer.append_data(imageio.imread("{}/{}".format(frames_path, file)))


picture_files = read_files_in_path(frames_path)
make_gif(picture_files)
import imageio
import os

movie_path = "test4_big.mp4"
frames_path = "img4"


def read_files_in_path(path):
  return sorted([file for file in os.listdir(path)])


def make_movie(file_list):
  with imageio.get_writer(movie_path, fps=60) as writer:
    for file in file_list:
      writer.append_data(imageio.imread("{}/{}".format(frames_path, file)))


picture_files = read_files_in_path(frames_path)
make_movie(picture_files)

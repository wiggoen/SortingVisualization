import os

path = "img3"

for filename in os.listdir(path):
	if len(filename) == 19:
		file = filename[:12]
		ending = filename[12:]
		#print(filename, file, ending)
		old_filename = "{}/{}".format(path, filename)
		renamed_filename = "{}/{}0{}".format(path, file, ending)
		#print(old_filename)
		#print(renamed_filename)
		os.rename(old_filename, renamed_filename)
	print("Done!")
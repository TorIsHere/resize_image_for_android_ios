
# Use format is python resize_image.py (android/ios) destination source...
# Android
# hdpi    38% 
# mdpi    25%
# xhdpi   50%
# xxhdpi  75% 
# xxxhdpi 100%
#
# iOS
# @1x     33.33% 
# @2x     66.66% 
# @3x     100%

import os, sys
from PIL import Image

mode = sys.argv[1]
output_directory = sys.argv[2]

# check output directory, if exists
if not os.path.exists(output_directory):
	os.makedirs(output_directory)

if mode == "android":
	# create android diredtory
	if not os.path.exists(output_directory + "/android/hdpi"):
		os.makedirs(output_directory + "/android/hdpi")
	if not os.path.exists(output_directory + "/android/mdpi"):
		os.makedirs(output_directory + "/android/mdpi")
	if not os.path.exists(output_directory + "/android/xhdpi"):
		os.makedirs(output_directory + "/android/xhdpi")
	if not os.path.exists(output_directory + "/android/xxhdpi"):
		os.makedirs(output_directory + "/android/xxhdpi")
	if not os.path.exists(output_directory + "/android/xxxhdpi"):
		os.makedirs(output_directory + "/android/xxxhdpi")
elif mode == "ios":
	if not os.path.exists(output_directory + "/ios"):
		os.makedirs(output_directory + "/ios")


for directory in sys.argv[3:]:
	print(directory)
	for root, dirs, files in os.walk(directory):
		for f in files:
			if f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".jpg"):
				img = Image.open(os.path.join(root, f))
				base_name = os.path.splitext(f)[0]
				file_extension = os.path.splitext(f)[1]
				
				if mode == "android":
					# hdpi    38% 
					target_width = int(img.size[0] * 0.38) if int(img.size[0] * 0.38) > 0 else 1
					target_height = int(img.size[1] * 0.38) if int(img.size[1] * 0.38) > 0 else 1
					resized_image = img.resize((target_width, target_height))
					resized_image.save(os.path.join(output_directory + "/android/hdpi" + "/" + f));
					# mdpi    25%
					target_width = int(img.size[0] * 0.25) if int(img.size[0] * 0.25) > 0 else 1
					target_height = int(img.size[1] * 0.25) if int(img.size[1] * 0.25) > 0 else 1
					resized_image = img.resize((target_width, target_height))
					resized_image.save(os.path.join(output_directory + "/android/mdpi" + "/" + f));
					# xhdpi   50%
					target_width = int(img.size[0] * 0.50) if int(img.size[0] * 0.50) > 0 else 1
					target_height = int(img.size[1] * 0.50) if int(img.size[1] * 0.50) > 0 else 1
					resized_image = img.resize((target_width, target_height))
					resized_image.save(os.path.join(output_directory + "/android/xhdpi" + "/" + f));
					# xxhdpi  75% 
					target_width = int(img.size[0] * 0.75) if int(img.size[0] * 0.75) > 0 else 1
					target_height = int(img.size[1] * 0.75) if int(img.size[1] * 0.75) > 0 else 1
					resized_image = img.resize((target_width, target_height))
					resized_image.save(os.path.join(output_directory + "/android/xxhdpi" + "/" + f));
					# xxxhdpi 100%
					target_width = int(img.size[0] * 1.00) if int(img.size[0] * 1.00) > 0 else 1
					target_height = int(img.size[1] * 1.00) if int(img.size[1] * 1.00) > 0 else 1
					resized_image = img.resize((target_width, target_height))
					resized_image.save(os.path.join(output_directory + "/android/xxxhdpi" + "/" + f));
				elif mode == "ios":
					# @1x     33.33% 
					target_width = int(img.size[0] * 0.33) if int(img.size[0] * 0.33) > 0 else 1
					target_height = int(img.size[1] * 0.33) if int(img.size[1] * 0.33) > 0 else 1
					resized_image = img.resize((target_width, target_height))
					resized_image.save(os.path.join(output_directory + "/ios/" + base_name + "@1x" + file_extension));
					# @2x     66.66% 
					target_width = int(img.size[0] * 0.66) if int(img.size[0] * 0.66) > 0 else 1
					target_height = int(img.size[1] * 0.66) if int(img.size[1] * 0.66) > 0 else 1
					resized_image = img.resize((target_width, target_height))
					resized_image.save(os.path.join(output_directory + "/ios/" + base_name + "@2x" + file_extension));
					# @3x     100%
					target_width = int(img.size[0] * 1.00) if int(img.size[0] * 1.00) > 0 else 1
					target_height = int(img.size[1] * 1.00) if int(img.size[1] * 1.00) > 0 else 1
					resized_image = img.resize((target_width, target_height))
					resized_image.save(os.path.join(output_directory + "/ios/" + base_name + "@3x" + file_extension));

				#print(os.path.join(root, f) + "  " + str(img.size[0]) + " : " + str(img.size[1]))

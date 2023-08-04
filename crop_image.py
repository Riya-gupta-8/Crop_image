import cv2
import os
from parameters import crop_size, stride

def crop_image_with_stride(image_path, output_folder):
    # Reads the image
    image = cv2.imread(image_path)

    # Get the image dimensions
    height, width, _ = image.shape

    #c = 0
    # Iterate through the image and do cropping
    for y in range(0, height - crop_size + 1, stride):
        for x in range(0, width - crop_size + 1, stride):
            cropped_image = image[y:y+crop_size, x:x+crop_size]
            cropped_height, cropped_width, crop_image_matrix = cropped_image.shape
            #print(cropped_image)
            #c += 1
            # Check if the cropped segment is smaller than 640x640
            # Pad the image with 0
            if cropped_height < crop_size or cropped_width < crop_size:
                pad_height = max(crop_size - cropped_height, 0)
                pad_width = max(crop_size - cropped_width, 0)
                cropped_image = cv2.copyMakeBorder(
                    cropped_image,
                    top=0,
                    bottom=pad_height,
                    left=0,
                    right=pad_width,
                    borderType=cv2.BORDER_CONSTANT,
                    value=(0, 0, 0),
                )

            # Save the cropped image
            filename = f"{output_folder}/crop_{y}_{x}.png"
            cv2.imwrite(filename, cropped_image)
    #print('count ',c)
if __name__ == "__main__":
    input_image_path = "sample1.jpg"
    output_folder_path = "cropped_images2"

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    crop_image_with_stride(input_image_path, output_folder_path)

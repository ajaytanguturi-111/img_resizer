import os
from PIL import Image

input_folder = 'imgcomp/input_images'       
output_folder = 'imgcomp/resized_images'    
target_size = (800, 600)            
output_format = 'JPEG'              


os.makedirs(output_folder, exist_ok=True)


valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif','.webp')


for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        input_path = os.path.join(input_folder, filename)
        output_name = os.path.splitext(filename)[0] + '.' + output_format.lower()
        output_path = os.path.join(output_folder, output_name)

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(target_size)
                resized_img.convert('RGB').save(output_path, output_format)
                print(f" Resized and saved: {output_name}")
        except Exception as e:
            print(f" Failed to process {filename}: {e}")
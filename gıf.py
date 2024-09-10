from tkinter import Image

from PIL import Image

def create_gif(image_paths , output_gif_paths , duration= 500):
    images = [Image.open(image_path) for image_path in image_paths]

    images[0].save(
        output_gif_paths,
        save_all = True,
        append_images = images[1:],
        duration = duration,
        loop = 0

    )



if __name__ == "__main__":
    image_paths = ["911.jpg","huracan.jpg","audi_r8.jpg"]
    output_gif_path = "output.GIF"
    create_gif(image_paths, output_gif_path)


print(f"GIF created and saved at {output_gif_path}")

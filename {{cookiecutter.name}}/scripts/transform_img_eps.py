import os
import Image


def main():
    directory = "img" + os.path.sep
    for full_name in get_images_names():
        img = Image.open(directory + full_name)
        if img.mode not in ("L", "RGB", "CMYK"):
            img = img.convert("RGB")

        name, extension = full_name.split(".")
        eps_name = directory + name + ".eps"
        img.save(eps_name)


def get_images_names():
    names = []
    extensions = ["png"]
    for file_ in os.listdir("img"):
        extension = file_.split(".")[-1]
        if extension in extensions:
            names.append(file_)
    return names


if __name__ == "__main__":
    main()

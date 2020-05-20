from xml.etree import ElementTree as ET
import glob
import math
import time
import matplotlib.pyplot as plt


def relative_box_size(path):
    """take the relative bounding box size in the image with the path
    @path: path in the directory to the image"""
    relative = []
    root = ET.parse(path).getroot()
    w_img = int(root.find("size/width").text)
    h_img = int(root.find("size/height").text)

    boxes = root.findall("object/bndbox")
    for box in boxes:
        xmin = int(box[0].text)
        ymin = int(box[1].text)
        xmax = int(box[2].text)
        ymax = int(box[3].text)
        temp = math.sqrt((xmax - xmin) * (ymax - ymin)) / math.sqrt(
            w_img * h_img
        )
        relative.append(temp)
    return relative


def main():
    path_iterator = iter(glob.glob("Annotations_new/*.xml"))
    relative_list = []
    number_of_images = 0
    while True:
        try:
            relative_list.extend(relative_box_size(next(path_iterator)))
            number_of_images += 1
        except StopIteration:
            break
    print("Number of images: %s" % number_of_images)
    print("Number of ships: %s" % len(relative_list))

    plt.hist(relative_list, bins=100)
    plt.gca().set(
        title="Frequency Histogram",
        ylabel="Frequency",
        xlabel="Relative bbox size",
    )
    plt.savefig("F:/viettel/relative_box_size_graph/Fequency_result.png")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.2f seconds ---" % (time.time() - start_time))
    print("--- COMPLETE ---")

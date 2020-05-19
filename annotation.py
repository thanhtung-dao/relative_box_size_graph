import numpy as np
from xml.etree import ElementTree as ET
import glob
import math
import time
import seaborn as sns
import matplotlib.pyplot as plt

def relative_box_size(path):
    root = ET.parse(path).getroot()
    xmin = int(root.find('object/bndbox/xmin').text)
    ymin = int(root.find('object/bndbox/ymin').text)
    xmax = int(root.find('object/bndbox/xmax').text)
    ymax = int(root.find('object/bndbox/ymax').text)

    w_img = int(root.find('size/width').text)
    h_img = int(root.find('size/height').text)
    relative = math.sqrt((xmax-xmin) * (ymax-ymin)) / math.sqrt(w_img * h_img)
    return relative

# ----- MAIN -----
start_time = time.time()

path_list = glob.glob('Annotations_new/*.xml')
relative_list = []
for path in path_list:
    relative_list.append(relative_box_size(path))
print(len(path_list), len(relative_list))

sns.distplot(relative_list, color="dodgerblue", **kwargs)
plt.xlabel('Relative box size')
plt.ylabel('Fequency')
plt.savefig('Fequency_result.png')
plt.legend();

print("--- %.2f seconds ---" % (time.time() - start_time))
print('--- COMPLETE ---')
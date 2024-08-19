import numpy as np
import matplotlib.pyplot as plt
import os

def center(a):
    height, width = a.shape[:2]
    if height > 1 and width > 1:
        center = (height-1)/2, (width-1)/2
    else:
        if (height == 1) & (width > 1):
            center = 0, (width-1)/2
        if (height > 1) & (width == 1):
            center = (height-1)/2, 0
        if (height == 1) & (width == 1):
            center = 0, 0
    return center   

def radial_distance(a):
    cent = center(a)
    height = a.shape[0]
    width = a.shape[1]
    y, x = np.ogrid[:height, :width]

    #calculate distances 
    distances = np.sqrt((x-cent[1])**2 + (y-cent[0])**2)
    return distances

def scale(a, tmin=0.0, tmax=1.0):
    d_array = radial_distance(a)
    amin = np.min(d_array)
    amax = np.max(d_array)

    if amax != 0:
        d_array_norm = (d_array - amin) / (amax - amin)
        d_array_scaled = d_array_norm * (tmax-tmin) + tmin
    else:
        d_array_scaled = d_array
    return d_array_scaled

def radial_mask(image):
    d_array_scaled = scale(image, tmin = 0.0, tmax = 1.0)
    return 1 - d_array_scaled

def radial_fade(image):
    mask = radial_mask(image)
    cent = center(image)
    y_cent = cent[0]
    x_cent = cent[1]
    #covert mask array to 3d
    mask_3d = mask[:, :, np.newaxis]
    mask_3d = np.array(np.repeat(mask_3d, 3, axis=2))
    image_mod = image * mask_3d
    return image_mod

def main():
    image = plt.imread("painting.png")
    mask = radial_mask(image)
    image_mod = radial_fade(image)
    
    #plot the images 
    fig, axes = plt.subplots(3,1)
    axes[0].imshow(image)
    axes[1].imshow(mask)
    axes[2].imshow(image_mod)
    plt.show()

if __name__ == "__main__":
    main()

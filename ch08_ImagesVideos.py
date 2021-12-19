import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

img1 = plt.imread('test.png')
# print(img1)

# plt.imshow(img1)
# plt.imshow(img1 , cmap='gray')


# fig , ax = plt.subplots()
# im = ax.imshow(img1)
# patch = patches.Circle((245 , 200) ,
#                        radius=200 ,
#                        transform=ax.transData)
# im.set_clip_path(patch)
# ax.axis('off')


img3 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

plt.imshow(img3)

methods = ['none', 'antialiased', 'nearest', 'bilinear',
'bicubic', 'spline16', 'spline36', 'hanning',
'hamming', 'hermite', 'kaiser', 'quadric',
'catrom', 'gaussian', 'bessel', 'mitchell',
'sinc', 'lanczos', 'blackman']

fig, axs = plt.subplots(nrows=4, ncols=6, figsize=(9, 6),
                        subplot_kw={'xticks': [], 'yticks': []})
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(img3, interpolation=interp_method, cmap='hot')
    ax.set_title(str(interp_method))
plt.tight_layout()

plt.show()

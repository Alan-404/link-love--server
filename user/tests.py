#%%
import cv2 as cv
import numpy as np
# %%
id = "62e3568b53b3680b76b6b5d3"
img = cv.imread(f'../common/users/{id}/avatar.jpg')
# %%
np.asarray(img)
# %%

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

def reduce_dimentions(img):
	if len(img)==0:
		return img

	''' image preprocessing '''
	scaler=StandardScaler()
	scaler.fit(img)

	scaled_data=scaler.transform(img)

	# applying pca here

	pca = PCA(n_components=10)
	x_pca = pca.fit_transform(scaled_data)

	# cum_var_exaplined = np.cumsum(pca.explained_variance_ratio_)
	# print(cum_var_exaplined)
	# plt.figure(figsize=(8,6))
	# plt.plot(cum_var_exaplined)
	# plt.grid()
	# plt.xlabel("n_components")
	# plt.ylabel("Cummulative explained variance")
	# plt.show()
	# # print(scaled_data.shape , x_pca.shape)

	return x_pca

from nilearn import image, input_data
from sklearn.preprocessing import StandardScaler

# Spatial smoothing
smoothed_img = image.smooth_img(fmri_img, fwhm=6)  # fwhm is the size of the smoothing kernel

# Temporal filtering
filtered_img = image.clean_img(smoothed_img, low_pass=0.01, high_pass=0.1, t_r=2.5)  # t_r is the repetition time

# Normalization
scaler = StandardScaler()
normalized_img = scaler.fit_transform(filtered_img)

# Regression of confounding signals
masker = input_data.NiftiMasker(mask_img=mask_img, standardize=True, detrend=True, high_variance_confounds=True)
time_series = masker.fit_transform(normalized_img)

# Feature extraction
correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]
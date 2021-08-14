import os
import nibabel as nib
import numpy as np
from utils import fs_ss, fsl_bet

in_path = '/media/david/datos1/Coding/maestria/paper_skull_strip/test_dataset/'
fsl_bet_path = '/media/david/datos1/Coding/maestria/paper_skull_strip/skullStripped/fsl'
fs_bet_path = '/media/david/datos1/Coding/maestria/paper_skull_strip/skullStripped/freesurfer'
head = 'sub-A00038642_ses-NFB3_T1w'

subjects = next(os.walk(in_path))[1] # [2]: lists files; [1]: lists subdirectories; [0]: ?

for subject in subjects:
	print('subject: {}\n'.format(subject))
	img = os.path.join(in_path, subject, 'sub-'+subject+'_ses-NFB3_T1w.nii.gz')
	out_fsl = os.path.join(fsl_bet_path, 'ss-sub-'+subject+'_ses-NFB3_T1w.nii.gz')
	out_fs = os.path.join(fs_bet_path, 'ss-sub-'+subject+'_ses-NFB3_T1w.nii.gz')
	#fs_ss(img, out_fs)
	fsl_bet(img, out_fsl)



'''img = nib.load(os.path.join(in_path, mri))
img_data = img.get_fdata()'''


#fs_ss()
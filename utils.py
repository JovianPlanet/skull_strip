from nipype.interfaces.freesurfer import WatershedSkullStrip
from nipype.interfaces.fsl import BET

def fsl_bet(input_file, out_file):
	skullstrip = BET()
	skullstrip.inputs.in_file = input_file 		#os.path.join(head_path, head)
	skullstrip.inputs.out_file = out_file 		#os.path.join(brain_path, fsl_brain)
	skullstrip.inputs.frac = 0.2				# [0-1] Valores mas pequenos estiman un area mayor de cerebro
	#skullstrip.inputs.robust = True
	skullstrip.inputs.reduce_bias = True
	skullstrip.run()

def fs_ss(in_, out_):
	skullstrip = WatershedSkullStrip()
	skullstrip.inputs.in_file = in_ #'/media/david/datos1/Coding/maestria/paper_skull_strip/test_dataset/A00038642/sub-A00038642_ses-NFB3_T1w.nii.gz'
	skullstrip.inputs.t1 = True
	skullstrip.inputs.out_file = out_ #"/media/david/datos1/Coding/maestria/paper_skull_strip/skullStripped/brainmask.auto.nii"
	skullstrip.run()
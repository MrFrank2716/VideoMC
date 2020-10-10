#!/usr/bin/env python3

import sys

from PIL import Image

def process_frame(img, w_samples, h_samples):
	samples = []
	
	# Do some math to figure out how to choose our samples.
	(w, h) = img.size
	w_inc = w // w_samples
	w_free = w - (w_inc * w_samples)
	h_inc = h // h_samples
	h_free = h - (h_inc * h_samples)
	
	# Now actually get them.
	for y_samp in range(h_samples):
		y_pos = h_inc * y_samp + (h_free / 2)
		for x_samp in range(w_samples):
			x_pos = w_inc * x_samp + (w_free / 2)
			(r, g, b) = img.getpixel((x_pos, y_pos))
			
			# Now compute if it's a 1 or a 0.
			avg = (r + g + b) / 3
			samples.append(int(avg // 64))

	return samples

outfile = sys.argv[1]
dimx = int(sys.argv[2])
dimy = int(sys.argv[3])

frames = []

with open(outfile, 'w') as f:
	f.write("%s %s\n" % (dimx, dimy))

	cur = 0
	while True:
		img_path = "image_%s.png" % (cur + 1)
		try:
			print('Processing:', img_path)
			img = Image.open(img_path)
			samps = process_frame(img, dimx, dimy)
			samps.append('\n')

			buf = ''.join([str(s) for s in samps])
			f.write(buf)

			cur += 1
		except:
			print('Found', cur - 1, 'images')
			break

print('Done!')


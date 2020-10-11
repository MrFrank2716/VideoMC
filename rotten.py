#!/usr/bin/env python3

import sys
import math

from PIL import Image

# Demo scene style color mode.
# From: https://minecraft.gamepedia.com/Talk:Dye/Archive_1#Palette_file
COLOR_PALETTE = {
	'0': (0, 0, 0),       # black
	'1': (164, 45, 41),   # (rose!) red
	'2': (86, 51, 28),    # green
	'3': (39, 51, 154),   # brown
	'4': (56, 77, 24),    # blue
	'8': (67, 67, 67),    # purple
	'9': (39, 117, 149),  # cyan
	'a': (59, 189, 48),   # lime
	'b': (194, 181, 28),  # yellow
	'c': (104, 139, 212), # light blue
	'd': (191, 76, 201),  # magenta
	'e': (234, 128, 55),  # orange
	'f': (255, 255, 255), # whide, this is different but it's okay
}

# TODO Make this configurable.
COLOR_MODE = 'DEMO'

def calc_color_bw(rgb):
	(r, g, b) = rgb
	avg = (r + g + b) / 3
	if avg >= 128:
		return 1
	else:
		return 1
		
def calc_color_greyscale(rgb):
	(r, g, b) = rgb
	# Now compute if it's a 1 or a 0.
	avg = (r + g + b) / 3
	return int(avg // 64)

# FIXME There's much better ways of doing this than what we're doing here.  We
# need to partition up the color space a little better.  I think it might make
# more sense if we did this in the 0..1 range so we could do things like adjust
# gamma and have it still work out.
def calc_color_demoscene(rgb):
	best_color = ''
	best_dist = -1
	for (col, (cr, cg, cb)) in COLOR_PALETTE.items():
		rd = (cr - r) ** 2
		gd = (cg - g) ** 2
		bd = (cb - b) ** 2
		dist = math.sqrt(rd + gd + bd)
		if dist < best_dist or best_dist == -1:
			best_color = col
			best_dist = dist

	return best_color

def get_color_fn():
	if COLOR_MODE == 'BW':
		return calc_color_bw
	if COLOR_MODE == 'GREYSCALE':
		return calc_color_greyscale
	if COLOR_MODE == 'DEMO:
		return calc_color_demoscene

def process_frame(img, w_samples, h_samples, color_fn):
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
			rgb = img.getpixel((x_pos, y_pos))
			samples.append(color_fn(rgb))

	return samples

outfile = sys.argv[1]
dimx = int(sys.argv[2])
dimy = int(sys.argv[3])

cfn = get_color_fn()

with open(outfile, 'w') as f:
	f.write("%s %s %s\n" % (dimx, dimy, COLOR_MODE))

	cur = 0
	while True:
		img_path = "image_%s.png" % (cur + 1)
		try:
			if cur > 1 and cur % 100 == 0:
				print('Processed', cur, 'frames')

			img = Image.open(img_path)
			samps = process_frame(img, dimx, dimy, cfn)
			samps.append('\n')

			buf = ''.join([str(s) for s in samps])
			f.write(buf)

			cur += 1
		except:
			print('Found', cur - 1, 'images')
			break

print('Done!')

package io.tr3y.rottenplayer;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Scanner;

public class RottenVideo {

	public final int width, height;
	private final byte[][] frames;

	private RottenVideo(int w, int h, byte[][] frames) {
		this.width = w;
		this.height = h;
		this.frames = frames;
	}

	public int getFrameCount() {
		return this.frames.length;
	}

	public byte[] getFrame(int n) {
		return this.frames[n];
	}

	/**
	 * Loads a rottenvideo from an input stream. This could be from a file or
	 * perhaps a network resource. It stores it in memory so don't make it too
	 * large.
	 * 
	 * Closes the input stream when done.
	 */
	public static RottenVideo fromInputStream(InputStream stream) throws IOException {

		Scanner s = new Scanner(stream);

		String dimLine = s.nextLine();
		String[] parts = dimLine.split(" ");

		int w = -1;
		int h = -1;

		try {
			w = Integer.parseInt(parts[0]);
			h = Integer.parseInt(parts[1]);
		} catch (NumberFormatException e) {
			s.close();
			throw new IllegalArgumentException("malformed rottenvideo: bad dim format");
		}

		// Okay this is really bad. Java fucking sucks.
		//
		// In Rust this is just `Vec<Vec<u8>>`.
		ArrayList<Object> frames = new ArrayList<>();

		while (s.hasNextLine()) {

			String line = s.nextLine();
			char[] lineChars = line.toCharArray();

			if (lineChars.length != w * h) {
				s.close();
				throw new IllegalArgumentException("malformed rottenvideo: bad frame format");
			}

			byte[] fb = new byte[w * h];
			for (int i = 0; i < lineChars.length; i++) {
				fb[i] = (byte) lineChars[i];
			}

			// Addd
			frames.add(fb);

		}

		s.close();

		// Now that we have all the things we can put it into a proper buffer.
		//
		// Is this array constructor even the right size? Who fucking knows!
		byte[][] fbs = new byte[frames.size()][];
		for (int i = 0; i < frames.size(); i++) {
			fbs[i] = (byte[]) frames.get(i);
		}

		return new RottenVideo(w, h, fbs);

	}

}

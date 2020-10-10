package io.tr3y.rottenplayer;

import org.bukkit.DyeColor;

public class BwColorPolicy implements ColorPolicy {

	@Override
	public DyeColor getColor(char c) {
		if (c == '0') {
			return DyeColor.BLACK;
		} else {
			return DyeColor.WHITE;
		}
	}

}

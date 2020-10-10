package io.tr3y.rottenplayer;

import org.bukkit.DyeColor;
import org.bukkit.entity.Sheep;
import org.bukkit.util.BoundingBox;

public class SheepState {
	public int x, z;
	public DyeColor color;

	public SheepState() {
		// nothing!
	}

	public SheepState(int x, int z) {
		this.x = x;
		this.z = z;
		this.color = DyeColor.WHITE; // sensible defaults
	}

	public SheepState(int x, int z, DyeColor c) {
		this.x = x;
		this.z = z;
		this.color = c;
	}

	public static SheepState fromSheep(Sheep sheep) {
		BoundingBox aabb = sheep.getBoundingBox();
		int x = (int) Math.round(aabb.getCenterX());
		int z = (int) Math.round(aabb.getCenterZ());
		return new SheepState(x, z, sheep.getColor());
	}
}

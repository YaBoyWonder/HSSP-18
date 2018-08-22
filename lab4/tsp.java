import java.util.*;
import java.io.*;

public class TSP {
	private static class Point {
		public int x, y, z, index;
		public Point(int index, int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
			this.index = index;
		}

        public double distance(Point planet) {
            return Math.sqrt(Math.pow(x-planet.x,2) + Math.pow(y-planet.y,2) + Math.pow(z-planet.z,2));
        }

        public String toString() {
            return "(" + index + ": " + x + ", " + y + ", " + z + ")";
        }
	}
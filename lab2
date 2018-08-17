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

	public static ArrayList<Point> getPlanets() {
		File fileEntry = new File("planets.txt");
        ArrayList<Point> points = new ArrayList<Point>(0);
		try (BufferedReader br = new BufferedReader(new FileReader(fileEntry))) {
			int index = 0;
			String line;
			while ((line = br.readLine()) != null) {
				String[] components = line.split(" ");
				points.add(new Point( Integer.parseInt(components[0]), Integer.parseInt(components[1]), Integer.parseInt(components[2]), Integer.parseInt(components[3])));
			}
		} catch(Exception e) {
			e.printStackTrace();
			System.out.println("There was an error reading planets.txt.  Contact gru or seg.");
		} return points;
	}

	public static void saveRoute(ArrayList<Point> planets) {
        String content = "";
		for (Point i : planets) content += Integer.toString(i.index) + " ";
		try {
			FileWriter writer = new FileWriter(new File("route.txt"), false);
            writer.write(content);
            writer.close();
		} catch(Exception e) {
            e.printStackTrace();
        }
	}

    public static double evaluateRoute(ArrayList<Point> route) {
        double dist = 0;
        for (int i=0; i<route.size()-1; i++) {
            dist += route.get(i).distance(route.get(i+1));
        } return dist + route.get(route.size()-1).distance(route.get(0));
    }

	public static void main(String[] args) 	{
		ArrayList<Point> planets = getPlanets();

        System.out.println(evaluateRoute(planets));

        // Insert your code here!

		saveRoute(planets);
	}
}

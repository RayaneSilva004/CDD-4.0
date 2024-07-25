package Polimorfismo;

public class Geometria {

	public static void main(String[] args) {
		Triangulo t1 = new Triangulo();
		t1.calcArea(5, 10);
		t1.calcPerimetro(5);
		t1.calcPerimetro(3, 4, 7);
	}

}

package Encapsulamento;

public class Geometria {
	public static void main(String[] args) {
		Retangulo retangulo = new Retangulo(0, 0);
		
		double area = retangulo.calcArea();
		double perimetro = retangulo.calcPerimetro();
		
		System.out.println(area);
		System.out.println(perimetro);
	}
}

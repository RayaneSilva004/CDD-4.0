package Polimorfismo;

public class Triangulo extends Formas{
	public void calcArea(double base, double altura) {
		System.out.println((base * altura)/2);
	}
	public void calcPerimetro(double a, double b, double c) {
		System.out.println(a+b+c);	
	}
	public void calcPerimetro(double lado) {
		System.out.println(lado*3);
	}

}

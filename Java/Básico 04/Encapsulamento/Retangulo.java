package Encapsulamento;

public class Retangulo {
	private double base;
	private double altura;
	
	public Retangulo(double base, double altura) {
		this.base = base;
		this.altura = altura;
	}
		
	public double calcArea(){
		return base * altura;
		}
	public double calcPerimetro() {
		return 2 *(base + altura);
	}

}

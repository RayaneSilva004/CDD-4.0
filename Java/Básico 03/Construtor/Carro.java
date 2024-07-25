package Construtor;

public class Carro {
	public String cor;
	public double preco;
	public String modelo;
	boolean ligado = false;
	
	/*CONSTRUTOR PADRÃO*/
	public Carro(){	
	}
	
	public Carro(String cor){
		this.cor = cor;
	}
	public Carro(String cor, double preco){
		this.cor = cor;
		this.preco = preco;
	}
	public Carro(String cor, double preco, String modelo){
		this.cor = cor;
		this.preco = preco;
		this.modelo = modelo;
	}
	 public void ligar(){
		 if (ligado == true){
			 System.out.println("O carro já está ligado");
		 }else {
			System.out.println("Você ligou o carro");
			ligado = true;
			 }
		 }
	 public void desligar(){
		 if (ligado == false){
			 System.out.println("O carro já está desligado");
		 }else {
			 System.out.println("Você desligou o carro");
			 ligado = false;

		 }
	 }
	 public void estado(){
		 if (ligado ==true) {
			 System.out.println("O carro está ligado");
		 }else {
			 System.out.println("O carro está desligado");
		 }
	 
	 
	 }
}

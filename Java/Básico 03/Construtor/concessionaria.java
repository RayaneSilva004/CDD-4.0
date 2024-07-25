package Construtor;

public class concessionaria {

	public static void main(String[] args) {
		Carro c1 = new Carro();
		c1.cor = "Vermelho";
		Carro c2 = new Carro("Vermelho",500000,"Porche");
		System.out.println(c2.cor+" " + c2.preco +" "+ c2.modelo);
		c2.ligar();
		c2.ligar();
		c2.desligar();
		c2.desligar();
		c2.estado();
		c2.ligar();
		c2.estado();
		
	}

}

package Metodos;

public class Calcularmetodos {
    int somar(int a, int b) {
        return a + b;
    }
    int somar(int a, int b, int c) {
        return a + b + c;
    }
    int subtrair(int a, int b) {
        return a - b;
    }
    int subtrair(int a, int b, int c) {
        return a - b - c;
    }
    int multiplicar(int a, int b) {
        return a * b;
    }
    int multiplicar(int a, int b, int c) {
        return a * b * c;
    }
    double dividir(int a, int b) {
        if (a == 0|| b == 0) {
            System.out.println("Não se pode dividir por 0 (zero).");
            return 0; 
        } else {
            return (double) a / b;
        }
    }
    double dividir(int a, int b, int c) {
        if (a == 0|| b == 0 || c == 0) {
            System.out.println("Não se pode dividir por 0 (zero).");
            return 0; 
        } else {
            return (double) a / b / c;
        }
    }
}
		public static void main(String[] args) {
		Calcularmetodos calc = new Calcularmetodos();
		
	    //Print para mostrar o return
		
		//PrintSoma
	        System.out.println(calc.somar(5, 3));
	        System.out.println(calc.somar(5, 3, 2));
	        
	     //PrintSubtração
	        System.out.println(calc.subtrair(5, 3));
	        System.out.println(calc.subtrair(5, 3, 2));
	        
	     //PrintMultiplicação
	 
	        System.out.println(calc.multiplicar(5, 3));
	        System.out.println(calc.multiplicar(5, 3, 2));
	        
	     //PrintDivisão
	        System.out.println(calc.dividir(6, 0));
	        System.out.println(calc.dividir(0, 4));
	        System.out.println(calc.dividir(6, 2));
	        System.out.println(calc.dividir(10, 3, 2));
	        System.out.println(calc.dividir(0, 3, 2));
	        System.out.println(calc.dividir(10, 0, 2));
	        System.out.println(calc.dividir(10, 3, 0));
	    }

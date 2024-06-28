package Atv;
import java.util.Scanner;

public class Atividade01 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int respostasPositivas = 0;
        String classificacao;

        System.out.println("Telefonou para a vítima?" +
                "\n1 - Sim" +
                "\n2 - Não");
        int pergunta1 = entrada.nextInt();
        if (pergunta1 == 1){
            respostasPositivas++;
        }
        System.out.println("Esteve no local do crime?" +
                "\n1 - Sim" +
                "\n2 - Não");
        int pergunta2 = entrada.nextInt();
        if (pergunta2 == 1){
            respostasPositivas++;
        }
        System.out.println("Mora perto da vítima?" +
                "\n1 - Sim" +
                "\n2 - Não");
        int pergunta3 = entrada.nextInt();
        if (pergunta3 == 1){
            respostasPositivas++;
        }
        System.out.println("Devia para a vítima?" +
                "\n1 - Sim" +
                "\n2 - Não");
        int pergunta4 = entrada.nextInt();
        if (pergunta4 == 1){
            respostasPositivas++;
        }
        System.out.println("Já trabalhou com a vítima?" +
                "\n1 - Sim" +
                "\n2 - Não");
        int pergunta5 = entrada.nextInt();
        if (pergunta5 == 1){
            respostasPositivas++;
        }

        if (respostasPositivas == 2){
            classificacao = "Suspeita";
        } else if (respostasPositivas >= 3 && respostasPositivas <= 4) {
            classificacao = "Cumplice";
        } else if (respostasPositivas == 5){
            classificacao = "Assasino";
        }else{
            classificacao = "Inocente";
        }

        System.out.println("A classificação é: " + classificacao);

    }
}
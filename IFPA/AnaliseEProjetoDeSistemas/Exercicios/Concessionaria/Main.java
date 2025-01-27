public class Main {
    public static void main(String[] args) {
        Automovel automovel01 = new Automovel();

        // Acessa o atributo diretamente:
        automovel01.nome = "Mercedes";
        automovel01.fabricante = "Mercedes";

        System.out.println("Nome: " + automovel01.nome);
        System.out.println("Fabricante: " + automovel01.fabricante);

        Carro carro01 = new Carro();
        // Acessa o atributo via método:
        carro01.setCor("Branco");
        System.out.println("Cor: " + carro01.getCor());

        Moto moto01 = new Moto();
        //moto01.setCor("Preto");
        moto01.setModelo("Bis");
        System.out.println("Modelo: " + moto01.getModelo());

        Moto moto02 = new Moto();
        moto02.setFabricante("Honda");
        System.out.println("Fabricante: "+ moto02.fabricante);
    }
}

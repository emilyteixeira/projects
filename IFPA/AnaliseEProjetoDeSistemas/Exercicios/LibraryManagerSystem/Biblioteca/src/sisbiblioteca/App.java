package sisbiblioteca;

import java.util.Date;
import java.text.SimpleDateFormat;
import java.util.List;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        // Cadastra um livro, uma biblioteca, um cliente, um funcionário, uma categoria, um empréstimo e uma devolução
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o nome do livro: ");
        String nomeLivro = scanner.nextLine();
        System.out.println("Digite o nome do autor: ");
        String autorLivro = scanner.nextLine();
        System.out.println("Digite o ISBN do livro: ");
        String isbnLivro = scanner.nextLine();
        System.out.println("Digite a categoria do livro: ");
        String categoriaLivro = scanner.nextLine();
        System.out.println("Digite o nome da biblioteca: ");
        String nomeBiblioteca = scanner.nextLine();
        System.out.println("Digite o endereço da biblioteca: ");
        String enderecoBiblioteca = scanner.nextLine();
        System.out.println("Digite o nome do cliente: ");
        String nomeCliente = scanner.nextLine();
        System.out.println("Digite o nome do funcionário: ");
        String nomeFuncionario = scanner.nextLine();
        System.out.println("Digite o cargo do funcionário: ");
        String cargoFuncionario = scanner.nextLine();
        System.out.println("Digite a data de contratação do funcionário (dd/MM/yyyy): ");
        String dataContratacaoFuncionarioStr = scanner.nextLine();
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        Date dataContratacaoFuncionario = sdf.parse(dataContratacaoFuncionarioStr);
        System.out.println("Digite a data de empréstimo (dd/MM/yyyy): ");
        String dataEmprestimoStr = scanner.nextLine();
        Date dataEmprestimo = sdf.parse(dataEmprestimoStr);
        System.out.println("Digite a data de devolução (dd/MM/yyyy): ");
        String dataDevolucaoStr = scanner.nextLine();
        Date dataDevolucao = sdf.parse(dataDevolucaoStr);

        List<Categorias> categoria = new Categorias(categoriaLivro);
        Biblioteca biblioteca = new Biblioteca(nomeBiblioteca, enderecoBiblioteca);
        Clientes cliente = new Clientes(nomeCliente, telefoneCliente);
        Funcionarios funcionario = new Funcionarios(nomeFuncionario, cargoFuncionario, dataContratacaoFuncionario);
        Livros livro = new Livros(nomeLivro, autorLivro, isbnLivro, true, categoria);

        biblioteca.adicionarLivro(livro);
        biblioteca.adicionarCliente(cliente);
        biblioteca.contratarFuncionario(funcionario);
        biblioteca.removerCliente(cliente);
        biblioteca.despedirFuncionario(funcionario);
        
        Emprestimos emprestimo = new Emprestimos(livro, cliente, new Date(), new Date());
        funcionario.registrarEmprestimo(emprestimo);
        funcionario.realizarDevolucao(emprestimo);

        scanner.close();
    }
}

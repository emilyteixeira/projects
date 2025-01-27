package sisbiblioteca;

public class Biblioteca {
    private String nome;
    private String endereco;

    public Biblioteca(String nome, String endereco) {
        this.nome = nome;
        this.endereco = endereco;
    }

    public String getNome() {
        return nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public void adicionarLivro(Livros livro) {
        System.out.println("Livro adicionado: " + livro.getTitulo());
    }

    public void removerLivro(Livros livro) {
        System.out.println("Livro removido: " + livro.getTitulo());
    }

    public void adicionarCliente(Clientes cliente) {
        System.out.println("Cliente adicionado: " + cliente.getNomeCliente());
    }

    public void removerCliente(Clientes cliente) {
        System.out.println("Cliente removido: " + cliente.getNomeCliente());
    }

    public void contratarFuncionario(Funcionarios funcionario) {
        System.out.println("Funcionário contratado: " + funcionario.getNomeFunc());
    }

    public void despedirFuncionario(Funcionarios funcionario) {
        System.out.println("Funcionário despedido: " + funcionario.getNomeFunc());
    }
}

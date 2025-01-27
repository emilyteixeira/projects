package sisbiblioteca;

import java.util.Date;

public class Emprestimos {
    private Livros livro;
    private Clientes cliente;
    private Date dataEmprestimo;
    private Date dataDevolucao;

    public Emprestimos(Livros livro, Clientes cliente, Date dataEmprestimo, Date dataDevolucao) {
        this.livro = livro;
        this.cliente = cliente;
        this.dataEmprestimo = dataEmprestimo;
        this.dataDevolucao = dataDevolucao;
    }

    public Livros getLivro() {
        return livro;
    }

    public Clientes getCliente() {
        return cliente;
    }

    public Date getDataEmprestimo() {
        return dataEmprestimo;
    }

    public Date getDataDevolucao() {
        return dataDevolucao;
    }

    public void setLivro(Livros livro) {
        this.livro = livro;
    }

    public void setCliente(Clientes cliente) {
        this.cliente = cliente;
    }

    public void setDataEmprestimo(Date dataEmprestimo) {
        this.dataEmprestimo = dataEmprestimo;
    }

    public void setDataDevolucao(Date dataDevolucao) {
        this.dataDevolucao = dataDevolucao;
    }

    public void registrar() {
        System.out.println("Empréstimo registrado: " + this.livro.getTitulo());
    }

    public void finalizar() {
        System.out.println("Devolução realizada: " + this.livro.getTitulo());
    }
}

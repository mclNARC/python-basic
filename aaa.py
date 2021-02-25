def removerTitulo(livros):
    removeLivro = input("\nDeseja remover algum livro? se sim digite 'S' se não digite 'N': ")
    while 1:
        if removeLivro == 's' or removeLivro == 'S':
            nomeLivroRemove = (input("Digite o nome do livro: "))
            if nomeLivroRemove in (livros):
                livros.remove(nomeLivroRemove)
            else:
                print("Livro não encontrado")
                    removeLivro2 = (input("Deseja remover outro livro se sim digite 'S' se não digit)).upper().strip()[0]
                                 while removeLivro2 not in 'Ss':
                                        removeLivro2 = (input( "[erro digite S para remover outro livro]Deseja remover outro livro se sim digite 'S' se não digit)).upper().strip()[0]


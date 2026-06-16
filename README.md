# Loja de Jogos

---
O sistema busca resolver o problema de organizacao de jogos, que devido a sua imensa quantidade e base de dados, se mostra dificil sua padronização e catalogação.

## 1. Modelos
### 1.1. Desenvolvedor
| Atributo      | Tipo      | Exemplo     |
|---------------|-----------|-------------|
| nome          | CharField | Team Cherry |
| engine        | CharField | Unity       |
| data_fundacao | DateField | 2014        |

### 1.2. Plataforma
| Atributo       | Tipo         | Exemplo    |
|----------------|--------------|------------|
| tipo           | CharField    | Computador |
| nome           | CharField    | Steam      |
| geracao        | IntegerField | 3          |
| ano_lancamento | DateField    | 12/09/2003 |

### 1.3. Jogo
| Atributo                 | Tipo                      | Exemplo                                          |
|--------------------------|---------------------------|--------------------------------------------------|
| titulo                   | CharField                 | Hollow Knight                                    |
| classificacao_indicativa | IntegerField              | 10                                               |
| estilo                   | CharField                 | Video-game                                       |
| genero                   | CharField                 | Metroidvania                                     |
| data_lancamento          | DateField                 | 24/02/2017                                       |
| descricao                | TextField                 | Na cidade perdida de Hallownest, um cavaleiro... |
| desenvolvedor            | ForeignKey(Desenvolvedor) | Team Cherry                                      |
| plataforma               | ManyToMany(Plataforma)    | Playstation 4, Playstation 5, Steam...           |

## 2. Configuracoes Técnicas
No modelo do Jogo o atributo desenvolvedor se conecta com 1 desenvolvedor especifico da tabela Desenvolvedor, visto que cada jogo pode ser feito por um estúdio/conjunto de pessoas/pessoa, mas cada desenvolvedor pode criar multiplos jogos, criando relacionamento 1xN. Analogamente um jogo pode estar disponivel em diversas plataformas, e cada plataforma suporta múltiplos jogos, criando relacionamento NxM.
Além disso, no modelo Jogo, o ForeignKey(Desenvolvedor, on_delete=models.SETNULL) foi usado devido a possibilidade de um estudio fechar e o jogo se manter ativo (como diversos jogos offline). Dessa forma, o SET_NULL será responsável por manter o registro do jogo e definir o desenvolvedor como nulo.

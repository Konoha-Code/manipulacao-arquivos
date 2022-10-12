# manipulacao-arquivos

![image](https://img.shields.io/badge/N%C3%ADvel-F%C3%A1cil-brightgreen?link=https://github.com/Konoha-Code?q=nivel-facil&type=all)

Desafio simples para manipulação de arquivos

## Entrada

Arquivo [`produtos.txt`](./produtos.txt), um arquivo com a estrutura, conforme exemplo abaixo:

```csv
id|descricao|gtin|quantidade_estoque|preco_unitario
1|Produto 1|7890000000001|29.38|8.0196
2|Prod C|||91.712
3|Prod B|7890000000003||17.41
4|Prod A|7890000000004||17.41
5|Produto 5||3.21|47.809
```

Onde cada propriedade é separada por um pipe `|`, as propriedades gtin e quantidade estoque podem estar vazias.

## Saída

Arquivo `estoque.txt`, um arquivo com a estrutura, conforme exemplo abaixo:

```csv
    id|descricao                               |preco_estoque  
000001|Produto 1                               |000000000235.62
000005|Produto 5                               |000000000153.47
000002|Prod C                                  |000000000000.00
000004|Prod A                                  |000000000000.00
000003|Prod B                                  |000000000000.00
      |TOTAL                                   |000000000389.09
```

A coluna `id` deve conter zeros à esquerda até ter o tamanho de 6 caracteres, a coluna `descricao` deve conter espaços à direita até ter o tamanho de 40 caracteres, a coluna `preco_estoque` deve conter zeros à esquerda até ter o tamanho de 15 caracteres.
A ordenação dos produtos deve ser:

- `preco_estoque` -> decrescente;
- `preco_unitario` -> decrescente;
- `descricao` -> crescente;

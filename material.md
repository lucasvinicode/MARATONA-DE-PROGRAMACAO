# C

## Entrada e Saída (stdio.h):
scanf(): Para entrada formatada de dados.
printf(): Para saída formatada de dados.

## Manipulação de Strings (string.h):
strlen(): Retorna o tamanho de uma string.\
strcpy(), strncpy(): Copiam strings.\
strcmp(), strncmp(): Comparam strings.\
strcat(), strncat(): Concatenam strings.

## Aritmética e Conversão (stdlib.h):
atoi(), atof(): Convertem strings em números inteiros ou de ponto flutuante.\
rand(): Gera números pseudoaleatórios.\
abs(), labs(): Valor absoluto de um número.\
qsort(): Ordena um array.

## Gerenciamento de Memória (stdlib.h):
malloc(), calloc(): Alocação de memória dinâmica.\
free(): Liberação de memória alocada dinamicamente.

## Estruturas de Dados:
struct: Define uma estrutura de dados personalizada.\
typedef: Define um novo tipo a partir de um existente.\
enum: Define um conjunto de constantes inteiras.

## Matemática (math.h):
Funções matemáticas como sqrt(), pow(), sin(), cos(), tan() etc.

## Bitwise (bit manipulation):
Operações bitwise como &, |, ^, <<, >>, ~.

## Alocação dinamica

Declara variavel para alocação dinamica
>int *array;\
int size = 5;

Aloca memoria dinamicamente, e inicializa o vetor com 0
>array = (int *)calloc(size, sizeof(int));

 Aloca sem inicializar
>array = (int *)malloc(size * sizeof(int));

Realocando ou aumentando
>int *new_array = (int *)realloc(array, new_size * sizeof(int));

É importante sempre fazer a verificação para conferir se a alocação funcionou
>if (new_array == NULL) {\
    printf("Falha na realocação de memória.\n");\
    free(array); \
    return 1;\
}

# Python

## Entrada e Saída:
input(): Para entrada de dados do usuário.\
print(): Para saída de dados na tela.

## Estruturas de Dados:
Listas: Trabalhar com sequências mutáveis de elementos.\
Tuplas: Sequências imutáveis.\
Dicionários: Coleções associativas (chave-valor).\
Conjuntos: Coleções de elementos únicos.

## Manipulação de Strings:
Métodos de string: split(), join(), replace(), find(), startswith(), endswith(), etc.\
Formatação de strings: F-strings (a partir do Python 3.6) ou str.format().\

## Controle de Fluxo:
if, else, elif: Estruturas condicionais.\
for: Laço de repetição para iterar sobre sequências.\
while: Laço de repetição com condição.\

## Funções e Modularidade:
def: Para definir funções.\
return: Para retornar valores de uma função.\
Módulos: Importar funcionalidades externas com import.\
lambda: Funções anônimas.\

## Ordenação e Busca:
sorted(): Ordenar listas.\
min() e max(): Encontrar o menor e o maior elemento em uma sequência.\
list.index(): Encontrar o índice de um elemento.

## Matemática:
Funções matemáticas: abs(), pow(), round(), math.sqrt(), etc.\
Operações de divisão: / (divisão normal), // (divisão inteira), % (resto da divisão).

## Bitwise:
Operações bitwise: &, |, ^, <<, >>.

## Geradores e Iteradores:
range(): Criar sequências numéricas.\
enumerate(): Iterar com índices.\
zip(): Agregar elementos de várias sequências.


## Manipulação de Arquivos:
open(): Abrir arquivos para leitura ou escrita.\
read(), readline(), readlines(): Ler conteúdo de arquivos.\
write(): Escrever em arquivos.

## Expressões Regulares:
Módulo re: Trabalhar com padrões de busca e substituição em strings.

```python
import re

# Verifica se uma string contém um número
pattern = r'\d+'
text = "12345"
if re.match(pattern, text):
    print("Contém um número")
else:
    print("Não contém um número")

# Encontra todas as ocorrências de números em uma string
text = "Tenho 3 maçãs, 2 bananas e 5 laranjas."
numbers = re.findall(pattern, text)
print("Números encontrados:", numbers)

# Substitui números em uma string por 'X'
new_text = re.sub(pattern, 'X', text)
print("Texto modificado:", new_text)

# Divide uma string em palavras usando espaços como separador
pattern = r'\s+'
text = "Isso é uma frase com várias palavras."
words = re.split(pattern, text)
print("Palavras:", words)
```

'.': Corresponde a qualquer caractere, exceto nova linha.\
'\d': Corresponde a um dígito.\
'+': Corresponde a um ou mais ocorrências do caractere anterior.\
'\s': Corresponde a um espaço em branco.\
'*': Corresponde a zero ou mais ocorrências do caractere anterior.\
'\w': Corresponde a um caractere alfanumérico.\
'[]': Define um conjunto de caracteres possíveis.\
'^': Corresponde ao início de uma linha.\
'$': Corresponde ao final de uma linha.

# C++

## Entrada e Saída:

cin e cout: Para entrada e saída padrão.\
cerr e clog: Para mensagens de erro e log.

## Contêineres da STL:

vector, list, deque, queue, stack: Estruturas de dados comuns.\
set, map, unordered_set, unordered_map: Estruturas de dados de conjuntos e mapas.

## Algoritmos da STL:
sort, reverse, rotate: Ordenação e rotação de elementos.\
find, binary_search, lower_bound, upper_bound: Busca em contêineres ordenados.\
max_element, min_element: Encontrar o elemento máximo e mínimo.

## Iteradores:
begin(), end(): Obtém iteradores para o início e o fim de um contêiner.
advance(): Move um iterador para a frente ou para trás.

## Strings:
string: Manipulação de strings.
getline(): Para ler uma linha inteira.

## Matemática:
abs, fabs: Valor absoluto.
ceil, floor, round: Funções de arredondamento.
pow, sqrt, log, exp: Funções matemáticas.

## Bitwise (Manipulação de bits):
&, |, ^, ~: Operações bitwise.
<<, >>: Deslocamento de bits.

## Alocação Dinâmica:
new, delete: Alocação e liberação de memória.
malloc, calloc, realloc, free: Alternativas em C.

## Templates:
template: Para criar classes e funções genéricas.

## Ordenação Personalizada:
Usando funções de comparação personalizadas em algoritmos.

## Operador Ternário:
condição ? valor_se_verdadeiro : valor_se_falso.

## Operações em Conjuntos:
set_intersection, set_union, set_difference.

## Operações com String:
substr, find, replace.

## Operações com Vetores:
erase, insert, emplace_back, emplace.

Matrizes:

Uso de matrizes e vetores de vetores.
Clock:

clock(), CLOCKS_PER_SEC para medir o tempo de execução.

´´´
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> numbers = {5, 2, 8, 1, 3};

    // Inserção e Acesso
    numbers.push_back(10);            // Adiciona um elemento ao final
    numbers.insert(numbers.begin() + 2, 7);  // Insere 7 na posição 2
    int first = numbers.front();      // Primeiro elemento
    int last = numbers.back();        // Último elemento
    int atPos2 = numbers[2];          // Acesso usando índice

    // Tamanho e Iteração
    int size = numbers.size();        // Tamanho do vetor
    for (int num : numbers) {
        std::cout << num << " ";      // Iteração usando range-based for loop
    }

    // Remoção
    numbers.pop_back();               // Remove o último elemento
    numbers.erase(numbers.begin() + 1);  // Remove elemento na posição 1

    // Ordenação e Busca
    sort(numbers.begin(), numbers.end());  // Ordena em ordem crescente
    bool found = binary_search(numbers.begin(), numbers.end(), 8);  // Busca binária

    // Limpeza
    numbers.clear();                  // Remove todos os elementos

    return 0;
}
´´´
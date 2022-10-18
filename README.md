# AnaliseDeAlgoritmos
Repositório destinado aos trabalhos e atividades da cadeira de Análise de Algoritmos
<h1>Insertion Sort vs Insortion Sort com Busca Binaria:<h1/>
<h6>  
O Insertion Sort é um dos algoritmos de ordenação de implementação mais simples, basicamente, a ordenação por inserção é eficiente para pequenos valores de dados, e para vetores que já estejam totalmente ordenados. É sabido que o Insertion Sort é Θ(n²).
A busca binária é um algoritmo de busca bem performático em buscar um item numa lista ordenada. Ela funciona dividindo repetidamente pela metade uma parte da lista que deve conter o item, e comparar com o item na posição do meio se o item procurado deve estar em uma posição acima ou abaixo da sua, e repetindo até chegar no item buscado. Sabe-se que desde que a lista esteja ordenada a busca binária apresenta complexidade Θ(lg n).
O Insertion Sort com busca binária é um algoritmo de ordenação como o Insertion Sort, mas em vez de usar a pesquisa linear para encontrar o local onde um elemento deve ser inserido, usamos a busca binária. Assim, reduzimos o limite superior da busca de Θ(N) para Θ(log N). Idealmente o Insertion Sort com busca binaria poderia ser dito como Θ(N(lgN)), porém por ter de fazer o shift, ou troca, entre os itens a ser ordenados do array, acaba não sendo Θ(N(lgN)), sendo apenas Θ(N²).
Portanto, tanto o Insertion Sort quanto o Insertion Sort com busca binaria são Θ(N²), porém o Insertion Sort com busca binaria ainda é melhor, mesmo que não o suficiente para ser um Θ de ordem menor, mas ainda performa melhor que o Insertion Sort Padrão como pode-se notar nos testes que seguem:
<h6/>

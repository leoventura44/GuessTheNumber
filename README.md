# GuessTheNumber

Este é um simples programa em que o computador irá gerar um número aleatório e o usuário irá tentar adivinhar que número é esse.

Neste projeto usei a IDE PyCharm, e escolhi uma numeração entre 1 e 10 - não por ser mais fácil para programar - e sim para ser mais rápido para adivinhar, já que um numero entre 1 e 1000 funcionaria da mesma maneira, e para isso basta mudar o valor da função GUESS ao chamá-la.

Para este Projeto chamado GuessTheNumber, o processo foi bem simples:
- Importei o módulo RANDOM;
- Criei uma função GUESS com uma variável X;
- Criei uma variável chamada random_number e pelo módulo RANDOM puxei a função random.randint() e coloquei os argumentos entre 1 e X (A função desta é simplesmente gerar um numero INT aleatório);
-Coloquei o valor de GUESS = 0 para que o número 0 não seja gerado aleatoriamente, afinal queremos um número somente entra 1 e 10
-Enfim, apliquei um While Loop com Input para que o usuário insira um numero e computador diga se ele acertou o numero corretamente. Caso o valor dado pelo usuário seja MENOR, o computador irá avisar que o número é menor, e caso seja MAIOR, a mesma coisa. Quando o usuário acertar o numero será dado uma mensagem de Parabéns e o loop irá parar.

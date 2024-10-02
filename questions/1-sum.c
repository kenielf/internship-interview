#include <stdio.h>

// 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
//    Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
//    Imprimir(SOMA);
//    Ao final do processamento, qual será o valor da variável SOMA?
int main() {
  // Declare variables
  int index = 13;
  int sum = 0;
  int k = 0;

  // Increment counter and sum
  while (k < index) {
    k += 1;
    sum += k;
  }

  // Print the result (expected result: 91)
  printf("Soma: %d\n", sum);

  // Exit
  return 0;
}

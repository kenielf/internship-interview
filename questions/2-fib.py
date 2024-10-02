#!/usr/bin/env python3
from functools import lru_cache
from sys import exit


@lru_cache
def fib(n: int) -> int:
    """
    Calcular fibonacci de maneira memoizada, recursivamente
    """
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def main():
    """
    2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo
       valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2,
       3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar
       onde, informado um número, ele calcule a sequência de Fibonacci e
       retorne uma mensagem avisando se o número informado pertence ou não a
       sequência.
    """
    try:
        value: int = int(input("Valor > "))
    except ValueError:
        print("ERRO: Valor de entrada deve ser um inteiro positivo!")
        exit(1)

    seq: list[int] = [fib(n) for n in range(value)]
    if value in seq:
        print(f"O valor '{value}' está contido na sequência de fibonacci.")
    else:
        print(f"O valor '{value}' não está contido na sequência de fibonacci.")


if __name__ == "__main__":
    main()

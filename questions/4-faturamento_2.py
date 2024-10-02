#!/usr/bin/env python3
from json import loads
from pathlib import Path


revenue: dict[str, float] = {
    "SP": 67_836.43,
    "RJ": 36_678.66,
    "MG": 29_229.88,
    "ES": 27_165.48,
    "Outros": 19_849.53,
}


def main():
    """
    4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por
       estado:
       • SP – R$67.836,43
       • RJ – R$36.678,66
       • MG – R$29.229,88
       • ES – R$27.165,48
       • Outros – R$19.849,53
       Escreva um programa na linguagem que desejar onde calcule o percentual
       de representação que cada estado teve dentro do valor total mensal da
       distribuidora.
    """
    # Calculate the total
    total = sum([revenue[x] for x in revenue])

    # Iteratively show the percentage of each group
    for key in revenue:
        percentage = (revenue[key] / total) * 100
        print(f"Percentual {key}: {percentage:.2f}%")


if __name__ == "__main__":
    main()

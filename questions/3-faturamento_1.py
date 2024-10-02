#!/usr/bin/env python3
from json import loads
from pathlib import Path


DATA_FILE = Path(__file__).parent.parent / "data" / "dados.json"
VALUE_KEY = "valor"
DAY_KEY = "dia"


def main():
    """
    3) Dado um vetor que guarda o valor de faturamento diário de uma
       distribuidora, faça um programa, na linguagem que desejar, que calcule e
       retorne:
        - O menor valor de faturamento ocorrido em um dia do mês;
        - O maior valor de faturamento ocorrido em um dia do mês;
        - Número de dias no mês em que o valor de faturamento diário foi
        superior à média mensal.
    """
    # Read the data
    with open(DATA_FILE, "r") as file:
        # Open the data and parse it - values in crescent order
        data = sorted(loads(file.read()), key=lambda x: x[VALUE_KEY])

    # Remove any days with no revenue
    filtered_data = [x for x in data if x[VALUE_KEY] > 0]

    # Calculate the results
    lowest, highest = filtered_data[0], filtered_data[-1]
    average = sum([x[VALUE_KEY] for x in filtered_data]) / len(filtered_data)
    days_above_average = [x for x in filtered_data if x[VALUE_KEY] > average]

    # Show results
    print(f"Menor Faturamento: R${lowest[VALUE_KEY]:,.2f} (Dia {lowest[DAY_KEY]})")
    print(f"Maior Faturamento: R${highest[VALUE_KEY]:,.2f} (Dia {highest[DAY_KEY]})")
    print(
        f"Dos {len(data)} dias, {len(days_above_average)} se encontram acima da média mensal de R${average:,.2f}"
    )


if __name__ == "__main__":
    main()

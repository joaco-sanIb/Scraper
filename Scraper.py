import codecs
import pandas as pd
from bs4 import BeautifulSoup
import pyfiglet


def Main():
    banner = pyfiglet.figlet_format("420 Argentina")
    print(banner)
    print("Instruciones:\nPoner este programa en la misma carpeta que el archivo que desa usar.\nCambiar el nobre del archivo a R.html\nCuando este listo ingrese las columnas que desea extrraer.")

    tot = int(input("\nCantidad de columnas a extraer:"))

    file = codecs.open(
        "./R.html", "r", "utf-8")
    f = file.read()
    soup = BeautifulSoup(f, "lxml")
    table = soup.find_all("table")[0]

    x = len(table.find_all("th"))
    y = len(table.find_all("tr"))
    new_table = pd.DataFrame(columns=range(0, x), index=range(0, y))

    row_marker = -1
    for row in table.find_all("tr"):

        colums_marker = 0
        columns = row.find_all("td")
        for column in columns:
            new_table.iat[row_marker, colums_marker] = column.get_text()
            colums_marker += 1
        row_marker += 1

    for col in range(0, x):
        if col > 2:
            if col != tot:

                new_table.drop([col], axis=1, inplace=True)
    print(new_table)
    print(new_table.to_json(orient='split'))
    with open('output.json', 'w') as outfile:
        outfile.write(new_table.to_json(orient='split'))
    if "y" == input("Esto es lo que buscabas y/n:"):
        print("Ahora aparece un archivo output.json. Ese el el resultado")
    else:
        Main()


if __name__ == "__main__":
    Main()


# links that i stole the code from
# https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

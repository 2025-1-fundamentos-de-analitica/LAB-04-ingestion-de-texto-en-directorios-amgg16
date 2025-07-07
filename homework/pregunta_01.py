# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import pandas as pd
def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    with zipfile.ZipFile("files/input.zip", 'r') as comprimido:
        comprimido.extractall("files")

    #carpeta de salida
    os.makedirs("files/output", exist_ok=True)



    for particion in ["train", "test"]:
        registros = []
        base = os.path.join("files", "input", particion)
        if not os.path.isdir(base):
            continue

        # Recorremos las carpetas positive/negative/neutral
        for etiqueta in ["positive", "negative", "neutral"]:
            ruta_etiqueta = os.path.join(base, etiqueta)
            if not os.path.isdir(ruta_etiqueta):
                continue
            for nombre in os.listdir(ruta_etiqueta):
                if not nombre.endswith(".txt"):
                    continue
                ruta_txt = os.path.join(ruta_etiqueta, nombre)
                with open(ruta_txt, encoding="utf-8") as f:
                    texto = f.read().strip()
                # Aquí usamos "target" en lugar de "sentiment"
                registros.append({
                    "phrase": texto,
                    "target": etiqueta
                })

        #Guardar CSV 
        df = pd.DataFrame(registros)
        df.to_csv(f"files/output/{particion}_dataset.csv", index=False)


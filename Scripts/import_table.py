from utils.utlis import get_cols_name, change_dtype
import camelot
import pandas as pd


class PDFReader:
    def __init__(self, input_path):
        self.input_path = input_path

    def read_file(self):
        docs = camelot.read_pdf(self.input_path, pages="all")

        section_colmap = get_cols_name()
        all_sections = list(section_colmap.keys())

        results = {}   # ← wird zurückgegeben

        for i, table in enumerate(docs):
            df = table.df
            section = all_sections[i] if i < len(all_sections) else f"section_{i}"

            section_cols = section_colmap.get(section, [])
            if len(section_cols) == len(df.columns):
                df.columns = section_cols

            # ALLE SPALTEN IN STRING KONVERTIEREN
            df = df.astype(str)

            # Datei speichern
            csv_path = f"DB/raw/{section}_table.csv"  
            df.to_csv(csv_path, index=False)

            # In Rückgabe speichern
            results[section] = {
                "df": df,
                "csv_path": csv_path
            }

        return results       # ← HIER werden die Daten zurückgegeben


# Beispielaufruf
reader = PDFReader("docs/Dok.pdf")
result = reader.read_file()

# Ausgabe prüfen
# print(result.keys())

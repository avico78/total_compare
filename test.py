import pandas as pd

class ExcelLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.excel_dataframes = self._load_excel_sheets()

    def _load_excel_sheets(self):
        # Read all sheets into a dictionary of dataframes
        return pd.read_excel(self.file_path, sheet_name=None)

    def display_sheets(self):
        # Access each dataframe by sheet name dynamically
        for sheet_name, df in self.excel_dataframes.items():
            print(f"Sheet Name: {sheet_name}")
            print(df)
            print("-" * 40)

if __name__ == "__main__":
    # Example usage
    excel_file_path = "run12.xlsx"
    excel_loader = ExcelLoader(excel_file_path)
    excel_loader.display_sheets()

import pandas as pd
import json

class ExportController:
    """
    Export feedback reports to various formats (CSV, PDF, JSON, etc.).
    """

    def export_to_csv(self, data, filename):
        """
        Export data (list of dicts or DataFrame) to a CSV file.
        """
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

    def export_to_json(self, data, filename):
        """
        Export data (list of dicts or DataFrame) to a JSON file.
        """
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient='records')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # PDF export can be implemented using libraries like ReportLab or FPDF
    # def export_to_pdf(self, data, filename):
    #     pass  # Placeholder for PDF export logic
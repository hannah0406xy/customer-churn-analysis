import xlrd
import os

def generate_data_dictionary():
    # Read the Excel file
    excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'data_documentation_class.xls')
    wb = xlrd.open_workbook(excel_path)
    ws = wb.sheet_by_index(0)
    
    # Create docs directory if it doesn't exist
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    
    # Generate markdown content
    md_content = "# Telecom Churn Dataset Dictionary\n\n"
    md_content += "This document describes the variables in the telecom churn dataset.\n\n"
    
    # Add table header
    md_content += "| Variable Name | Description | Type |\n"
    md_content += "|--------------|-------------|------|\n"
    
    # Add each variable (skip header row)
    for row_idx in range(1, ws.nrows):
        var_name = str(ws.cell_value(row_idx, 0)).strip()
        description = str(ws.cell_value(row_idx, 1)).strip()
        var_type = str(ws.cell_value(row_idx, 2)).strip() if ws.ncols > 2 else "Unknown"
        
        # Clean up the content
        var_name = var_name.replace('|', '-')
        description = description.replace('|', '-')
        var_type = var_type.replace('|', '-')
        
        if var_name:  # Only add non-empty rows
            md_content += f"| {var_name} | {description} | {var_type} |\n"
    
    # Write to file
    output_path = os.path.join(docs_dir, 'data_dictionary.md')
    with open(output_path, 'w') as f:
        f.write(md_content)

if __name__ == "__main__":
    generate_data_dictionary() 
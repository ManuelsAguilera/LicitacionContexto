---
name: xlsx
description: Use when creating, reading, or manipulating Excel workbooks programmatically with formulas, charts, and formatting.
---

# Excel Spreadsheets

## When to Use This Skill
- Generating Excel reports with formatted data
- Adding formulas, charts, or conditional formatting
- Reading and processing data from .xlsx files
- Handling large datasets efficiently

## Workflow
1. Install the library: `pip install openpyxl` or `npm install exceljs`
2. Create a workbook: `wb = Workbook()` or `new ExcelJS.Workbook()`
3. Access or create worksheets: `ws = wb.active`
4. Write data: cells, rows, or columns
5. Add formulas: `ws['B2'] = '=SUM(A1:A10)'`
6. Format cells: font, fill, border, alignment, number format
7. Add charts: reference a data range and configure the chart type
8. Save: `wb.save('output.xlsx')`

## Rules
- Don't merge cells for layout — use it only for data that spans multiple columns
- Use number formats for dates, currency, and percentages
- Set column widths for readability — don't leave defaults
- Test with Excel, LibreOffice, and Google Sheets
- Stream large datasets instead of loading everything into memory
- Use freeze panes for headers on large sheets

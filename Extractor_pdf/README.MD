
Explanation:
    I built an ETL pipeline here I extracted structured data from PDFs, transformed it into CSV using Python, and loaded it into PostgreSQL using psycopg2 with proper transaction handling and conflict management.


Install:
    pdfplumber, pandas,psycopg2 

pdfplumber:
Used to extract text and tables from PDF files.
It works well with text-based PDFs and allows page-level access, making it ideal for data extraction and preprocessing tasks.

psycopg2:
A PostgreSQL database adapter for Python.
It allows Python applications to connect, insert, update, and query data in PostgreSQL databases using SQL

pandas:
A powerful data analysis and manipulation library.
It provides the DataFrame structure, which makes cleaning, transforming, and exporting data (CSV, Excel, DB) fast and efficient.


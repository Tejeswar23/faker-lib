# Log Data Generation and Analysis using Faker

## Description

This project focuses on generating fake server log data using the Python Faker library
and analyzing that data to understand basic log patterns. The generated logs are read
from a file, processed using regular expressions, and summarized into a separate
log summary file.

The main goal of this project is to practice file handling, regex, and real-time
log analysis concepts using Python.

## Project Functionality

- Generate fake server log data
- Read and process log data from a text file
- Extract IP addresses using regular expressions
- Identify unique and duplicate IP addresses
- Analyze HTTP status codes (2xx, 3xx, 4xx, 5xx)
- Save the summarized output into `log_summary.txt`

## Technologies Used

- Python
- Faker Library
- Regular Expressions
- File Handling
- VS Code

## Workflow

1. Fake server logs are generated using Faker
2. Log data is stored in a text file
3. The file is read line by line
4. Regex is used to extract required information
5. Log details are analyzed and categorized
6. Final summary is written into a summary file

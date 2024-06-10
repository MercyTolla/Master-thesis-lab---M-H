readme_content = """
# Master Thesis Lab - M-H

This GitHub repository includes all relevant data files and codes used in the lab for the master thesis by Hanna Imsland Mo and Mercy Abebe Tolla.

## Contents

### Scripts

- **test_plot.py**: This script plots the removed weight against time. It is used to analyze the erosion data.

### Folders

- **Excess Files**: Contains preliminary work and files that were not included in the final analysis. This folder can be neglected.
- **Data**: Contains Excel spreadsheets with data obtained from the erosion cell testing and the rotational and oscillatory tests performed using the Anton Paar Rheometer.

### Data Files

- **Erosion Data**: Data from the erosion cell tests.
- **Rheometer Data**: Data from the rotational and oscillatory tests conducted with the Anton Paar Rheometer.
"""
with open("README.md", "w") as file:
    file.write(readme_content)


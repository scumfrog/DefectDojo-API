# Defect-Dojo Data Exporter

You can find two main scripts:

## Defectdojo Report

This script is designed to fetch and report findings from the Defect-Dojo API. The key features are:

- Retrieve the total number of findings created in the last 30 days.
- Retrieve the number of findings closed in the last 30 days.
- Organize findings based on their severity.
- Exclude findings of a specific product type.

## Pre-requisites

- Python 3.x
- `requests` library (`pip install requests`)

## Configuration

Before running the script, set up the necessary configurations:

1. Open the script in your favorite editor.
2. Modify the following variables under the configuration section:
    - `BASE_URL`: Your Defect-Dojo instance URL.
    - `USERNAME`: Your Defect-Dojo username.
    - `PASSWORD`: Your Defect-Dojo password.
    - `EXCLUDE_PRODUCT_TYPE`: ID of the product type you want to exclude.

Note: The script by default disables SSL/TLS warnings to handle self-signed certificates. If you have a valid certificate for your Defect-Dojo instance, you can set `VERIFY_SSL` to `True`.

## Running the script

To run the script:

```bash
python script_name.py
```
Replace `script_name.py` with the actual name of the script if you've renamed it.

## Output

The script will print the findings count, organized by their severity, for the last 30 days. 

## Notes

The script uses pagination to retrieve all findings from the Defect-Dojo API. Ensure that the API limits are set appropriately to allow fetching all records.

and 

# DefectDojo User/Group Data Exporter

A Python script to fetch and export roles, groups, and users with their permissions from a DefectDojo instance into a CSV file.

## Features

- Uses basic authentication.
- Ignores SSL errors (use with caution; intended for controlled/test environments).
- Exports roles, groups, and users with permissions to `results.csv`.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/scumfrog/DefectDojo-API.git
cd DefectDojo-API
```

2. Install the required Python libraries:

```bash
pip install requests
```

3. Update the `dojo_export.py` script with your DefectDojo instance details:

- `BASE_URL`: The base URL of your DefectDojo instance.
- `USERNAME`: Your DefectDojo username.
- `PASSWORD`: Your DefectDojo password.

## Usage

Run the script:

```bash
python dojo_export.py
```

After successful execution, you will find a `results.csv` file in the current directory containing the exported data.

## Warning

This script is configured to ignore SSL errors for ease of use in controlled or test environments. Please exercise caution and consider the security implications before using it in a production environment.

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

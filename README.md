# Defect-Dojo Reporting Script

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

---

Save the above content as `README.md` and place it in the same directory as the script in your Git repository.

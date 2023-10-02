import requests
from datetime import datetime, timedelta
import urllib3
from collections import defaultdict

# Disable SSL warning in case we use self-signed certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "URL_DEFECTDOJO"
USERNAME = 'USER'
PASSWORD = 'PWD'
VERIFY_SSL = False
EXCLUDE_PRODUCT_TYPE = "ID_PRODUCT"  # Exclude if you wanted any product type for the counting

def fetch_all_pages(endpoint, params={}):
    offset = 0
    limit = 25
    total_records = []
    
    while True:
        print(f"Fetching data for offset {offset}...")
        response = requests.get(
            BASE_URL + endpoint, 
            auth=(USERNAME, PASSWORD),
            params={**params, "limit": limit, "offset": offset},
            verify=VERIFY_SSL
        )

        if response.status_code != 200:
            print(f"Error on page: {response.url}, Status code: {response.status_code}")
            print(response.text)
            raise Exception("There was an error fetching the findings.")
        
        data = response.json()
        total_records.extend(data["results"])
        
        if data["next"] is None:
            break
        offset += limit
    return total_records

def process_findings(findings):
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)

    created_last_30_days = defaultdict(int)
    closed_last_30_days = defaultdict(int)

    for finding in findings:
        if datetime.fromisoformat(finding["created"]) >= thirty_days_ago:
            created_last_30_days[finding["severity"]] += 1
            if not finding["active"]:
                closed_last_30_days[finding["severity"]] += 1

    print(f"Total number of findings created in the last 30 days: {sum(created_last_30_days.values())}")
    for severity, count in created_last_30_days.items():
        print(f"Number of {severity} findings created in the last 30 days: {count}")
        
    print(f"\nTotal number of findings closed in the last 30 days: {sum(closed_last_30_days.values())}")
    for severity, count in closed_last_30_days.items():
        print(f"Number of {severity} findings closed in the last 30 days: {count}")

if __name__ == "__main__":
    findings = fetch_all_pages("findings/", {"product_type__exact": EXCLUDE_PRODUCT_TYPE, "exclude": True})
    process_findings(findings)

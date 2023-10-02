import requests
import csv

# Configuration
BASE_URL = 'URL'
ENDPOINT_ROLES = '/api/v2/roles/'  # Adjust as per documentation
ENDPOINT_GROUPS = '/api/v2/groups/'  # Adjust as per documentation
ENDPOINT_USERS = '/api/v2/users/'  # Adjust as per documentation
USERNAME = 'your_username'
PASSWORD = 'your_password'
CSV_FILE = 'results.csv'


def get_data_from_endpoint(session, endpoint):
    """Fetch data from a specific endpoint."""
    response = session.get(BASE_URL + endpoint)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


def save_to_csv(data):
    """Save data to a CSV file."""
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Name", "Permissions"])  # Header

        for item in data:
            if item["type"] == "Role":
                writer.writerow(["Role", item["name"], item["permissions"]])
            elif item["type"] == "Group":
                writer.writerow(["Group", item["name"], item["permissions"]])
            elif item["type"] == "User":
                writer.writerow(["User", item["username"], item["permissions"]])


def main():
    # Ignore SSL warnings (not safe)
    requests.packages.urllib3.disable_warnings()
    session = requests.Session()
    session.verify = False
    session.auth = (USERNAME, PASSWORD)

    # Fetch data
    roles = get_data_from_endpoint(session, ENDPOINT_ROLES)
    groups = get_data_from_endpoint(session, ENDPOINT_GROUPS)
    users = get_data_from_endpoint(session, ENDPOINT_USERS)

    all_data = [{"type": "Role", **role} for role in roles] + \
               [{"type": "Group", **group} for group in groups] + \
               [{"type": "User", **user} for user in users]

    # Save to CSV
    save_to_csv(all_data)


if __name__ == "__main__":
    main()

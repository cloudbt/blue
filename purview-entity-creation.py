import requests
import json

def get_access_token(tenant_id, client_id, client_secret):
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': 'https://purview.azure.net'
    }
    token_r = requests.post(token_url, data=token_data)
    return token_r.json().get('access_token')

def create_entities(account_name, access_token, entities):
    url = f"https://{account_name}.purview.azure.com/catalog/api/atlas/v2/entity/bulk"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps({"entities": entities}))
    return response

# Replace these with your actual values
tenant_id = "your_tenant_id"
client_id = "your_client_id"
client_secret = "your_client_secret"
account_name = "your_purview_account_name"

# Get access token
access_token = get_access_token(tenant_id, client_id, client_secret)

# Define the entities
entities = [
    {
        "typeName": "azure_sql_table",
        "attributes": {
            "name": "M_Approver",
            "friendlyName": "Approver master",
            "description": "Common Master",
            "qualifiedName": "azure_sql_table://M_Approver"
        }
    },
    {
        "typeName": "azure_sql_column",
        "attributes": {
            "name": "RowVersion",
            "dataType": "timestamp",
            "description": "RowVersion",
            "isNullable": False,
            "qualifiedName": "azure_sql_table://M_Approver/RowVersion"
        },
        "relationshipAttributes": {
            "table": {
                "typeName": "azure_sql_table",
                "uniqueAttributes": {
                    "qualifiedName": "azure_sql_table://M_Approver"
                }
            }
        }
    },
    {
        "typeName": "azure_sql_column",
        "attributes": {
            "name": "ID",
            "dataType": "varchar",
            "length": 100,
            "description": "User ID",
            "isNullable": False,
            "qualifiedName": "azure_sql_table://M_Approver/ID"
        },
        "relationshipAttributes": {
            "table": {
                "typeName": "azure_sql_table",
                "uniqueAttributes": {
                    "qualifiedName": "azure_sql_table://M_Approver"
                }
            }
        }
    },
    {
        "typeName": "azure_sql_column",
        "attributes": {
            "name": "Name",
            "dataType": "nvarchar",
            "length": 30,
            "description": "Approval name",
            "isNullable": True,
            "qualifiedName": "azure_sql_table://M_Approver/Name"
        },
        "relationshipAttributes": {
            "table": {
                "typeName": "azure_sql_table",
                "uniqueAttributes": {
                    "qualifiedName": "azure_sql_table://M_Approver"
                }
            }
        }
    }
]

# Create the entities
response = create_entities(account_name, access_token, entities)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

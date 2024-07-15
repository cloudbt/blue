import requests
import json

def get_access_token(tenant_id, client_id, client_secret):
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://purview.azure.net/.default'
    }
    token_r = requests.post(token_url, data=token_data)
    return token_r.json().get('access_token')

def get_or_create_collection(account_name, access_token, collection_name):
    # This function remains the same as in the previous example
    # ...

def create_entities(account_name, access_token, collection_id, entities):
    url = f"https://{account_name}.purview.azure.com/catalog/api/atlas/v2/entity/bulk"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Add collection information to each entity
    for entity in entities:
        entity['attributes']['collectionId'] = collection_id

    payload = {
        "entities": entities
    }
    response = requests.post(url, headers=headers, json=payload)
    return response

# Replace these with your actual values
tenant_id = "your_tenant_id"
client_id = "your_client_id"
client_secret = "your_client_secret"
account_name = "your_purview_account_name"
collection_name = "CollectionA"

# Get access token
access_token = get_access_token(tenant_id, client_id, client_secret)

# Get or create collection
collection_id = get_or_create_collection(account_name, access_token, collection_name)
if not collection_id:
    print(f"Failed to get or create collection '{collection_name}'.")
    exit(1)

# Define the entities
entities = [
    {
        "typeName": "azure_sql_table",
        "attributes": {
            "name": "M_Approver",
            "qualifiedName": f"mssql://your-server.database.windows.net/your-database/your-schema/M_Approver#{collection_id}",
            "description": "Approver master table"
        }
    },
    {
        "typeName": "azure_sql_column",
        "attributes": {
            "name": "RowVersion",
            "qualifiedName": f"mssql://your-server.database.windows.net/your-database/your-schema/M_Approver#RowVersion#{collection_id}",
            "data_type": "timestamp",
            "description": "RowVersion column"
        },
        "relationshipAttributes": {
            "table": {
                "typeName": "azure_sql_table",
                "uniqueAttributes": {
                    "qualifiedName": f"mssql://your-server.database.windows.net/your-database/your-schema/M_Approver#{collection_id}"
                }
            }
        }
    },
    {
        "typeName": "azure_sql_column",
        "attributes": {
            "name": "ID",
            "qualifiedName": f"mssql://your-server.database.windows.net/your-database/your-schema/M_Approver#ID#{collection_id}",
            "data_type": "varchar",
            "length": 100,
            "description": "User ID column"
        },
        "relationshipAttributes": {
            "table": {
                "typeName": "azure_sql_table",
                "uniqueAttributes": {
                    "qualifiedName": f"mssql://your-server.database.windows.net/your-database/your-schema/M_Approver#{collection_id}"
                }
            }
        }
    },
    {
        "typeName": "azure_sql_column",
        "attributes": {
            "name": "Name",
            "qualifiedName": f"mssql://your-server.database.windows.net/your-database/your-schema/M_Approver#Name#{collection_id}",
            "data_type": "nvarchar",
            "length": 30,
            "description": "Approval name column"
        },
        "relationshipAttributes": {
            "table": {
                "typeName": "azure_sql_table",
                "uniqueAttributes": {
                    "qualifiedName": f"mssql://your-server.database.windows.net/your-database/your-schema/M_Approver#{collection_id}"
                }
            }
        }
    }
]

# Create the entities
response = create_entities(account_name, access_token, collection_id, entities)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

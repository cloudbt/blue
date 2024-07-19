
AWS Aurora MySQLのインスタンスクラスをdb.r5.largeからdb.r6.largeに変更する方法と、その際のアプリケーションへの影響を最小限に抑える方法について説明します。また、変更前後のコストの概算も提供します。
変更方法：

リーダーインスタンスの変更:

AWS Management ConsoleまたはAWS CLIを使用して、各リーダーインスタンスを個別に変更します。
変更中、短時間のダウンタイムが発生しますが、ライターインスタンスは影響を受けません。
リーダーを1つずつ変更することで、常に少なくとも1つのリーダーが利用可能な状態を維持できます。


ライターインスタンスの変更:

ライターインスタンスの変更には、フェイルオーバーが必要です。
Aurora の自動フェイルオーバー機能を利用するか、手動でフェイルオーバーを実行します。
フェイルオーバー中、短時間（通常60秒以内）の書き込み操作の中断が発生します。



アプリケーションへの影響を最小限に抑えるためのヒント：

メンテナンスウィンドウ中に実行: トラフィックの少ない時間帯を選んで変更を実施します。
アプリケーションの準備:

接続プールを使用している場合、古い接続を適切に破棄し、新しい接続を確立するようにアプリケーションを設定します。
フェイルオーバーに対応できるよう、アプリケーションにリトライロジックを実装します。


段階的な変更: リーダーを1つずつ変更し、各変更後にアプリケーションの動作を確認します。

コストの比較:
注意: 以下は概算であり、実際のコストは使用リージョンやその他の要因によって異なる場合があります。
db.r5.large (現在):

vCPU: 2
メモリ: 16 GiB
ネットワークパフォーマンス: 最大10 Gbps

db.r6g.large (変更後):

vCPU: 2
メモリ: 16 GiB
ネットワークパフォーマンス: 最大10 Gbps

一般的に、db.r6g.largeはdb.r5.largeと比較して約10-20%のコスト削減が期待できます。ただし、正確なコストは、リージョン、使用量、予約インスタンスの有無などによって変わります。
例えば、米国東部（バージニア北部）リージョンでのオンデマンド料金を基に概算すると：
db.r5.large: 約$0.27/時
db.r6g.large: 約$0.226/時
3つのインスタンス合計で：
変更前: $0.27 x 24 x 30 x 3 = 約$583.20/月
変更後: $0.226 x 24 x 30 x 3 = 約$488.16/月
この例では、月額約$95.04の削減が見込まれます。ただし、これはあくまで概算であり、実際のコストは様々な要因によって変動する可能性があります。正確なコストについては、AWS料金計算ツールを使用するか、AWSの担当者に相談することをお勧めします。

















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

def get_collections(account_name, access_token):
    url = f"https://{account_name}.purview.azure.com/account/collections?api-version=2021-07-01"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Replace these with your actual values
tenant_id = "your_tenant_id"
client_id = "your_client_id"
client_secret = "your_client_secret"
account_name = "your_purview_account_name"

# Get access token
access_token = get_access_token(tenant_id, client_id, client_secret)

# Get collections
collections = get_collections(account_name, access_token)

# Print collections
print(json.dumps(collections, indent=4))

# Extract the ID of a specific collection (replace 'collection_name' with the actual name of your collection)
collection_name = "your_collection_name"
collection_id = None
for collection in collections['value']:
    if collection['name'] == collection_name:
        collection_id = collection['id']
        break

print(f"Collection ID for '{collection_name}': {collection_id}")



Status Code: 404
Response: {"requestId": "687bbee1-e1a7-49bc-b10d-0b2f99e7f6d1", "errorCode": "ATLAS-404-00-007", "errorMessage": "Invalid instance reation/updation parameters passed : azure_sql_column data_type: mandatory attribute value missing in type azure_sql_column"}
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
            "dataType": "TIMESTAMP",
            "description": "RowVersion",
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
            "dataType": "VARCHAR(100)",
            "description": "User ID",
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
            "dataType": "NVARCHAR(30)",
            "description": "Approval name",
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
            "dataType": "TIMESTAMP",
            "description": "RowVersion",
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
            "dataType": "VARCHAR(100)",
            "description": "User ID",
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
            "dataType": "NVARCHAR(30)",
            "description": "Approval name",
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

import pyautogui
import sys
import os
import time
import random


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

try:

  while True:
    sleep = random.randrange(60, 120)
    time.sleep(sleep)
    step = random.randrange(2)
    #if sleep % 2 == 0:
      #pyautogui.moveTo(100,100,duration=0.25)
    #pyautogui.moveTo(200,100,duration=step)
    click = random.randrange(100, 200)
    pyautogui.click(500,click)
except KeyboardInterrupt:
    print('\nDone')

Microsoft Purviewアカウントのガイドラインを作成するための基本方針として、次のポイントを考慮します。

1. **アカウントの作成と管理**:
   - 各テナントに対して1つのMicrosoft Purviewアカウントを作成します。
   - アカウントの作成時には、適切な管理者ロールを割り当て、必要な権限を与えます。
   - アカウントの管理者は、アカウント内のデータのアクセス権やセキュリティポリシーを適切に管理します。

2. **コレクションの作成と管理**:
   - 各環境（例：PreProd、Prod）ごとにコレクションを作成します。
   - コレクションは、その環境に関連するデータを一元管理するためのコンテナとして機能します。
   - データの特性やセキュリティ要件に応じて、適切なコレクションを作成し、データを整理します。

3. **アクセス管理と権限設定**:
   - 各コレクションに対して適切なアクセス権を割り当てます。例えば、PreProd環境のデータにアクセスできるのは開発者のみとするなど。
   - アクセス権の設定は、ロールベースのアクセス制御（RBAC）を使用して行います。
   - データへのアクセス権は、最小限の必要な権限に制限し、原則として原則として最小特権の原則に従います。

4. **監査とコンプライアンス**:
   - アカウント内のデータのアクセスや操作を監査ログに記録します。
   - 監査ログの定期的なレビューと分析を行い、セキュリティイベントやポリシー違反の検出を行います。
   - コンプライアンス要件に準拠するための監査ログの保持期間やレポート作成方法を定義します。

5. **トレーニングと教育**:
   - ユーザーに対してMicrosoft Purviewの使い方やセキュリティポリシーに関するトレーニングを提供します。
   - データ管理やセキュリティ意識向上のための定期的な教育プログラムを実施します。

これらの方針をもとに、Microsoft Purviewアカウントのガイドラインを作成し、組織内でのデータ管理とセキュリティの向上に役立ててください。


Here's the guideline for creating a Microsoft Purview Account based on the provided policy:

1. **Account Creation and Management**:
   - Create one Microsoft Purview account for each tenant.
   - Assign appropriate administrator roles during account creation and grant necessary permissions.
   - Account administrators should manage access rights and security policies within the account effectively.

2. **Collection Creation and Management**:
   - Create collections for each environment (e.g., PreProd, Prod).
   - Collections serve as containers to centrally manage data related to each environment.
   - Create and organize data into appropriate collections based on the characteristics and security requirements of the data.

3. **Access Management and Permission Setting**:
   - Assign appropriate access rights to each collection. For example, only developers may access data in the PreProd environment.
   - Access rights are set using Role-Based Access Control (RBAC).
   - Access to data should be limited to the minimum necessary privileges, following the principle of least privilege.

4. **Audit and Compliance**:
   - Record access and operations on data within the account's audit logs.
   - Regularly review and analyze audit logs to detect security events and policy violations.
   - Define retention periods for audit logs and methods for generating compliance reports to adhere to compliance requirements.

5. **Training and Education**:
   - Provide training on how to use Microsoft Purview and educate users on security policies.
   - Conduct regular education programs on data management and security awareness.

Utilize these guidelines to create a Microsoft Purview Account and enhance data management and security within your organization.

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

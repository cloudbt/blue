This Mermaid diagram illustrates the relationship between the Governance Domain Policy and the Data Product Access Policy. Here's an explanation of the diagram:

The Governance Domain Policy, Glossary Term Policy, and Critical Data Element Policy all inherit their policies to the Data Product Access Policy.
The Data Product Access Policy aggregates these inherited policies along with its own specific policies.
The inherited policies from the Governance Domain include:

Manager Approval
Data Copy Permission
Custom Attestations


The Data Product specific policies include:

Permitted Access
Approval Requirements
Access Request Approvers
Access Provider
Attestations
Terms of Use


All these policies are aggregated and reflected in the Access Request Form that data consumers see when requesting access to a data product.

This diagram helps visualize how policies at different levels (Governance Domain, Glossary Terms, Critical Data Elements) are inherited and combined with Data Product-specific policies to create a comprehensive access policy for each data product. CopyRetryC

-----
I've created a new, more comprehensive diagram that includes the policy structure, the process of requesting access to data products, and how to view access requests. Here's an explanation of the diagram:

Policy Structure:

Shows the relationship between Governance Domain Policy and Data Product Access Policy.
Illustrates how these policies are aggregated to form the basis for the request form.


Access Request Process:

Steps 1-2: User searches the Data Catalog and finds a Data Product.
Steps 3-4: User requests access by filling out and submitting the Request Form.
Steps 5-6: This triggers an Approval Workflow, notifying the Approvers.
Steps 7-8: Approvers make a decision, and the User is notified of the outcome.


View Access Requests:

Shows how a User can check their access requests.
Displays the possible statuses: Pending, Approved, Denied, and Completed.



基盤構築の段階では、以下の具体的な作業内容と方法を実施します。

1. **Azureクラウドインフラの構築とコード化**
   - **作業内容:**
     - Azureポータルを使用して、必要なAzureリソース（仮想マシン、ネットワーク、ストレージなど）を構築します。
     - ARM (Azure Resource Manager) テンプレートを作成し、インフラストラクチャをコードで定義します。
   - **方法:**
     - Azureポータルにログインし、必要なリソースを選択してデプロイします。
     - ARMテンプレートを使用して、インフラストラクチャをコードで定義し、管理します。
     - PowerShellやAzure CLIを使ってARMテンプレートを適用し、インフラストラクチャを自動化します。

2. **システム構成図検討と設計**
   - **作業内容:**
     - システムの機能要件や非機能要件を分析し、適切なシステム構成図を検討します。
     - ネットワーク構成、サーバー構成、データベース構成などを設計します。
   - **方法:**
     - 関係者とのミーティングやワークショップを実施し、要件を明確にし、システム構成図を合意します。
     - ツールやソフトウェアを使用して、システムの設計図を作成し、関係者と共有します。

3. **データベースの移行：OracleDBからAzure SQLDatabaseへ**
   - **作業内容:**
     - OracleDBからAzure SQL Databaseへのデータベース移行計画を立案します。
     - データの抽出、変換、ロード (ETL) を実施して、データの移行を実現します。
   - **方法:**
     - SSMA (SQL Server Migration Assistant) や自作のスクリプトを使用して、OracleDBからAzure SQL Databaseへのデータ移行を行います。
     - 移行前のテストを行い、データの整合性と完全性を確認します。

4. **設計書とテスト仕様書の作成**
   - **作業内容:**
     - システム設計書やテスト仕様書を作成し、プロジェクトの進行と品質管理を確保します。
     - 設計やテストの方針、手順、基準を文書化します。
   - **方法:**
     - テンプレートやツールを使用して、設計書やテスト仕様書を作成します。
     - 関係者とのレビューを行い、必要に応じて修正や更新を行います。

5. **テストの実施**
   - **作業内容:**
     - テスト計画に基づいて、システムの各機能や性能をテストします。
     - 単体テスト、結合テスト、システムテストなどを実施します。
   - **方法:**
     - テストケースを作成し、テストを実施します。
     - テスト結果を記録し、問題点を特定して修正します。

6. **リリース作業の実施**
   - **作業内容:**
     - テストが完了したシステムを本番環境にリリースし、運用に移行します。
   - **方法:**
     - リリース手順を定義し、本番環境への変更を計画し、実施します。
     - リリース後のシステムの動作をモニタリングし、問題がないことを確認します。

これらの作業を段階的に進めることで、損保子システムの基盤を効果的に構築し、運用保守を確保します。



運用保守作業の具体的な作業内容と方法を以下に示します。

1. **新機能追加要望によるInfra Azureリソースの追加**
   - **作業内容:**
     - ユーザーやステークホルダーからの新機能追加や要望に基づき、必要なAzureリソースを追加します。
     - リソースの追加には、仮想マシン、データベース、ストレージなどが含まれます。
   - **方法:**
     - Azureポータルやコマンドラインツールを使用して、必要なリソースを作成します。
     - リソースの構成や設定は、プロジェクトの要件やセキュリティポリシーに準拠して行います。

2. **Azureコストの削減**
   - **作業内容:**
     - Azureのリソース使用状況をモニタリングし、無駄なコストを削減するための施策を実施します。
     - 不要なリソースの停止や削除、リソースのサイズ変更などを検討します。
   - **方法:**
     - Azure Cost ManagementやAzure Advisorなどのツールを使用して、コスト分析を行います。
     - リソースの利用状況やコストを評価し、最適なコスト削減策を選択します。

3. **Azure Monitorでの監視設定**
   - **作業内容:**
     - システムのパフォーマンス、可用性、セキュリティなどを監視し、問題を早期に検出します。
     - モニタリング対象となるメトリクスやログを設定し、モニタリングダッシュボードを構築します。
   - **方法:**
     - Azure Monitorを使用して、アラートルールを設定し、異常や問題の通知を受け取ります。
     - メトリクスやログの収集を構成し、適切なモニタリングを行います。

これらの作業を通じて、システムの運用を円滑に行い、コストの最適化や問題の早期発見・対応を実現します。

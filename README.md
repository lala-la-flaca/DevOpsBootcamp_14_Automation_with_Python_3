# 🐍Module 14 – Automation with Python
This exercise is part of Module 14: Automation with Python. Module 14 focuses on automating cloud operations with Python. The demos showcase how to interact with AWS services (EC2, EKS, snapshots), perform monitoring tasks, and implement recovery workflows. By the end of this module, you will have practical experience in scripting infrastructure automation, monitoring, and recovery solutions.

# 📦Demo 3 – Automate Displaying EKS Cluster Information
# 📌 Objective
Create a Python script that fetches and displays AWS EKS cluster status and details.

# 🚀 Technologies Used
* Python: programming language.
* IntelliJ-PyCharm: IDE used for development.
* AWS: Cloud provider.
* Boto3 AWS SDK for Python.
* Terraform

# 🎯 Features
✅ Retrieves EKS cluster details
📡 Displays cluster configuration and status

# Prerequisites
* AWS account
* Python and PyCharm installed.
* Terraform EKS demo.
  
# 🏗 Project Architecture

# ⚙️ Project Configuration
   
## Adding Tags to EC2 Instances
1. Deploy the EKS infrastructure using Terraform from the demo in the Terraform section.
   
2. Import boto3 module.
   ```bash
   import boto3
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_2/blob/main/Img/2.PNG" width=800 />
   
3. Initialize EKS client
   ```bash
   eks_client = boto3.client('eks', region_name = "us-east-2")   
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_3/blob/main/Img/2.PNG" width=800 />
   
4. List Available EKS Clusters
   ```bash
      #List Clusters
      available_clusters = eks_client.list_clusters()
      eks_clusters = available_clusters["clusters"]
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_3/blob/main/Img/4.PNG" width=800 />
   
5. Get details about the cluster and print them
   ```bash
       for eks_cluster in eks_clusters:
    
          #Getting details about the cluster
          cluster_details = eks_client.describe_cluster(
              name = eks_cluster
          )
          cluster_info = cluster_details["cluster"]
          cluster_status = cluster_info["status"]
          cluster_endpoint = cluster_info["endpoint"]
          cluster_version = cluster_info["version"]
      
          print(f"Cluster: {eks_cluster} status is {cluster_status}\nThe Cluster endpoint is: {cluster_endpoint}\nThe Cluster K8 version is: {cluster_version}")

   ```
   

   5. Outputs:
      <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_3/blob/main/Img/4%20name%20and%20status.png" width=800 />
      <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_3/blob/main/Img/5%20getting%20endpoint%20and%20version.png" width=800 />
      
   

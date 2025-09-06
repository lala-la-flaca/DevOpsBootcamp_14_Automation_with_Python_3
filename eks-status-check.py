import boto3

eks_client = boto3.client('eks', region_name = "us-east-2")

#List Clusters
available_clusters = eks_client.list_clusters()
eks_clusters = available_clusters["clusters"]

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






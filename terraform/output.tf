output "eks_cluster_endpoint" {
    value = aws_eks_cluster.app-cluster.endpoint

}

output "rds_endpoint" {
    value = aws_db_instance.app-db.endpoint
  
}
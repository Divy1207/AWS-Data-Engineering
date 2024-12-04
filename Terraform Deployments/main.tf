#S3 Deployment
# Provider configuration
provider "aws" {
  region = "ca-central-1"
}

# Create an S3 Bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-divy-12"
  acl    = "private"

}

# Enable Versioning
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.my_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Enable Bucket Encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
  bucket = aws_s3_bucket.my_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

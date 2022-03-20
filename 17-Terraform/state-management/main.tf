terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}  

  provider "aws" {
    region  = "us-east-1"
  }

# Storing state file in S3 bucket
   terraform {
     backend "s3" {
       bucket  = "stellu-bucket"
       key     = "state_management/terraform.tfstate"
       encrypt = true
       region  = "us-east-1"
       dynamodb_table = "StelluDB"
     }
   }

# Setting up S3 bucket for state file
resource "aws_s3_bucket" "stellu" {
  bucket = "stellu-bucket"
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.stellu.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "versioning_example" {
  bucket = aws_s3_bucket.stellu.id
  versioning_configuration {
    status = "Enabled"
  }
}

# DynamoDB Code
resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "StelluDB"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "LockID"

  attribute {
      name = "LockID"
      type = "S"
  }
}



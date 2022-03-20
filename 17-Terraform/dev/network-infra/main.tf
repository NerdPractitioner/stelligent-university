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
       key     = "dev/network-infra/state/terraform.tfstate"
       encrypt = true
       region  = "us-east-1"
       dynamodb_table = "StelluDB"
     }
   }

# Create a VPC
resource "aws_vpc" "stellu-vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "pubsub" {
  vpc_id     = aws_vpc.stellu-vpc.id
  cidr_block = "10.0.32.0/20"
  availability_zone = "us-east-1a"

  tags = {
    Name = "Public Subnet"
  }
}

resource "aws_subnet" "privsub" {
  vpc_id     = aws_vpc.stellu-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "Private Subnet"
  }
}

# locals {
#   network_cidr = "${var.network_cidr_prefix}/${var.network_cidr_suffix}"
#   network_objs = [
#     for i, n in var.subnets : {
#       name     = n.name
#       new_bits = abs(var.network_cidr_suffix - n.cidr_block)
#   }]
# }

# module "subnet_addrs" {
#   source          = "github.com/hashicorp/terraform-cidr-subnets.git?ref=v1.0.0"
#   base_cidr_block = local.network_cidr
#   networks        = local.network_objs
# }
# locals {
#     vpc_cidr = "10.0.0.0/20"
#     public_subnet_count = 2
#     public_subnet_newbits = 4
#     public_subnets_newbits_array = [
#         for i in range(local.public_subnet_count) :
#             local.public_subnet_newbits
#     ]
#     public_cidr_subnets = cidrsubnets(local.vpc_cidr, local.public_subnets_newbits_array...)
# }


# output "public_cidr_subnets" {
#     value = local.public_cidr_subnets
# }
# public_cidr_subnets = tolist([
#   "10.0.0.0/24",
#   "10.0.1.0/24",
# ])
# resource "aws_subnet" "public_subnet" {
#     count = local.public_subnet_count
#     vpc_id     = "stellu-vpc"
#     cidr_block = local.public_cidr_subnets[count.index]
# }
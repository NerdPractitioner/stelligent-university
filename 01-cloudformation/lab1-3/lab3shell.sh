#! /bin/bash

yq e '.[]' regions.yml| while read region
do
aws-vault exec temp -- aws cloudformation create-stack --stack-name holmes-sdk-demo --template-body file://./template.yml  --parameters file://./parameters.json --region $region
done
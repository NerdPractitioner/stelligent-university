aws-stellu cloudformation create-stack --stack-name holmesdemolab --template-body file://lab1-2/lab1-2.yml --parameters file://lab1-2/parameters.json --capabilities CAPABILITY_NAMED_IAM
aws-stellu cloudformation update-stack --stack-name holmesdemolab --template-body file://lab1-2-3/template.yml --parameters file://lab1-2-3/parameters.json --capabilities CAPABILITY_NAMED_IAM


aws-vault exec temp -- aws 
alias aws-stellu="aws-vault exec temp -- aws"
# Questions and Answers

## Question: Why YAML

_Why do we prefer the YAML format for CFN templates?_

### Answer:

Yaml is generally easier and faster to write and takes less characters. 
It also allows for the use of conditional logic and self referencing.
Yaml has many other dynamic features that JSON doesn't support 
and can parse json as well if needed.

#### Question: Protecting Resources

_What else can you do to prevent resources in a stack from being deleted?_

### Answer:

- You can set the deletion policy attribute to Retain or Snapshot
- You can use IAM policies to restrict users from being able to delete stack resources
- You can use stack policies to prevent updates to the stack resources
- You can enable termination protection on the stack

_How is that different from applying Termination Protection?_

### Answer:

Termination protection will cause a stack deletion to fail.
The other options seem to provide more granular control of what can and can't be deleted.
For instance, if you set the deletion policy to Retain, the stack will still be deleted but the resources will remain.

## Question: Portability

_Can you list 4 features of CloudFormation that help make a CFN template
portable code?_

##Tasks

### Task: String Substitution 

Demonstrate 2 ways to code string combination/substitution using
built-in CFN functions.

#### MyWork
`
- Fn::Join and/or !Join in Yaml allows you to combine string values and variables into a single value
-- EX. Fn::Join: [ delimiter, [ comma-delimited list of values ] ]
-- Used several times in labs for concatenating names using region, AZ, string value, etc.

- Fn::Sub and/or !Sub in Yaml allows you to do things like return a string while filling in referenced variables from elsewhere in the script
-- Used in lab 1-2-3
      ManagedPolicyArns:
        - !ImportValue
          Fn::Sub: '${StackPolicy}-policy-arn'
-- Seems to be most useful for simplifying large data structure. Example in docs provides instance UserData
    UserData:
      Fn::Base64:
        !Sub |
          #!/bin/bash -xe
          yum update -y aws-cfn-bootstrap
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchConfig --configsets wordpress_install --region ${AWS::Region}
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
`
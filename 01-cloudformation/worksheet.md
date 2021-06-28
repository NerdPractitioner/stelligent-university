# Questions and Answers

#### Question: Why YAML

_Why do we prefer the YAML format for CFN templates?_

##### Answer:

Yaml is generally easier and faster to write and takes less characters. 
It also allows for the use of conditional logic and self referencing.
Yaml has many other dynamic features that JSON doesn't support and can parse json as well if needed.

#### Question: Protecting Resources

_What else can you do to prevent resources in a stack from being deleted?_

##### Answer:

- You can set the deletion policy attribute to Retain or Snapshot
- You can use IAM policies to restrict users from being able to delete stack resources
- You can use stack policies to prevent updates to the stack resources
- You can enable termination protection on the stack 

_How is that different from applying Termination Protection?_

##### Answer: 

Termination protection will cause a stack deletion to fail.
The other options seem to provide more granular control of what can and can't be deleted.
For instance, if you set the deletion policy to Retain, the stack will still be deleted but the resources will remain.



#### Question: Portability

_Can you list 4 features of CloudFormation that help make a CFN template
portable code?_





###Tasks

#### Task: String Substitution

Demonstrate 2 ways to code string combination/substitution using
built-in CFN functions.

##### MyWork

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

#### Task: Policy Tester

Show how to use the IAM policy tester to demonstrate that the user
cannot perform 'Put' actions on any S3 buckets.

-

#### Task: SSM Parameter Store

Using the AWS Console, create a Systems Manager Parameter Store
parameter in the same region as the first Stack, and provide a value for
that parameter. Modify the first Stack's template so that it utilizes
this Parameter Store parameter value as the IAM User's name. Update the
first stack. Finally, tear it down.

- 

#### Task: DRYer Code

How reusable is your SDK-orchestration code? Did you share a single
method to load the configuration file for both stack creation/updating
(Lab 1.3.2) and deletion (Lab 1.3.3)? Did you separate the methods for
finding existing stacks from the methods that create or update those stacks?

If not, refactor your Python, Ruby or NodeJS scripts to work in the
manner described.

- My code can uses python sys.argz to take arguments at runtime. I used the following:
- python pythonstack.py deploy holmes-demo regions.json template.yml parameters.json
- - Note - the first argument will delete if you specify delete, any other argument will deploy which isn't great
- - The code also requires that the template, parameters and regions files be in the same directory currently
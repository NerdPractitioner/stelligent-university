#### Question: Why YAML

_Why do we prefer the YAML format for CFN templates?_

#### Question: Protecting Resources

_What else can you do to prevent resources in a stack from being deleted?_

See [DeletionPolicy](https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-accidental-updates/).

_How is that different from applying Termination Protection?_

#### Task: String Substitution

Demonstrate 2 ways to code string combination/substitution using
built-in CFN functions.

#### Task: Policy Tester

Show how to use the IAM policy tester to demonstrate that the user
cannot perform 'Put' actions on any S3 buckets.

#### Task: SSM Parameter Store

Using the AWS Console, create a Systems Manager Parameter Store
parameter in the same region as the first Stack, and provide a value for
that parameter. Modify the first Stack's template so that it utilizes
this Parameter Store parameter value as the IAM User's name. Update the
first stack. Finally, tear it down.
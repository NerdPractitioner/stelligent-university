# Questions and Answers
## Question 0.1.1: 1

What method did you use to store the aws credentials?  What are some other options?

### Answer 1
Using aws-vault was the easiest for me.
I attempted to automate setting the environment variables in bash but that isn't a strong area of mine.
I was able to use aws configure set commands to set the access and secret access keys
but I believe this requires the aws config and credentials files to exist already.
I could do some conditional logic to check if those exist and create them using bash if I put more time into it.

## Question 0.1.1: 2

Which AWS environment variable cannot be set in order to run the
`aws sts get-session-token` command?

### Answer 2
When I tried setting an mfa token in my profile it seemed to cause issues when I tried cli commands.
I'm assuming because the token will be expired by the time you try to use it.

## Question: Environments
Running the two commands in lab 0.1.1 and lab 0.1.3 should have shown the same results.
What does this tell you about the access the keys give you on your laptop and the access you have in the Cloud9 environment?
What other methods are there to provide this level of access without using keys?

### Answer 3
The Cloud9 environment doesn't need to verify an mfa token to run cli commands.
I'm assuming this is because it has its own resource access policy associated.
I had to do some minor networking work to set it in a public vpc subnet but it wasn't necessary to manage any profiles or keys.
I'm not sure how else you would give this level of access to an mfa enabled account that wouldn't require token verification.

## helloworld app explaination
This is a django python app. 
There is a virtual environment in the file structure that you can use to make migrations and run a server to demo.
I can include more detailed instructions if needed.
I set amazonaws.com as an allowed-host so it can be ran from cloud9 which was something new I learned about.
Cloud9 will provide an IP address for you to visit that simulates localhost.
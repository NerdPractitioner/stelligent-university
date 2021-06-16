### Question 0.1.1: 1

What method did you use to store the aws credentials?  What are some other options?

#### Answer
Using aws-vault was the easiest for me. I attempted to automate setting the environment variables in bash but that isn't a strong area of mine. I was able to use aws configure set commands to set the access and secret access keys but I believe this requires the aws config and credentials files to exist already. I could do some conditional logic to check if those exist and create them using bash if I put more time into it. 


### Question 0.1.1: 2

Which AWS environment variable cannot be set in order to run the
`aws sts get-session-token` command?

#### Answer 
When I tried setting an mfa token in my profile it seemed to cause issues when I tried cli commands. I'm assuming because the token will be expired by the time you try to use it. 


## helloworld app explaination
This is a django python app. There is a virtual environment in the file structure that you can use to make migrations and run a server to demo. I can include more detailed instructions if needed. I set amazonaws.com as an allowed-host so it can be ran from cloud9 which was something new I learned about. Cloud9 will provide an IP address for you to visit that simulates localhost.
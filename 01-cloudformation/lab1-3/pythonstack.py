
import boto3
import sys
import json

region_list = region_parser("./regions.json")
cf_client = boto3.client('cloudformation')

bucket_name = "region, accountid, bucketname"

s3_client = boto3.client('s3', region_name=region)
def deploy_stack(create_or_update, template_location, parameter_location, capabilities):
    if stack_exists():
        result = cf_client.update_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Parameters=parameters,
            Capabilities="CAPABILITY_NAMED_IAM"
        )


def stack_exists(client, stack_name):
    stacks = client.list_stacks()['StackSummaries']
    for stack in stacks:
        if stack['StackStatus'] == 'DELETE_COMPLETE':
            continue
        if stack_name == stack['StackName']:
            return True
    return False

def region_parser(file_location):
    f = open(file_location)
    data = json.load(f)
    demo_regions = data['regions']
    f.close()
    return demo_regions
    
    # s3client.create_bucket(Bucket=bucket_name)


def delete_stack(client, stack_name) -> None:
    response = client.delete_stack(
    StackName=stack_name
    )

def create_regional_clients(regions_list):
	clients = []
	for region in regions_list:
		client = boto3.client('cloudformation', region_name=region)
		clients.append(client)
	return clients

def _init():
    #Check for arguments
	if len(sys.argv) < 5:
		print("Missing arguments. \nUsage: ./pythonstack.py <action-desired> <stack-name> <regions-json> <template-yaml>")
		exit()
        action_desired = sys.argv[1]
        stack_name = sys.argv[2]
        regions_file = sys.argv[3]
        template_file = sys.argv[4]

	#parse JSON data from regions file
	regions_list = region_parser(regions_file)

	#create list of boto clients for each region
	regional_clients = create_regional_clients(regions_list)

	for index, client in enumerate(regional_clients):
		# generate full name for stack with the format <region>-<friendly-name>
		full_stack_name = "-".join([regions_list[index], stack_name])
		
		if stack_exists(full_stack_name, client):
			# Check if delete flag was specified in the end
			if action_desired == "delete":
				delete_stack(full_stack_name, client)		
			else:
				deploy_stack(full_stack_name, template_file, client, stack_name)


if __name__ == "__main__":
    _init()

#!/usr/bin/env python3

import boto3
import sys
import json

bucket_name = "region, accountid, bucketname"
#s3_client = boto3.client('s3', region_name=region)

def deploy_stack(cf_client, cf_template, verbose_stack_name, parameters):
    if stack_exists(cf_client, verbose_stack_name):
        response = cf_client.update_stack(
            StackName=verbose_stack_name,
            TemplateBody=cf_template,
            Parameters=parameters,
            Capabilities=["CAPABILITY_NAMED_IAM"]
        )
    else:
        response = cf_client.create_stack(
            StackName=verbose_stack_name,
            TemplateBody=cf_template,
            Parameters=parameters,
            Capabilities=["CAPABILITY_NAMED_IAM"]
        )


def stack_exists(cf_client, stack_name):
    stacks = cf_client.list_stacks()['StackSummaries']
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

def delete_stack(cf_client, verbose_stack_name):
    response = cf_client.delete_stack(
    StackName=verbose_stack_name
    )

def make_clients(preferred_regions):
	clients = []
	for region in preferred_regions:
		cf_client = boto3.client('cloudformation', region_name=region)
		clients.append(cf_client)
	return clients
	
def parameter_parser(parameter_location):
    f = open(parameter_location)
    parameters = json.load(f)
    f.close()
    return parameters

def template_parser(template_location):
	with open(template_location) as fileobj:
		template_body = fileobj.read()
	return template_body

def main():
    if len(sys.argv) < 6:
        print("Missing arguments")
        exit()
        
    action_desired = sys.argv [1]
    stack_name = sys.argv[2]
    regions_file = sys.argv[3]
    template_location = sys.argv[4]
    parameter_location = sys.argv[5]
    
    cf_template = template_parser(template_location)
    preferred_regions = region_parser(regions_file)
    regional_clients = make_clients(preferred_regions)
    parameters = parameter_parser(parameter_location)
    
    for index, cf_client in enumerate(regional_clients):
        verbose_stack_name = "-".join([preferred_regions[index], stack_name])
        if action_desired == "delete":
            delete_stack(cf_client, verbose_stack_name)
        else: deploy_stack(cf_client, cf_template, verbose_stack_name, parameters)



if __name__ == "__main__":
    main()

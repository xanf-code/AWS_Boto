# ------------------------------------------------------------------
# IP Set CRUD Operation (Create, Update, List, Delete) - done
# Rule Groups (RateBasedStatement) (CRUD) - (Update same as create)
# Rules - 
# ------------------------------------------------------------------

import boto3

waf_client = boto3.client('wafv2')

IP_SET_LIST = ['0.0.0.0/32', '192.0.2.44/32']

GROUP_RULES = [
    {
        'Name' : 'test-rate-based-rules',
        'Priority' : 1,
        'Statement' : {
            'RateBasedStatement' : {
                'Limit' : 100,
                'AggregateKeyType' : 'IP',
            }
        },
        'Action' : {
            'Count' : {},
        },
        'VisibilityConfig': {
            'SampledRequestsEnabled': True,
            'CloudWatchMetricsEnabled': True,
            'MetricName': 'test-metric'
        },
    }
]

visibility_config = {
    'SampledRequestsEnabled': True,
    'CloudWatchMetricsEnabled': True,
    'MetricName': 'test-metric'
}

def create_ip_sets(ip_set_name,ip_set_scope,ip_version,ip_addresses):
    waf_client.create_ip_set(
        Name= ip_set_name,
        Scope = ip_set_scope,
        IPAddressVersion = ip_version,
        Addresses = ip_addresses
    )
    
    print("IP Set " + ip_set_name + " Created!")
    
def get_ip_set(ip_set_name,ip_set_scope,ip_set_id):
    response = waf_client.get_ip_set(
        Name = ip_set_name,
        Scope = ip_set_scope,
        Id = ip_set_id
    )
    return response

def update_ip_set(ip_set_name,ip_set_scope,ip_set_id,ip_addresses):
    token_meta = get_ip_set(ip_set_name,ip_set_scope,ip_set_id)
    waf_client.update_ip_set(
        Name=ip_set_name,
        Scope=ip_set_scope,
        Id= ip_set_id,
        Addresses=ip_addresses,
        LockToken=token_meta["LockToken"]
    )
    
    print("Updated Successfully!!")

def create_group(group_name,group_scope,group_capacity,group_rules):
    waf_client.create_rule_group(
        Name = group_name,
        Scope = group_scope,
        Capacity = group_capacity,
        Rules = group_rules,
        VisibilityConfig = visibility_config
    )
    print("Rule group created!!")
  
def get_group(group_name,group_scope,group_id,group_arn):
    response = waf_client.get_rule_group(
        Name = group_name,
        Scope = group_scope,
        Id = group_id,
        ARN = group_arn
    )
    print(response)
    return response
  
def delete_group(group_name,group_scope,group_id,group_arn):
    group_rule_meta = get_group(group_name,group_scope,group_id,group_arn)
    waf_client.delete_rule_group(
        Name = group_name,
        Scope = group_scope,
        Id = group_id,
        LockToken = group_rule_meta["LockToken"]
    )
    print("Group Rule Deleted!")
    
# create_ip_sets('test-set-1', 'REGIONAL', 'IPV4', IP_SET_LIST)
# get_ip_set('test-set-1', 'REGIONAL','16d33e7f-8a27-4f9d-b882-be969efe6356')
# update_ip_set('test-set-1', 'REGIONAL','16d33e7f-8a27-4f9d-b882-be969efe6356',['0.1.1.2/32'])
create_group('test-group-1','REGIONAL', 100, GROUP_RULES)
# get_group('test-group-1','REGIONAL','a1e1c0e1-8aee-414a-90f1-37927c2cf3e9','arn:aws:wafv2:ap-south-1:212291066577:regional/rulegroup/test-group-1/a1e1c0e1-8aee-414a-90f1-37927c2cf3e9')
# delete_group('test-group-1','REGIONAL','a1e1c0e1-8aee-414a-90f1-37927c2cf3e9','arn:aws:wafv2:ap-south-1:212291066577:regional/rulegroup/test-group-1/a1e1c0e1-8aee-414a-90f1-37927c2cf3e9')
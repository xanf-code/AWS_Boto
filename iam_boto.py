# ---------------------------------------- #
# Create a user - done
# Create a group - done
# Add user to the group - done
# Remove user from the group - done
# Get the group - done
# Attach policies to that group - done
# Detach group policies - done
# ---------------------------------------- #

from multiprocessing import current_process
from webbrowser import get
import boto3

iam = boto3.resource('iam')
iam_client = boto3.client('iam')

def create_user(userName):
    iam.create_user(
        UserName = userName
    )

def get_current_user():
    current_user = iam.CurrentUser()
    return current_user.user_name

def get_group(name):
    group = iam.Group(name)
    return group

def create_group(group_name):
    iam.create_group(
        GroupName=group_name,
    )
    
def attach_group_policies(grp_name,policy_arn):
    iam_client.attach_group_policy(
        GroupName = grp_name,
        PolicyArn = policy_arn
    )
    print("Policy Attached")
    
def detach_group_policies(grp_name,policy_arn):
    iam_client.detach_group_policy(
        GroupName = grp_name,
        PolicyArn = policy_arn
    )
    print("Policy Detached")
    
def add_user_group(groupName,UserName):
    get_group_name = get_group(groupName)
    get_group_name.add_user(
        UserName = UserName
    )
     
def remove_user_group(groupName,UserName):
    iam_client.remove_user_from_group(
        GroupName = groupName,
        UserName = UserName
    )
    print("User " + UserName + " removed from " + groupName)

def getUser():
    current_user = get_current_user()
    print("Current User: "+ current_user)

# create_user("Darsh_test")

# create_group("Darsh-Group")

# add_user_group("Demo-Group","Darsh_test")

# remove_user_group("Demo-Group", "Darsh_test")

# attach_group_policies("Darsh-Group","arn:aws:iam::aws:policy/AmazonS3FullAccess")

# detach_group_policies("Darsh-Group", "arn:aws:iam::aws:policy/AmazonS3FullAccess")
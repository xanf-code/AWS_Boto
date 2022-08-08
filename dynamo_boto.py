import boto3

db = boto3.resource('dynamodb')
table = db.Table("employee")

emp_ob = {
    "empID" : "3",
}

def add_items(employee_object):
    table.put_item(
    Item=employee_object
)

def get_items():
    response = table.get_item(
        Key={
            'empID' : "2"
        }
    )
    item = response['Item']
    print(item)

def delete_items(key_obj) :
    table.delete_item(
        Key=key_obj
    )    
    
delete_items(emp_ob)

# get_items()

# #Get Item
# response = table.get_item(
#     Key={
#         'empID' : '3',
#         'name' : 'Rahul'
#     }
# )
# print(response)
# item = response['Item']
# print(item)
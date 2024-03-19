from chalice import Chalice
import boto3
from database.dynamodb import DynamoDB
from aws_services import AWSServices

app = Chalice(app_name='AwsServices')

# Calling the DynamoDB class to create the table
dynamo_resource = boto3.resource('dynamodb')
dynamo_db = DynamoDB(dynamo_resource)
aws_services = AWSServices()

@app.route('/sign-up', methods=['POST'], cors=True)
def sign_up():
    request = app.current_request
    body = request.json_body
    return dynamo_db.signUp(body)


@app.route('/login', methods=['POST'], cors=True)
def login():
    request = app.current_request
    return dynamo_db.login(request.json_body)


@app.route('/addCommunity', methods=['PUT'], cors=True)
def index():
    request = app.current_request
    dynamo_db.putCommunity(request.json_body)
    return {'message': 'Community added successfully!'}


@app.route('/getCommunity/{user_name}', methods=['GET'], cors=True)
def get_community(user_name):
    return dynamo_db.getCommunity(user_name)

@app.route('/joinCommunity', methods=['GET'], cors=True)
def join_community():
    # requires a user_name and community_id
    request = app.current_request
    return dynamo_db.join_community(request.json_body)

@app.route('/leaveCommunity', methods=['GET'], cors=True)
def leave_community():
    # requires a user_name and community_id
    request = {
        "community_id": 11,
        "user_name": "ALI"
    }
    print(request)
    return dynamo_db.leave_community(request)


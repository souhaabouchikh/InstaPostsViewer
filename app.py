from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Define a handler function for serverless invocation
def handler(event, context):
    try:
        # Handle HTTP requests
        if event.get('httpMethod') == 'GET':
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Hello from Flask!'})
            }
        else:
            return {
                'statusCode': 405,
                'body': json.dumps({'error': 'Method Not Allowed'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

# For local development, use the Flask app as usual
@app.route('/', methods=['GET'])
def index():
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run(debug=True)

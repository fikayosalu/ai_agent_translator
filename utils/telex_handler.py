import json
from flask import request

def parse_telex_request(req):
    """Parse incoming JSON-RPC request from Telex."""
    try:

        # Access the message content by drilling down through nested keys
        user_text = req['params']['message']['parts'][0]['text']
        return user_text.strip()
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error extracting text from RPC request structure: {e}")
        return None

def telex_response(result, request_id=1):
    """Format JSON-RPC compliant response."""
    return {
        "jsonrpc": "2.0",
        "result": result,
        "id": request_id
    }

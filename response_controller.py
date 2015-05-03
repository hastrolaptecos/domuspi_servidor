from flask import Response
import json

class ResponseController:
  @staticmethod
  def json_response(obj):
    # return Response(json.dumps(obj), 200)
    return Response(json.dumps(obj), 200, {'Content-type: text/json'})
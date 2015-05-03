from flask import Response
import json

class ResponseController:
  @staticmethod
  def json_response(obj):
    return Response(json.dump(obj), 200, {'Content-type: text/json'})
from rest_framework import renderers
import json
class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_types, renderer_context):
        response = ""
        if 'ErrorDetial' in str(data):
            response = json.dumps({'error':data})
        else :
            response = json.dumps(data)
        return response
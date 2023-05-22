from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import xmltodict
import json


def convert_to_json(data):
    convert = xmltodict.parse(data.text)
    result = json.dumps(convert)
    return json.loads(result)


@api_view(["GET"])
def vuln_results(request):
    url = "https://qualysapi.qg2.apps.qualys.eu/api/2.0/fo/asset/host/vm/detection"
    headers = {"X-Requested-With": "Curl"}
    # your credentials
    auth = ()
    params = {"action": "list"}
    xml_result = requests.get(url=url, params=params, headers=headers, auth=auth)
    return Response(convert_to_json(xml_result))
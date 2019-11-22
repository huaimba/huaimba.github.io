# encoding=utf-8
# @安全北北

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import json
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

@csrf_exempt
@xframe_options_exempt
def vuln_alert_dingding(request):
	dingding_access_token = 'xxx'
	dingding_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % dingding_access_token
	
	headers = {'Content-Type': 'application/json;charset=utf-8'}
	xray_json_data = json.loads(request.body)
	url = xray_json_data.get('target').get('url')
	plugin = xray_json_data.get('plugin')
	vuln_class = xray_json_data.get('vuln_class')

	send_json_data = {
		"msgtype": "markdown",
		"markdown": {
			"title":"新漏洞预警",
			"text": "#发现新漏洞" +  "  \n漏洞分类：" +  vuln_class + "  \n扫描插件：" + plugin + "  \n漏洞url：" + url + "  \n"
			},
	}

	make_request = requests.post(dingding_webhook, data=json.dumps(send_json_data),headers=headers)
	return HttpResponse(1)

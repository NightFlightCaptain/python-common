# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'
from urllib import request, parse

import requests
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':
    target = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    Form_Data = {}
    Form_Data['i'] = 'doing what'

    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1540644119071'
    Form_Data['sign'] = 'abfea8a830c133d356948480043ea7fb'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTION'
    Form_Data['typoResult'] = 'false'

    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(target, data)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    print(translate_results)
    print("****************")
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print(translate_results)


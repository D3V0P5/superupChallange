#!/usr/bin/env python

from bottle import route, run, template
import boto3




@route('/secret')
def index():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('devops-challenge')
    co = table.get_item(Key = {"code_name" : "thedoctor"})['Item']['secret_code']
    return template('{ secret_code: "{{code}}"}', code=co)

@route('/')
@route('/health')
def health():
    return '''{ status: healthy, container: https://hub.docker.com/r/d3v0p5/superup_devops_ch/ , project: https://github.com/D3V0P5/superupChallange }'''



run(host='0.0.0.0', port=5000)

'''
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
'''

#print(table.get_item(Key = {"code_name" : "thedoctor"})['Item']['secret_code'])

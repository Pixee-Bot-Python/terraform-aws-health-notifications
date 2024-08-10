#!/usr/bin/python

import os
from decimal import Decimal
import time
import requests
from calendar import timegm

SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK")
ACCOUNT_NAME = os.environ.get("ACCOUNT_NAME")
ACCOUNT_NUMBER = os.environ.get("ACCOUNT_NUMBER")
CUSTOMER_NAME = os.environ.get("CUSTOMER_NAME")


def lambda_handler(event, context):
  print(event)
  notify_slack(
    customer=CUSTOMER_NAME,
    account=ACCOUNT_NAME,
    account_number=ACCOUNT_NUMBER,
    region=event['region'],
    title=event['detail']['eventTypeCode'],
    description=event['detail']['eventDescription'][0]['latestDescription'],
    start_time=event['detail']['startTime'],
    end_time=event['detail']['endTime'],
    affected_resources=", ".join(event['resources']),
    event_type=event['detail']['eventTypeCategory'],
    service=event['detail']['service'],
    webhook=SLACK_WEBHOOK
  )

def to_timestamp(date_string):
  timestamp = timegm(
    time.strptime(
      date_string.replace('Z', 'GMT'),
      '%Y-%m-%dT%H:%M:%S%Z'
    )
  )
  return timestamp

def notify_slack(customer, account, account_number, region, title, description, start_time, end_time, affected_resources, event_type, service, webhook):
  print("Notify via Slack")
  message = {
    'attachments': [{
      'fallback': title,
      'color': "warning",
      'author_name': 'Amazon Health Notifications',
      'text': description,
      'fields': [
        {
          'title': 'Type',
          'value': title,
          'short': False,
        },
        {
          'title': 'Customer',
          'value': customer,
          'short': True,
        },
        {
          'title': 'Region',
          'value': region,
          'short': True,
        },
        {
          'title': 'Account Name',
          'value': account,
          'short': True,
        },
        {
          'title': 'Account Number',
          'value': account_number,
          'short': True,
        },
        {
          'title': 'Affected Service',
          'value': service,
          'short': True,
        },
        {
          'title': 'Event Type',
          'value': event_type,
          'short': True,
        },
        {
          'title': 'Start Date/Time',
          'value': start_time,
          'short': True,
        },
        {
          'title': 'End Date/Time',
          'value': end_time,
          'short': True,
        },
        {
          'title': 'Affected Resources',
          'value': affected_resources,
          'short': False,
        },
      ]
    }]
  }

  response = requests.post(webhook, json=message, timeout=60)
  if response.status_code != 200:
    raise ValueError("Slack wouldn't speak to me, I got this back" % response.text)

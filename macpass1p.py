#!/usr/bin/env python

import os
import logging

import ConfigParser
import argparse
from jinja2 import Environment, PackageLoader
from bs4 import BeautifulSoup

# Helper
def normalize(s):
  return '"%s"' % s.replace('"', '""')

# Setup logging
script_name = os.path.splitext(os.path.basename(__file__))[0]
logging.basicConfig()
logger = logging.getLogger(script_name)
logger.setLevel(logging.DEBUG)

# Parse command line options
parser = argparse.ArgumentParser(
    description='Converts MacPass XML file to 1Password CSV')
parser.add_argument('--version', action='version', version='%(prog)s 0.2.0')
args = parser.parse_args()

# Read config file
config = ConfigParser.SafeConfigParser()
config.read(os.path.join('etc', 'settings.conf'))

passwords_xml = BeautifulSoup(open(config.get('General', 'input')), 'lxml')
logger.info('MacPass XML file is opened')

passwords = []

for entry in passwords_xml.find_all('entry'):
  password = {}
  # tag fields
  fields = {}

  for tag in entry.find_all('string'):
      fields[tag.key.string.lower()] = tag.value.string

  password['title'] = normalize(fields['title'])
  password['username'] = normalize(fields['username'])
  password['password'] = normalize(fields['password'])
  password['url'] = normalize(fields['url'].replace('http://', ''))
  password['notes'] = normalize(fields['notes'])

  passwords.append(password)

# Prepare output file
env = Environment(loader=PackageLoader('__main__', 'templates'))
template = env.get_template('passwords.tmpl')
output = open(config.get('General', 'output'), 'w')
output.write(template.render(passwords = passwords).encode('utf-8'))
output.close()

logger.info('1Password CSV file is written')

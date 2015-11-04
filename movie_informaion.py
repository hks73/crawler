#!/usr/bin/env python
import omdb
import json
import sys
# print sys.argv[1]
x=sys.argv[1]
res = omdb.request(t=x)
xml_content = res.content
parsed = json.loads(xml_content)

# print parsed
print "Name :",parsed["Title"]
print "Type :",parsed["Type"]
print "Year :",parsed["Year"]
print "Language :",parsed["Language"]
print "Cast :",parsed["Actors"]
print "Plot :",parsed["Plot"]


#!/usr/bin/env python
import omdb
import json
t=raw_input()
res = omdb.request(t)
xml_content = res.content
parsed = json.loads(xml_content)

print "Name :",parsed["Title"]
print "Type :",parsed["Type"]
print "Year :",parsed["Year"]
print "Language :",parsed["Language"]
print "Cast :",parsed["Actors"]
print "Plot :",parsed["Plot"]


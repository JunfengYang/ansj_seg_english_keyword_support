#!/usr/bin/python
#-*- coding: utf-8 -*-

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from  datetime  import  *
import time


class WIKIDictXMLParse:
    def __init__(self):
        self.filePath = "enwiktionary-latest-pages-articles.xml"
        
    def iterparseXML(self):
        count = 0
        docId = ""
        url = ""
        content = ""
        timestamp = ""
        lastModified = ""
        title = ""
        fo = open("dic","w")
        for event, elem in ET.iterparse(self.filePath):
            if event == 'end':
                #print elem.tag,elem.text
                if elem.tag.find("title") > -1:
                    #title = elem.text
                    #print elem.text
                    if elem.text.find(":") < 0:
                        if elem.text.find("-") > -1:
                            title = elem.text.encode("utf-8")+"\n"
                        elif elem.text.find(" ") > -1:
                            title = elem.text.encode("utf-8")+"\n"
                    
                # if elem.tag.find("timestamp") > -1:
                #     lastModified = elem.text
                if elem.tag.find("text") > -1:
                    if elem.text:
                        if elem.text.find("==English==") > -1:
                            if title != "":
                                fo.write(title)
                    title = ""
                #     content = elem.text
                # if elem.tag.find("page") > -1:
                #     count += 1
                #     print "---------------------"
                #     print title, timestamp
                #     print text
                #     docId = "http://zh.wikipedia.org/wiki/" + title
                #     url = docId
                #     timestamp = datetime.utcnow().isoformat() + 'Z'
                #     del content, lastModified, timestamp, title
                
                # if count > 100:
#                     break
            elem.clear() # discard the element
        fo.close()
        print count


if __name__ == '__main__':
    parser = WIKIDictXMLParse()
    parser.iterparseXML()

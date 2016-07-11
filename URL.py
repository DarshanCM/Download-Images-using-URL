import sys
import xml.sax


class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.Key = ""
      #self.LastModified = ""

   sys.stdout=open("test.txt","a")
   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "contents":
         print "*****Movie*****"
         title = attributes["key"]
         print "key:", title
   
   sys.stdout=open("test.txt","a")
   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "Key":
         print "http://s3.amazonaws.com/dunzo2/" + self.type 
     
   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "Key":
         self.type = content
     
     
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("imageslink.xml")




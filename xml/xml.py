# XML Parser Architectures and APIs
'''
Simple API for XML (SAX):
    Here, you register callbacks for events of interest and then let the parser proceed through 
    the document. This is useful when your documents are large or you have memory limitations, it parses 
    the file as it reads it from disk and the entire file is never stored in memory.

    Is a stream-based processor. You only have a tiny part in memory at any 
    time and you "sniff" the XML stream by implementing callback code for events like tagStarted() etc. 
    It uses almost no memory, but you can't do "DOM" stuff, like use xpath or traverse trees.

Document Object Model (DOM) API: 
    This is a World Wide Web Consortium recommendation wherein the entire file is read into memory 
    and stored in a hierarchical (tree-based) form to represent all the features of an XML document.

    You load the whole thing into memory. it's a massive memory hog. You can blow memory with even medium 
    sized documents. But you can use xpath and traverse the tree etc.
'''


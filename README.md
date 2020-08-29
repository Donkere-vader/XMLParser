# XMLParser
A XMLParser written by me.
It's probably not so good/ clean good. And probably not the best way to do it. But this is my first parser. So don't go to hard on me :)).

## Reliabillity
This is a very simple module and not tested that much, I'm going to use this in my own project but There is a big chance that there are some reliabillity issues with different forms of formatting and such.

Please repport any issues you encounter.

### Known issues :bug:
- when assinging a value to an attribute and the value contains a '=', if there are any spaces surrounding the '=' those will be removed.
- the escape character doesn't escape the ' and " characters

### Supported format
The following situations are all supported by the module.  

Oneliners:  
``<root><text></text></root>``

Spaces between the = with attributes:  
``<root name = "main root thinige">``

self closing:  
``<item />``

## Installation
Move the XMLParser file into the folder with your python modules
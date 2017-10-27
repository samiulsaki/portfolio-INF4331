#!/usr/bin/env python3

# The parser.py script runs and finds all the mathces in markdown text using regexes.
# The scripts does the following conversions (from markdown to html):
# Markdown Text                                  |           HTML Text
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Italic = '*text*'                              |           <i>text</i>
# Bold = '%text%'                                |           <b>text</b>
# '\%' or '\*'                                   |           % or *
# Blockquote = '>> text'                         |           <blockquote> text </blockquote> 
# Hyperlink = '[text](url)'                      |           <a href='url'>text</a> (url with www gets http://)
# ImageURL = '<imageURL>(w=WIDTH, h=HEIGHT)'     |           <img src="imageURL" style="width:WIDTHpx;height:HEIGHTpx;">
# WikipediaQuery = '[wp:QUERY]'                  |           <a href="https://en.wikipedia.org/w/index.php?title=Special:Search&search=query>QUERY</a>
# 
# Diclaimer:
# I haven't created any test file. Users can easily insert their string as input.



import os,sys,re


out=[]
output=[]

def parse_nwodkram(text):
    for line in text.splitlines():
        temp_list=[]
        #block_list =[]    
        out.append(line)    
        if re.search('\>>',line):
            regex = r'\>>'
            #print(line)
            #original = len(re.findall(regex,line)) + 1
            convert = "<blockquote>" 
            blockquote = re.sub(regex, convert, line ) + " </blockquote>"
            temp_list.append(blockquote)

        elif re.search(r"\[([\w\D\d].*)\](\()((w{3}\.)|(http://)|(https://))([a-z\w\d:#@%/;$()~_?\+-=\\\.&\d])*?(.*)(\))",line):
            #print(line)
            fr_link = line.find(r'(') + 1
            to_link = line.find(r')', fr_link)
            fr_name = line.find(r'[') + 1
            to_name = line.find(r']', fr_name)
            link = line[fr_link:to_link]
            link_name = line[fr_name:to_name]
            if re.search(r'^www', link):
                hyperlink = "<a href=\'http://"+link+"\'>"+link_name+"</a>"
            else:
                hyperlink = "<a href=\'"+link+"\'>"+link_name+"</a>"
            temp_list.append(hyperlink)

        elif re.search(r"\<(https?):((//)|(\\\\))+.*\>",line):
            fr_link = line.find(r'<') + 1
            to_link = line.find(r'>', fr_link)
            fr_width = line.find(r'w=') + 2
            to_width = line.find(r',', fr_width)
            fr_height = line.find(r'h=') + 2
            to_height = line.find(r',', fr_height)
            link = line[fr_link:to_link]
            link_width = line[fr_width:to_width]
            link_height = line[fr_height:to_height]
            imageURL = '<img src="'+link+'" style="width:'+link_width+'px;height:'+link_height+'px;">'
            temp_list.append(imageURL)

        elif re.search(r'\[wp:', line):
            fr_query = line.find(r'wp:') + 3
            to_query = line.find(r']', fr_query)
            link_query = line[fr_query:to_query]
            wp_query = '<a href="https://en.wikipedia.org/w/index.php?title=Special:Search&search='+link_query+">"+link_query+"</a>"
            temp_list.append(wp_query)
        
        for i in out[-1:]:
            
            if (i is not "") and ('>>' not in i) and ('http' not in i) and ('www' not in i) and ('wp:' not in i):                
                for j in i.split():
                    if re.search(r"\*(.*)\*",j):
                        regex = '*'
                        fr = j.find(regex) + 1
                        to = j.find(regex, fr)
                        original = '\*'+ j[fr:to] + '\*'
                        convert = "<i>"+ j[fr:to] + "</i>"
                        italic = re.sub(original, convert , j)
                        temp_list.append(italic)
                                            
                    elif re.search(r"\%(.*)\%",j):
                        regex = '%'
                        fr = j.find(regex) + 1
                        to = j.find(regex, fr)
                        original = '\%'+ j[fr:to] + '\%'
                        convert = "<b>"+ j[fr:to] + "</b>"
                        bold = re.sub(original, convert , j)
                        temp_list.append(bold)
                    
                    elif re.search(r"(\\)(\*|\%)",j):
                        #print(j)
                        regex = '\\'
                        backslash = re.sub(r'\\', '', j)
                        #print(backslash)
                        temp_list.append(backslash)

                    else:
                        temp_list.append(j)
                        
        temp=' '.join(temp_list)
        output.append(temp)
    
    result = '\n'.join(output)
    return result


if __name__ == "__main__":
    sample_string = r"""    
This is some Nwodkram text. Note that *this* is in italic, and %this% is in bold.
If you want to write an \* or an equal sign and not have the parser eat them, 
that's easy -  note that \* this \* is not in italic even though it's between two \*s,
and \% this \% is not in bold.

>> This is a Quoteline
>> This is in *italic* and in blockquote, but blockquote excape the italic marks

[here](www.google.com) is a hyperlink.
[here](http://www.google.com) is another.
[and here](https://www.weird?$|site.weird/path/) is a third with some weird characters.
Follow it at your own peril.

Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
But don't worry too much if some weird combination is ambiguous or results in
weird stuff.

This is an image:
<https://www.python.org/static/community_logos/python-logo-master-v3-TM.png>(w=600, h=200)

This is a wikipedia query:
[wp:matrix]    

    """

    # Main Program
    os.system('clear')
    print('Main Program Started')
    print('--------------------\n')
    usr_input = input('Enter your own string (just paste single lines) or leave it blank for default : ')
    if usr_input is not "":
        sample_string = usr_input
        print(sample_string)
        print('\nThese are the scraped emails from the String (user input) : \n',parse_nwodkram(sample_string))
    else:
        print(sample_string)
        print('\nThese are the scraped emails from the String (default) : \n',parse_nwodkram(sample_string))
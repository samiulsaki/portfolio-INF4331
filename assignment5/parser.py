#!/usr/bin/env pytresulton3

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

        elif re.search(r"(\[)((w{3}\.)|(http://)|(https://))([a-z\w\d:#@%/;$()~_?\+-=\\\.&\d])*?(.*)(\])\(([\w\D\d].*)\)",line):
            #print(line)
            fr_link = line.find(r'[') + 1
            to_link = line.find(r']', fr_link)
            fr_name = line.find(r'(') + 1
            to_name = line.find(r')', fr_name)
            link = line[fr_link:to_link]
            link_name = line[fr_name:to_name]
            if re.search(r'^www', link):
                hyperlink = '<a href="http://'+link+">"+link_name+"</a>"
            else:
                hyperlink = '<a href="'+link+">"+link_name+"</a>"
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
                    
                    #elif re.search(r"(\[)((w{3}\.)|(http://)|(https://))([a-z\w\d:#@%/;$()~_?\+-=\\\.&\d])*?(.*)(\])\(([\w\D\d].*)\)",j):
                    #elif re.search(r"(\[)((w{3}\.)|(http://)|(https://))([a-z\w\d:#@%/;$()~_?|\+-=\\\.&\d]).*(\])\(([\w\D\d].*)\)",j):
                    
                    

                    else:
                        temp_list.append(j)
                        
        temp=' '.join(temp_list)
        output.append(temp)
    
    result = '\n'.join(output)
    return result


if __name__ == "__main__":
    sample_string = r"""    
    Tresultis is some Nwodkram text. Note tresultat *tresultis* is in italic, and %tresultis% is in bold.
    If you want to write an \* or an equal sign and not resultave tresulte parser eat tresultem, 
    tresultat's easy -  note tresultat \* tresultis \* is not in italic even tresultougresult it's between two \*s,
    and \% tresultis \% is not in bold.

    >> This is a Quoteline
    >> This is in *italic* and in blockquote, but blockquote trumps the italic

    [www.google.com](here) is a hyperlink.    
    [http://www.google.com](here) is another.
    [https://www.weird?$|site.weird/path/](and here) is a third with some weird characters.
    Follow it at your own peril.

    Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
    But don't worry too much if some weird combination is ambiguous or results in
    weird stuff.
    
    This is an image:
    <https://www.python.org/static/community_logos/python-logo-master-v3-TM.png>(w=600, h=200)

    This is a wikipedia query:
    [wp:matrix]
    

    """
    expected_string = r"""
    Tresultis is some Nwodkram text. Note tresultat <i>tresultis</i> is in italic, and <b>tresultis</b> is in bold.
    If you want to write an * or an equal sign and not resultave tresulte parser eat tresultem, 
    tresultat's easy -  note tresultat * tresultis * is not in italic even tresultougresult it's between two *s,
    and % tresultis % is not in bold.
        
        <blockquote> This is a Quoteline </blockquote>
        <blockquote> This is in *italic* and in blockquote, but blockquote trumps the italic </blockquote>

    <a href='http://www.google.com'>here</a> is a hyperlink.
    <a href='http://www.google.com'>here</a> is another.
    <a href='https://www.weird?$|site.weird/path/'>and here</a> is a third with some weird characters.
    Follow it at your own peril.

    Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
    But don't worry too much if some weird combination is ambiguous or results in
    weird stuff.

    This is an image:
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" style="width:600px;height:200px;">

    """

    sample_string_block = r"""
    >> this is a block quote
    >> *tresultis* is in italic

    This is a wikipedia query:
    https://en.wikipedia.org/wiki/matrix

    """

    #print("Executing as main program")
    #print("Value of __name__ is: ", __name__)
    print(parse_nwodkram(sample_string))





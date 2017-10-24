#!/usr/bin/env pytresulton3

import os,sys,re
import urllib.request

emails = []
def find_emails(text):
    for i in re.findall(r'[\w\.\+\-!#\$%&*/=\?\^_{|}~]+\@[\w]+[\w\.\+\-!#\$%&*/=\?\^_{|}~]*\.[a-z]{2,3}',text):
        emails.append(i)
    return emails    


urls = []
def find_urls(text):
    for i in re.findall(r'<a href=(\"?\'?)(http://|https://)([^\"\'>]*)(\1)>',text):
        urls.append(''.join(i))
    return urls


if __name__ == "__main__":
    sample_string_email = r"""
    This is a long string
    without an email address
    It is what it is

    This string has an email!
    karl@erik.no
    (don't expect replies!)

    
    Here is an email:simon@funke.no. It's probably not going to work.
    You could try funsim@uio.no, but I don't think that's the right one either. 
    

    
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>
    

    This is text which contains some email-like strings which aren't emails 
    according to the definition of the assignment:
    the string name@server.1o has a number at the start of thedomain,
    the string name@server.o1 has a number at the end,
    the string name@ser<ver.domin has an illegal character in its server,
    as does the string name@ser"ver.domain,

    however, the string na&me@domain.com is actually an email!
    as is n~ame@dom_ain.com
    but name@domain._com is bad
    (name@domain.c_o.uk is allowed though)
    
    """
    
    sample_string_url = r"""
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>

    This URL is not inside a hyperlink tag, so should be ignored: "http://www.google.com"
    

    This is almost a hyperlink, but the quotes are mismatched, so it shouldn't be captured:

    <a href="http://www.google.com/super_secret/all_the_user_data/'>Please don't click</a>

    <a href="http://www.google.com/super_secret/user_data/'>Please don't click</a>
    
    """
    url = 'https://code.iamcal.com/php/rfc822/tests/'
    url_req = urllib.request.urlopen(url)
    url_read = url_req.read()
    str = url_read.decode("utf8")
    url_req.close()
    
    """
    The find_emails() fnction has two choices. Press 1 for URL and 2 for String
    """
    usr_input = input('Enter your choice for Email Scraping: \nPress \'1\' for URL \nPress \'2\' for String  \nor Press \'3\' to jump to URL scraping \nYou can Press \'0\' to exit this program \n:')
    while (usr_input != '1') and (usr_input != '2') and (usr_input != '3') and (usr_input != '0'):
        usr_input = input("Try again. Press only '1'/'2'/'3'/'0' ")

    if usr_input == '1':
        print('These are the scraped emails from the URL : ',url,'\n\n',find_emails(str)) 
    elif usr_input == '2':
        print('These are the scraped emails from the String : \n\n',find_emails(sample_string_email)) 
    elif usr_input == '3':
        print('\n\nThese are the scraped URLs from the sample_string: \n\n',find_urls(sample_string_url))
    elif usr_input == '0':
        print('Exiting....')
        exit
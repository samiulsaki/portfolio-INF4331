#!/usr/bin/env python3

# The scraper.py script is designed to scrap all the URLs and Emails from a given URL or a string.
# The script is pretty self explanatory. Just run the script and follow the instructions.
# 
# The following options does as follows:
#   Option 1 for Email Scraping in URL 
#   Option 2 for Email Scraping in Sample String
#   Option 3 for URL Scraping in URL
#   Option 4 for URL Scraping in Sample String
#   Option 5 for Email Scraping in depth level of URL
#   Option 0 to exit this program
#
# Disclaimer:
# The program might be not too sophisticated. But I tried my best to make it as good as I can. 
# If you like to find all the emails in deeper level URLs (option 5) I suggest you do that in a cloud server or
# just stick with upto depth level 3 (or less).
# I haven't created any test file. Users can easily insert their string as input.

import os,sys,re,time
import urllib.request

def url_read(url):
        if url.endswith('/'):
            pass
        elif not url.endswith('.html'):
            url = url+'/'
        url_req = urllib.request.urlopen(url)
        url_read = url_req.read()
        string = url_read.decode("utf8")
        url_req.close()
        return string

def find_emails(text):
    emails = []
    for i in re.findall(r'[\w\.\+\-!#\$%&*/=\?\^_{|}~]+\@[a-z]+[\w\.\+\-!#\$%&*/=\?\^_{|}~]*\.[a-z]{2,3}',text):
        emails.append(i)
    return emails    

def find_urls(text):
    urls = []
    for i in re.findall(r'<a href=(\"?\'?)(http://|https://)([^\"\'>]*)(\1)>',text):
        hyperlink = ''.join(i)
        urls.append(hyperlink.strip('"'))
    for j in re.findall(r'<a href=(\"?\'?)(\w.*).*(\.html)(\1)>', text):
        relative_hyperlink = ''.join(j)
        if relative_hyperlink not in urls:
            if re.search(r'http',relative_hyperlink):
                relative_hyperlink = relative_hyperlink.strip('"')
            else:
                if url.endswith('/'):
                    relative_hyperlink = url+relative_hyperlink.strip('"')
                else:
                    new_url = re.sub(r'\b(/\w.*\.html)','',url)
                    relative_hyperlink = new_url+'/'+relative_hyperlink.strip('"')
            urls.append(relative_hyperlink)
    return urls

def all_the_emails(url,depth):
    all=[]
    def urls_emails(url):
        string = url_read(url)        
        for i in find_urls(string):
            if i not in all:                       
                all.append(i)
    
    for i in range(0,depth):
        urls_emails(url)
        for i in all:
            try:
                print('\nThe URL is : ', i)
                j = find_emails(url_read(i))
                if j!= []:
                    print('And these are the emails found from the above URL: \n\n',set(j))
            except Exception:
                pass
        if (depth > 1):
            depth = depth - 1
            for i in all:
                print('\nThe URL that getting searched now:',i,'........\n')
                time.sleep(4)
                try:
                    all_the_emails(i,1)
                except Exception:
                    pass
            all=[]
        else:
            pass

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
    
    # Main Program
    os.system('clear')
    usr_input = input('''Enter your choice for URL/Email Scraping: \n
    Press \'1\' for Email Scraping in URL \n
    Press \'2\' for Email Scraping in Sample String \n
    Press \'3\' for URL Scraping in URL \n
    Press \'4\' for URL Scraping in Sample String \n
    Press \'5\' for Email Scraping in depth level of URL \n
    You can Press \'0\' to exit this program \n:''')
    while (usr_input != '1') and (usr_input != '2') and (usr_input != '3') and (usr_input != '4') and (usr_input != '0') and (usr_input != '5'):
        usr_input = input("Try again. Press only '1'/'2'/'3'/'4'/'5'/'0' : ")
    if usr_input == '1':
        usr_input = input('Enter your own url or leave it blank for default : ')
        if usr_input is not "":
            url = usr_input
            str = url_read(url)
            print('\nThese are the scraped emails from the URL (user input) : ',url,'\n\n',find_emails(str))
        else:
            url = 'https://code.iamcal.com/php/rfc822/tests/'
            str = url_read(url)
            print('\nThese are the scraped emails from the URL (default) : ',url,'\n\n',find_emails(str)) 
    elif usr_input == '2':
        usr_input = input('Enter your own string (just paste single lines) or leave it blank for default : ')
        if usr_input is not "":
            sample_string = usr_input
            print('\nThese are the scraped emails from the String (user input) : \n\n',find_emails(sample_string))
        else:
            print(sample_string_email)
            print('\nThese are the scraped emails from the String (default) : \n\n',find_emails(sample_string_email)) 
    elif usr_input == '3':
        usr_input = input('Enter your own URL or leave it blank for default : ')
        if usr_input is not "":
            url = usr_input
            str = url_read(url)
            print('\nThese are the scraped URLs from the URL (user input): ',url,'\n\n',find_urls(str))
        else:
            url = 'https://lucidtech.io/index.html'
            str = url_read(url)
            print('\nThese are the scraped URLs from the URL (default): ',url,'\n\n',find_urls(str))
    elif usr_input == '4':
        usr_input = input('Enter your own String (just paste single lines) or leave it blank for default : ')
        if usr_input is not "":
            sample_string = usr_input
            print('\nThese are the scraped URLs from the sample String (user input): \n\n',find_urls(sample_string))
        else:
            print(sample_string_url)
            print('\nThese are the scraped URLs from the sample String (default): \n\n',find_urls(sample_string_url))
    elif usr_input == '5':
        usr_input = input('Enter your own URL or leave it blank for default : ')        
        if usr_input is not "":
            url = usr_input
            depth = int(input('Set your depth level (in integer): '))
            print('\nThese are the scraped emails from the URL (user input) : ',url,'with depth level : ',depth,'\n\n')
            all_the_emails(url,depth)
        else:
            url = 'http://lucidtech.io'
            depth = int(input('Set your depth level (in integer): '))
            print('\nThese are the scraped emails from the URL (default) : ',url,'with depth level : ',depth,'\n\n')
            all_the_emails(url,depth) 
    elif usr_input == '0':
        print('Exiting....')
        exit

    
    

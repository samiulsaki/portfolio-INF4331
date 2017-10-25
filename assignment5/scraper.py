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
        st1 = ''.join(i)
        urls.append(st1)
    for j in re.findall(r'<a href=(\"?\'?)(\w.*).*(\.html)(\1)>', text):
        st2 = ''.join(j)
        if st2 not in urls:
            urls.append(st2)
    return urls


url = 'http://startuplab.no'
def all_the_emails(url,depth):
    url_req = urllib.request.urlopen(url)
    url_read = url_req.read()
    str = url_read.decode("utf8")
    url_req.close()
    all_urls = find_urls(str)
    all_emails = find_emails(str)
    for i in all_urls:
        print(i)
        if re.search(r'http',i):
            #print(i)
            all_urls1 = find_urls(i)
            for i in all_urls1:
                all_urls2 = find_urls(i)
                for i in all_urls2:
                    all_url3 = find_emails(i)
                    #for i in all_url3:
                     #   print(i)


all_the_emails(url,1)

# if __name__ == "__main__":
#     sample_string_email = r"""
#     This is a long string
#     without an email address
#     It is what it is

#     This string has an email!
#     karl@erik.no
#     (don't expect replies!)

    
#     Here is an email:simon@funke.no. It's probably not going to work.
#     You could try funsim@uio.no, but I don't think that's the right one either. 
    

    
#     This is a bit of html:
# 	<span id="vrtx-person-change-language-link">
# 	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
# 	</span>

        
          
#             <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
#                 <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
#             </div>
    

#     This is text which contains some email-like strings which aren't emails 
#     according to the definition of the assignment:
#     the string name@server.1o has a number at the start of thedomain,
#     the string name@server.o1 has a number at the end,
#     the string name@ser<ver.domin has an illegal character in its server,
#     as does the string name@ser"ver.domain,

#     however, the string na&me@domain.com is actually an email!
#     as is n~ame@dom_ain.com
#     but name@domain._com is bad
#     (name@domain.c_o.uk is allowed though)
    
#     """
    
#     sample_string_url = r"""
#     This is a bit of html:
# 	<span id="vrtx-person-change-language-link">
# 	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
# 	</span>

        
          
#             <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
#                 <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
#             </div>

#     This URL is not inside a hyperlink tag, so should be ignored: "http://www.google.com"
    

#     This is almost a hyperlink, but the quotes are mismatched, so it shouldn't be captured:

#     <a href="http://www.google.com/super_secret/all_the_user_data/'>Please don't click</a>

#     <a href="http://www.google.com/super_secret/user_data/'>Please don't click</a>
    
#     <a href="otherpage.html">
#     """
    
#     def url_read(url):
#         url_req = urllib.request.urlopen(url)
#         url_read = url_req.read()
#         str = url_read.decode("utf8")
#         url_req.close()
#         return str

#     # Main Program
#     """
#     The find_emails() fnction has two choices. Press 1 for URL and 2 for String
#     """
#     usr_input = input('''Enter your choice for URL/Email Scraping: \n
#     Press \'1\' for Email Scraping in URL \n
#     Press \'2\' for Email Scraping in Sample String \n
#     Press \'3\' for URL Scraping in URL \n
#     Press \'4\' for URL Scraping in Sample String \n
#     Press \'5\' for Email Scraping in depth in URL \n
#     You can Press \'0\' to exit this program \n:''')
#     while (usr_input != '1') and (usr_input != '2') and (usr_input != '3') and (usr_input != '4') and (usr_input != '0'):
#         usr_input = input("Try again. Press only '1'/'2'/'3'/'4'/'5'/'0' : ")

#     if usr_input == '1':
#         usr_input = input('Enter your own url or leave it blank for default : ')
#         if usr_input is not "":
#             url = usr_input
#             str = url_read(url)
#             print('\nThese are the scraped emails from the URL (user input) : ',url,'\n\n',find_emails(str))
#         else:
#             url = 'https://code.iamcal.com/php/rfc822/tests/'
#             str = url_read(url)
#             print('\nThese are the scraped emails from the URL (default) : ',url,'\n\n',find_emails(str)) 
#     elif usr_input == '2':
#         usr_input = input('Enter your own string (just paste it) or leave it blank for default : ')
#         if usr_input is not "":
#             sample_string = usr_input
#             print('\nThese are the scraped emails from the String (user input) : \n\n',find_emails(sample_string))
#         else:
#             print('\nThese are the scraped emails from the String (default) : \n\n',find_emails(sample_string_email)) 
#     elif usr_input == '3':
#         usr_input = input('Enter your own URL or leave it blank for default : ')
#         if usr_input is not "":
#             url = usr_input
#             str = url_read(url)
#             print('\nThese are the scraped URLs from the URL (user input): \n\n',find_urls(str))
#         else:
#             url = 'https://lucidtech.io/index.html'
#             str = url_read(url)
#             print('\nThese are the scraped URLs from the URL (default): \n\n',find_urls(str))
#     elif usr_input == '4':
#         usr_input = input('Enter your own String (just paste it) or leave it blank for default : ')
#         if usr_input is not "":
#             sample_string = usr_input
#             print('\nThese are the scraped URLs from the sample String (user input): \n\n',find_urls(sample_string))
#         else:
#             print('\nThese are the scraped URLs from the sample String (default): \n\n',find_urls(sample_string_url))
#     elif usr_input == '0':
#         print('Exiting....')
#         exit

    
    

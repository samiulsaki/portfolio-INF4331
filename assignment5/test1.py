# Imports 
from parser import parse_nwodkram

###################
#########   ITALIC
###################

def test_parser_italic():
    """ Test parsing of italic """

    # test one case, one line success
    md_italic = "that *this* is"
    html_italic = "that <i>this</i> is"
    assert parse_nwodkram(md_italic) == html_italic

    # test multiple cases, one line
    md_italic = "that awd *this* awd is awd *siht* awd"
    html_italic = "that awd <i>this</i> awd is awd <i>siht</i> awd"
    assert parse_nwodkram(md_italic) == html_italic

    # test multiple cases, multiple lines
    md_italic = r"""that awd *this* awd is \n awd *siht* awd"""
    html_italic = r"""that awd <i>this</i> awd is \n awd <i>siht</i> awd"""
    assert parse_nwodkram(md_italic) == html_italic

    # test span over multiple lines
    md_italic = r"""that awd *this* awd *is \n awd siht* awd"""
    html_italic = r"""that awd <i>this</i> awd <i>is \n awd siht</i> awd"""
    assert parse_nwodkram(md_italic) == html_italic

    # test false positive / commented
    md_italic = "that awd *this* and not \*this\* awd"
    html_italic = "that awd <i>this</i> and not \*this\* awd"
    assert parse_nwodkram(md_italic) == html_italic

###################
#########   STRONG
###################

def test_parser_strong():
    """ Test parsing of bold / strong """

    # test one case, one line
    md_strong = "that %this% is"
    html_strong = "that <strong>this</strong> is"
    assert parse_nwodkram(md_strong) == html_strong

    # test multiple cases, one line
    md_strong = "that %this% awd is awd %siht% awd"
    html_strong = "that <strong>this</strong> awd is awd <strong>siht</strong> awd"
    assert parse_nwodkram(md_strong) == html_strong

    # test multiple cases, multiple lines
    md_strong = r"""that %this% is \n awd %siht% awd"""
    html_strong = r"""that <strong>this</strong> is \n awd <strong>siht</strong> awd"""
    assert parse_nwodkram(md_strong) == html_strong

    # test span over multiple lines
    md_strong = r"""that %this% is awd %is \n awd siht% awd"""
    html_strong = r"""that <strong>this</strong> is awd <strong>is \n awd siht</strong> awd"""
    assert parse_nwodkram(md_strong) == html_strong

    # test false positive / commented
    md_strong = "that %this% and not \%sthis\% awd"
    html_strong = "that <strong>this</strong> and not \%sthis\% awd"
    assert parse_nwodkram(md_strong) == html_strong

###################
#######   HYPERLINK
###################

def test_parser_hyperlink():
    """ Test parsing of hyperlinks """

    # test one case one line
    md_hyperlink = "awd [here](www.google.com) is a hyperlink"
    html_hyperlink = "awd <a href='www.google.com'>here</a> is a hyperlink"
    assert parse_nwodkram(md_hyperlink) == html_hyperlink

    # test multiple cases, one line
    md_hyperlink = "awd [here](www.google.com) is a hyperlink and [here](www.google.com) is another one"
    html_hyperlink = "awd <a href='www.google.com'>here</a> is a hyperlink and <a href='www.google.com'>here</a> is another one"
    assert parse_nwodkram(md_hyperlink) == html_hyperlink

    # test multiple cases, multiple lines
    md_hyperlink = r"""[here](www.google.com) is a hyperlink \n and [here](www.google.com) is another one"""
    html_hyperlink = r"""<a href='www.google.com'>here</a> is a hyperlink \n and <a href='www.google.com'>here</a> is another one"""
    assert parse_nwodkram(md_hyperlink) == html_hyperlink

    # test weird case
    md_hyperlink = "[and here](https://www.weird?$|site.weird/path/) is a third"
    html_hyperlink = "<a href='https://www.weird?$|site.weird/path/'>and here</a> is a third"
    assert parse_nwodkram(md_hyperlink) == html_hyperlink

###################
##########   QUOTE
###################

def test_parser_quote():
    """ Test parsing of (block)quote """

    md_quote = ">> some quote"
    html_quote = "<blockquote> some quote </blockquote>"
    assert parse_nwodkram(md_quote) == html_quote

    # "corner" case
    md_quote = "awdawdaw >> some quote"
    html_quote = "awdawdaw <blockquote> some quote </blockquote>"
    assert parse_nwodkram(md_quote) == html_quote

###################
##########   IMAGE
###################

def test_parser_image():
    """ Test parsing of image """

    md_img = "awd <www.imgurl.com>(w=123,h=321) awd"
    html_img = "awd <img src='www.imgurl.com' width='123' height='321'> awd"
    assert parse_nwodkram(md_img) == html_img

###################
###########   WIKI
###################

def test_parser_wiki():
    """ Test parsing wiki query """

    md_wiki = "awd [wp:QUERYSOMETHING] awd"
    html_wiki = "awd <a href='en.wikipedia.org/wiki/QUERYSOMETHING'>QUERYSOMETHING</a> awd"
    assert parse_nwodkram(md_wiki) == html_wiki


###################
#######   RUN TEST
###################

#test_parser_italic()
#test_parser_strong()
#test_parser_hyperlink()
#test_parser_quote()
#test_parser_wiki()
#test_parser_image()
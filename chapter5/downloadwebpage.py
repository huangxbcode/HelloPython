from bs4 import BeautifulSoup
import urllib2

def get_stock_html(ticker_name):
    opener = urllib2.build_opener(
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler(debuglevel=0),
        )
    opener.addheaders = [
        ('User-agent',
         "Mozilla/4.0 (compatible; MSIE 7.0;"
         ".NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
        ]
    url = "http://finance.yahoo.com/q?s=" + ticker_name
    response = opener.open(url)
    return ''.join(response.readlines())

def find_quote_section(html):
    soup = BeautifulSoup(html)
    quote = soup.find('div', attrs={'class':'yfi_quote_summary'})
    return quote

def parse_stock_html(html, ticker_name):
    quote = find_quote_section(html)
    result = {}
    tick = ticker_name.lower()

    #<h2>Google Inc.</h2>
    print quote
    print "----8888888888888888888888888888888888888---------"
    print quote.find('h2')
    result['stock_name'] = quote.find('h2').contents[0]

    ###After hours values
    # <span id="yfs_191_goog">329.94</span>
    result['ah_price'] = quote.find('span',
                                     attrs={'id':'yfs_191_'+tick}).string

    # <span id="yfs_z08_goog">329.94</span>
    # <span class="yfs-price-changed-down">0.22</span>
    result['ah_change'] = (quote.find('span',
                                     attrs={'id':'yfs_z08_'+tick}).contents[1])

    ### Current values
    # <span id="yfs_l10_goog">330.16</span>
    result['last_trade'] = quote.find('span',
                                     attrs={'id':'yfs_l10_'+tick}).string

    # <span id="yfs_c10_goog" class="yfi_quote_price">
    # <span class="yfs-price-change-down">1.06</span>
    def is_price_change(value):
        return (value is not None and value.strip().lower()
                .startswith('yfi-price-change'))

    result['change'] = (quote.find(attrs={'id':'yfs_c10_'+tick})
                        .find(attrs={'class':is_price_change}).string)
    
    return result
    
if __name__ == '__main__':
    html = get_stock_html('GOOG')
    print html
    print "------------------------------------------"
    print parse_stock_html(html,'GOOG')


demo所用网页
http://finance.yahoo.com/q?s=GOOG

Beautiful Soup
www.crummy.com/software/BeautifulSoup/
下载：beautifulsoup4-4.4.1
安装，注意要到setup.py所在目录执行：python setup.py install

from bs4 import BeautifulSoup
注意：和书上的有差别！

FireFox and Firebug
http://getfirefox.com/
http://getfirebug.com/

报错：
to this:

 BeautifulSoup([your markup], "html.parser")

<div class="yfi_quote_summary"><div class="rtq_table" id="yfi_quote_summary_data"><table id="table1"><tr><th scope="row" width="48%">Prev Close:</th><td class="yfnc_tabledata1">747.77</td></tr><tr><th scope="row" width="48%">Open:</th><td class="yfnc_tabledata1">753.00</td></tr><tr><th scope="row" width="48%">Bid:</th><td class="yfnc_tabledata1"><span id="yfs_b00_goog">747.50</span><small> x <span id="yfs_b60_goog">100</span></small></td></tr><tr><th scope="row" width="48%">Ask:</th><td class="yfnc_tabledata1"><span id="yfs_a00_goog">748.50</span><small> x <span id="yfs_a50_goog">300</span></small></td></tr><tr><th scope="row" width="48%">1y Target Est:</th><td class="yfnc_tabledata1">853.67</td></tr><tr><th scope="row" width="48%">Beta:</th><td class="yfnc_tabledata1">1.032</td></tr><tr><th scope="row" width="54%">Next Earnings Date:</th><td class="yfnc_tabledata1">N/A</td></tr></table><table id="table2"><tr><th scope="row" width="48%">Day's Range:</th><td class="yfnc_tabledata1"><span><span id="yfs_g53_goog">743.01</span></span> - <span><span id="yfs_h53_goog">758.08</span></span></td></tr><tr><th scope="row" width="48%">52wk Range:</th><td class="yfnc_tabledata1"><span>486.23</span> - <span>775.96</span></td></tr><tr><th scope="row" width="48%">Volume:</th><td class="yfnc_tabledata1"><span id="yfs_v53_goog">2,669,028</span></td></tr><tr><th scope="row" width="48%">Avg Vol <span class="small">(3m)</span>:</th><td class="yfnc_tabledata1">2,113,610</td></tr><tr><th scope="row" width="48%">Market Cap:</th><td class="yfnc_tabledata1"><span id="yfs_j10_goog">511.25B</span></td></tr><tr><th scope="row" width="48%">P/E <span class="small">(ttm)</span>:</th><td class="yfnc_tabledata1">31.34</td></tr><tr><th scope="row" width="48%">EPS <span class="small">(ttm)</span>:</th><td class="yfnc_tabledata1">23.72</td></tr><tr class="end"><th scope="row" width="48%">Div &amp; Yield:</th><td class="yfnc_tabledata1">N/A (N/A) </td></tr></table></div></div>
----8888888888888888888888888888888888888---------
None

Traceback (most recent call last):
  File "E:\workspace\HelloPython\downloadwebpage.py", line 64, in <module>
    print parse_stock_html(html,'GOOG')
  File "E:\workspace\HelloPython\downloadwebpage.py", line 32, in parse_stock_html
    result['stock_name'] = quote.find('h2').contents[0]
AttributeError: 'NoneType' object has no attribute 'contents'
>>> 

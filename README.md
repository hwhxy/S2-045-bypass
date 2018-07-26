### 来历

TSCTF时光机

### S-045

该脚本为s-045 bypass防火墙测试脚本，payload在脚本中呈现。  
其中包含如下两个脚本：  
1. s-045_path_bypass.py  
2. s-045_shell_bypass.py
1用来获取web网站的真实路径，2用来写入webshell进入1获得的路径下。  

### 使用方法

1. [\*] python s-045_load_bypass.py <url>
2. [\*] python s-045_shell_bypass.py <url> <path> <cmd>

import re

def Read_Headers(file):
    headerDict = {}
    f = open(file,'r')
    headersText = f.read()
    # print(headersText)
    headers = re.split('\n',headersText)#将文本通过回车符隔开
    print(headers)
    for header in headers:
        result = re.split(':',header,maxsplit=1)#将header通过 ：分割，并且只分割一次
        headerDict[result[0]] = result[1].strip()
    f.close()
    return headerDict
if __name__ == '__main__':
    print(Read_Headers('head_tm.txt'))

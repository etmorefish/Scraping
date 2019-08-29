
import requests

url = "https://www.baidu.com/s"

querystring = {"wd":"python"}

headers = {
    'Connection': "keep-alive",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    'Cookie': "BAIDUID=7B7D88053B10EB435DB1E212DBF145BF:FG=1; BIDUPSID=7B7D88053B10EB435DB1E212DBF145BF; PSTM=1551098874; BDRCVFR[pNjdDcNFITf]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; BD_UPN=123253; BD_HOME=1; locale=zh; H_PS_PSSID=1444_21092_18559_26350_28415; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; H_PS_645EC=b710sJmEk7esA9h2dxosAL9oFPrYrIk%2FdoimlGSz7DCKfuSVp27CVuygqGuvEqwhznOf",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
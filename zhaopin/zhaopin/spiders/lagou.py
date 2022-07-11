from zhaopin.items import ZhaopinItem
import scrapy
import json
import re


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    bash_url = 'https://www.lagou.com/wn/jobs'
    max_page = 1
    temp = 'JSESSIONID=ABAAABAABAGABFA758BA40E76C8252849B4EB20956703CC; WEBTJ-ID=20220709140905-181e1937389db4-00ec36581b2e53-4a617f5c-2073600-181e193738a86d; RECOMMEND_TIP=true; user_trace_token=20220709140906-f6c1b556-c6f0-476b-8ce6-d455d6825b9e; LGUID=20220709140906-2588fbcc-272f-438e-86fd-e8049fe3994b; _gid=GA1.2.2079106617.1657346947; _ga=GA1.2.1263018898.1657346947; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1657346947; privacyPolicyPopup=false; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; X_MIDDLE_TOKEN=8b53e209d1facbae074efa1070454105; __lg_stoken__=f5c897dc015d9066762bc3f7efdeba5e561318c69967a5775347ab8588e8de778b78ca16db9f67debd7d49975659bb13e164fb7a983b492ec458cec9f60b1dae2d97437ee19b; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; gate_login_token=b7a6bb8dc56177730caac4a6caa44034b582ddfd934b920a80ab606873d946ce; LG_LOGIN_USER_ID=eecbf4307439c3beb8f2013e82d8df0c30d1791280df839808fa33b0520815c6; LG_HAS_LOGIN=1; _putrc=6C69077BDDDD9D9B123F89F2B170EADC; LGSID=20220709152752-4434e5a8-6579-464b-a335-b2ec67f54409; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; login=true; unick=%E5%A7%9A%E7%B4%AB%E9%B9%8F; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=9; X_HTTP_TOKEN=2ea6d33c81f5bbb03761537561f78ca63ffdaa9724; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1657351674; __SAFETY_CLOSE_TIME__17175162=1; LGRID=20220709152754-de1dbfa2-ce7a-46cb-b643-65ae02ff9a98; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217175162%22%2C%22first_id%22%3A%22181e19377d2371-0ddff96f4956e7-4a617f5c-2073600-181e19377d3b77%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22103.0.5060.66%22%7D%2C%22%24device_id%22%3A%22181e19377d2371-0ddff96f4956e7-4a617f5c-2073600-181e19377d3b77%22%7D'
    cookies = { cooke.split('=')[0]: cooke.split('=')[-1] for cooke in temp.split('; ')}

    def start_requests(self):
        for page in range(1, self.max_page + 1):
            url = f'{self.bash_url}?kd=Python&city=长沙&pn={page}'
            yield scrapy.Request(url, callback=self.parse, cookies=self.cookies)


    def parse(self, response):
        json_data = re.findall(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', response.text, re.S)[0]
        data = json.loads(json_data)
        # print(data)
        jobs = data['props']['pageProps']['initData']['content']['positionResult']['result']
        item = ZhaopinItem()
        for job in jobs:
          item['name'] = job['positionName']
          item['company'] = job['companyFullName']
          item['date'] = job['formatCreateTime']  
          item['salary'] = job['salary'] 
          item['work_year'] = job['workYear'] 
          item['education'] = job['education']
          item['position'] = job['positionDetail'].replace('<br />', '')
          item['address'] = job['positionAddress']  

          yield item    
  
     
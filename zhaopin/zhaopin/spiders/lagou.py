from zhaopin.items import ZhaopinItem
import scrapy
import json
import re


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    bash_url = 'https://www.lagou.com/wn/jobs'
    max_page = 1
    temp = 'RECOMMEND_TIP=true; user_trace_token=20220630170226-206ed619-d24f-40aa-a630-b41fe3c2c5fb; LGUID=20220630170226-4fc3bec5-c084-49af-b5be-2737aa0fc7d0; _ga=GA1.2.2108233836.1656579747; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABAGABFA6162D19C8E2DA9861BB956C3FDDDA59C; WEBTJ-ID=20220711104901-181eb29014717-017a270478a666-74492d21-1049088-181eb29014bc; PRE_UTM=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; LGSID=20220711104917-f705e060-566c-4b19-bbb5-acda91210255; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1656579747,1657022983,1657507746; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1657507746; _gid=GA1.2.2054728656.1657507747; privacyPolicyPopup=false; sensorsdata2015session=%7B%7D; TG-TRACK-CODE=index_navigation; LGRID=20220711104930-a574ce8a-0bf8-43a2-8a2c-2545810effdb; X_HTTP_TOKEN=72baa0f47a8822cf1777057561705ac91d4d9540b0; X_MIDDLE_TOKEN=149ea3bcc0d912e9889cf46d5223ea00; __lg_stoken__=905733c1814080718a96ca6967b70092d6bf0a6803336df82ee3892c5bd6063ef69eafd16128b4fa104a5fbc02bef7c1fcd3006357d7d466a81ec8a7407801e0b17e05b1373f; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22181b3d8f2bf11e-05285b9543e35f-26021a51-2073600-181b3d8f2c1cf%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22103.0.5060.114%22%7D%2C%22%24device_id%22%3A%22181b3d8f2bf11e-05285b9543e35f-26021a51-2073600-181b3d8f2c1cf%22%7D'
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
  
     

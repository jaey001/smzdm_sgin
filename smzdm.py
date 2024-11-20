# coding=utf-8
import requests
import json

# 设置Server酱post地址 不需要可以删除
serverChan = "https://sc.ftqq.com/*****************************************.send"
# 状态地址
current_url = 'https://zhiyou.smzdm.com/user/info/jsonp_get_current'
# 签到地址
checkin_url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
# 用用户名和密码登录后获取Cookie
userCookie = "**************************************************************"
headers = {
    'Referer': 'https://www.smzdm.com/',
    'Host': 'zhiyou.smzdm.com',
    'Cookie':__ckguid=Jp2X1U29c34hRpYVCJY6ir6; device_id=3748172166171759818529269543f4bfc776230d56844bf711f21b35d1; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1732102258; HMACCOUNT=B6DE96A1CCFB778C; _tea_utm_cache_10000007=undefined; homepage_sug=b; r_sort_type=score; footer_floating_layer=0; ad_date=20; ad_json_feed=%7B%7D; _zdmA.vid=*; sess=BA-0Lq2ejqFgOUnfO0D6ryYe4KK%2BYnZC4nCxNpBhsaMXwn3hDpmkFmtrS6EGQwqxGrsHcqkBl8k9E41kQsUBtA25%2FtXQxio9v0US6Y45bWaps8G%2BYJnihZVt1%2BK; user=user%3A9891696455%7C9891696455; smzdm_id=9891696455; _zdmA.uid=ZDMA.kk7fWHdini.1732117057.2419200; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1732117057; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A2%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%229891696455%22%2C%22first_id%22%3A%2218fe8d472ac581-09d7d0eb78aae6-4c657b58-1821369-18fe8d472ade88%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2F%22%7D%2C%22%24device_id%22%3A%2218fe8d472ac581-09d7d0eb78aae6-4c657b58-1821369-18fe8d472ade88%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzNDk1NmZkNDRiMGQtMDVkNTYyZDE2Zjc1YzgtNGM2NTdiNTgtMTgyMTM2OS0xOTM0OTU2ZmQ0NTI3ZTMiLCIkaWRlbnRpdHlfbG9naW5faWQiOiI5ODkxNjk2NDU1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%229891696455%22%7D%7D; _zdmA.time=1732117092261.0.https%3A%2F%2Fwww.smzdm.com%2F,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def req(url):
    url = url
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = json.loads(res.text)
        return data


data = req(current_url)
if data['checkin']['has_checkin']:
    info = '%s ：%s 你目前积分：%s，经验值：%s，金币：%s，碎银子：%s，威望：%s，等级：%s，已经签到：%s天' % (data['sys_date'], data['nickname'], data['point'], data['exp'], data['gold'], data['silver'], data['prestige'], data['level'],data['checkin']['daily_checkin_num'])
    print(info)
    # 通过Server酱发送状态 不需要可以删除
    requests.post(serverChan, data={'text': data['nickname'] + '已经签到过了', 'desp': info})
else:
    checkin = req(checkin_url)['data']
    # print(checkin)
    info = '%s 目前积分：%s，增加积分：%s，经验值：%s，金币：%s，威望：%s，等级：%s' % (data['nickname'], checkin['point'], checkin['add_point'], checkin['exp'], checkin['gold'], checkin['prestige'], checkin['rank'])
    print(info)
    # 通过Server酱发送状态 不需要可以删除
    requests.post(serverChan, data={'text': data['nickname'] + '签到信息', 'desp': info})
 

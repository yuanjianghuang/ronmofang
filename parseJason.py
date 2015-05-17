# -*- coding: utf-8 -*-
import json
from pprint import pprint
import jieba.analyse

# This is used to parse the JASON files, provided the crawled data from rongmofang.com
media_report = 0
interests_payback_notice = 1
website_notice = 2

def write_data(content, file):
    with open(file,'w+') as f:
        content = unicode(content).encode('utf-8')
        f.write(content)
        f.close()

key_words = [
        '关于我们','关于融魔方','管理团队','合作机构','法律保障',
        '联系我们','常见问题','走进融魔方','投资理财','交易安全'
        '充值提现','安全保障','投资安全','数据安全','隐私安全','注册','登录',
        '新手攻略','重庆澜鼎信息技术有限公司','渝ICP备','充值投资','资金提现',
        '点击','客服','QQ','微信'
       ]

jieba.suggest_freq('融魔方',True)

def find_key_words(file,topK):
    with open(file,'r') as f:
        text_clean  = f.read()
        f.close()
    tags = jieba.analyse.extract_tags(text_clean, topK=topK)
    #print(",".join(tags))
    return (",".join(tags))

def main():
    with open('info.json') as data_file:
        lines = data_file.readlines()
    media_notice_content = []
    interests_payback_notice_content = []
    website_notice_content = []

    for line in lines:
        data = json.loads(line)
        if data["type"] == media_report:
            media_notice_content.append(data["content"])
        if data["type"] == interests_payback_notice:
            interests_payback_notice_content.append(data["content"])
        if data["type"] == website_notice:
            website_notice_content.append(data["content"])


    write_data(''.join(media_notice_content), 'media_report.txt')
    write_data(''.join(interests_payback_notice_content), 'interests_payback_notice.txt')
    write_data(''.join(website_notice_content), 'website_notice.txt')

    topK = 20
    print u'媒体报到：', find_key_words('media_report.txt',topK)
    print u'还款公告：', find_key_words('interests_payback_notice.txt',topK)
    print u'站内公告：', find_key_words('website_notice.txt',topK)
if __name__ == "__main__":

    main()
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import sys
from pymongo.errors import ConnectionFailure
import jieba
import jieba.analyse

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "ronmofangDB"
MONGODB_COLLECTION = "ronmofangCollection"
# This py is used to test Mongo database related issues.
def main():
    try:
        connection = MongoClient(
            MONGODB_SERVER,
            MONGODB_PORT
        )
        db = connection[MONGODB_DB] # Getting a databse
        collection = db[MONGODB_COLLECTION]  # Getting a collection
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

    #collection.drop()
    #document_sample = collection.find_one({'url': "http://www.rongmofang.com/"} )
    #if not document_sample:
    #    print "no document found."
    #else:
    #    print "document found,and has text: ", document_sample['text']
    #    print "document found,and has internal url: ", document_sample['url_internal']
    #   print "document found,and has external url: ", document_sample['url_external']

    all_text = collection.find({},{"text":1,"_id":0})
    print ("There are %s items are found." % all_text.count())
    print "all_text type: ", type(all_text)

    with open("all_text.txt",'w') as f:
        for cursor in all_text:
            #print cursor["text"]
            f.write(unicode(cursor["text"]).encode('utf-8'))
    f.close()

    with open("all_text.txt",'r') as f:
        txt  = f.readlines()
        f.close()

    file_clean = open("all_text_clean.txt",'w')
    for line in txt:
        if len(line) >= 2:
            clean_line = " ".join(line.split())
            line = clean_line + " " + "\n"
            file_clean.write(line)
        else:
            pass
    file_clean.close()


    with open("all_text_clean.txt",'r') as f:
        text_clean  = f.readlines()
        f.close()
    key_words = [
        '关于我们','关于融魔方','管理团队','合作机构','法律保障',
        '联系我们','常见问题','走进融魔方','投资理财','交易安全'
        '充值提现','安全保障','投资安全','数据安全','隐私安全','注册','登录',
        '新手攻略','重庆澜鼎信息技术有限公司','渝ICP备','充值投资','资金提现',
        '点击','客服','QQ','微信'

       ]

    file_clean2 = open("all_text_clean2.txt",'w')

    with open("all_text_clean.txt",'r') as f:
        text_clean  = f.readlines()
        f.close()

    for line in text_clean:
        #print line
        find = False
        for words in key_words:
            if line.find(words) != -1 :
                find = True
                break
        if not find:
            file_clean2.write(line)
    file_clean2.close()

    with open("all_text_clean2.txt",'r') as f:
        text_clean2  = f.read()
        f.close()
    jieba.suggest_freq('融魔方',True)
    tags = jieba.analyse.extract_tags(text_clean2, topK=20)
    print(",".join(tags))

if __name__ == "__main__":
    main()

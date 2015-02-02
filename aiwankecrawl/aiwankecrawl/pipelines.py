# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from __future__ import unicode_literals

from twisted.enterprise import adbapi
from scrapy import log

import codecs
import json
import datetime
import sys
import MySQLdb


class JsonWriterPipeline(object):
    def __init__(self):
        #self.file = open('D:\\develop\\aiwanke\\aiwankecrawl\\json\\myapp.json','wb')
        self.file = codecs.open("D:\\develop\\aiwanke\\aiwankecrawl\\json\\myapp.json", "w", "utf-8")

    def process_item(self, item, spider):
        #line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

class MySQLTStorePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',db = 'aiwankedb',user = 'root',passwd = 'root',charset='utf8', use_unicode=True)
    def process_item(self,item,spider):
        query = self.dbpool.runInteraction(self._conditional_insert,item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self,tx,item):
        #log.err(item["appName"])
        #log.err(self.convertXhs(item["appName"]) if item["appName"] else "")
        #tx.execute("set names utf8")
        tx.execute("insert into tbgame (name,icon,apkfile,developer,categoryName,memo,createtime,lastupdatetime) "\
                   "values (%s, %s, %s, %s, %s, %s, %s, %s)",
            (
                # item["appName"].encode('utf-8') if item["appName"] else "",
                # item["iconUrl"].encode('utf-8') if item["iconUrl"] else "",
                # item["apkUrl"].encode('utf-8') if item["apkUrl"] else "",
                # item["authorName"].encode('utf-8') if item["authorName"] else "",
                # item["categoryName"].encode('utf-8') if item["categoryName"] else "",
                # item["desc"].encode('utf-8') if item["desc"] else "",

                item["appName"] if item["appName"] else "",
                item["iconUrl"] if item["iconUrl"] else "",
                item["apkUrl"] if item["apkUrl"] else "",
                item["authorName"] if item["authorName"] else "",
                item["categoryName"] if item["categoryName"] else "",
                item["desc"] if item["desc"] else "",

                # self.convertXhs(item["appName"]) if item["appName"] else "",
                # self.convertXhs(item["iconUrl"]) if item["iconUrl"] else "",
                # self.convertXhs(item["apkUrl"]) if item["apkUrl"] else "",
                # self.convertXhs(item["authorName"]) if item["authorName"] else "",
                # self.convertXhs(item["categoryName"]) if item["categoryName"] else "",
                # self.convertXhs(item["desc"]) if item["desc"] else "",

                datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'),
                datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
            )
        )
        log.msg("Item stored in db: %s" % item["appName"], level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)
        #pass

    def convertXhs(self,uni_str):
        xhs_str = ""
        for s in uni_str:
            xhs_str = xhs_str + s.encode("utf-8")
        return  xhs_str

class MySQLStorePipeline(object):

    def process_item(self,item,spider):
        try:
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "root", db = "aiwankedb",charset='utf8')
        except MySQLdb.Error,e:
            print "error %d：%s" % (e.args[0],e.args[1])
            sys.exit(1)
        try:
            # reload(sys)
            # sys.setdefaultencoding('utf-8')
            cursor = conn.cursor()
            sqlStr = "insert into tbgame (name,icon,apkfile,developer,categoryName,memo,gamesource,createtime,lastupdatetime) "\
                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            sqlParam = (
                item["appName"].encode('utf-8') if item["appName"] else "",
                item["iconUrl"].encode('utf-8') if item["iconUrl"] else "",
                item["apkUrl"].encode('utf-8') if item["apkUrl"] else "",
                item["authorName"].encode('utf-8') if item["authorName"] else "",
                item["categoryName"].encode('utf-8') if item["categoryName"] else "",
                item["desc"].encode('utf-8') if item["desc"] else "",
                item["source"],
                datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'),
                datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'),
            )
            cursor.execute(sqlStr,sqlParam)
            conn.commit()
        except MySQLdb.Error, e:
            print "error %d: %s" % (e.args[0], e.args[1])
        cursor.close()
        conn.close()

class DjangoPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
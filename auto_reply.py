#coding=utf8
import time
import itchat
from itchat.content import *
'''
data = {}
friends = itchat.get_friends()
for f in range(0,len(friends)):#第0个好友是自己,不统计
    if friends[f]['UserName'] and friends[f]['RemarkName']: # 优先使用好友的备注名称，没有则使用昵称
        user_name = friends[f]['UserName']
        remark_name = friends[f]['RemarkName']
        data[remark_name] = user_name

remarkname = u'慎终如始'
#for key in data.keys():
#    print(key)
#print(data[remarkname])
itchat.send_msg(msg='fuck', toUserName=None)
'''
former_user = ""
@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def auto_reply(msg):
    current_from = msg["FromUserName"]
    friend = itchat.search_friends(userName=current_from)
#    itchat.send("Message at %s has been received, I will reply to you later. --itchat python" % time.ctime(), toUserName='filehelper')
    if former_user == current_from:
        pass
    else:
        former_user = current_from
        itchat.send("Message at %s has been received, I will reply to you later. ahaha" % time.ctime(), toUserName=current_from)


itchat.auto_login(hotReload=True)
itchat.run()

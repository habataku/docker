

#@title 0x0でいいね {display-mode:"form"}
import requests
import json
import re
import datetime
import pprint
from IPython.display import display,Markdown

class IStudyPlusUser:
  def __init__(self,json):
    self.data=json

  def followee(self):
    json=requests.get("https://api.studyplus.jp/2/users?followee="+self.data["username"]+"&page=1&per_page=100&include_recent_record_seconds=t").json()
    followees=json["users"]
    if json["page"]<json["total_page"]:
      for i in range(2,json["total_page"]+1):
        followees += requests.get("https://api.studyplus.jp/2/users?followee="+self.data["username"]+"&page="+str(i)+"&per_page=100&include_recent_record_seconds=t").json()["users"]
    return followees

  def follower(self):
    json=requests.get("https://api.studyplus.jp/2/users?follower="+self.data["username"]+"&page=1&per_page=100&include_recent_record_seconds=t").json()
    followers=json["users"]
    if json["page"]<json["total_page"]:
      for i in range(2,json["total_page"]+1):
        followers += requests.get("https://api.studyplus.jp/2/users?follower="+self.data["username"]+"&page="+str(i)+"&per_page=100&include_recent_record_seconds=t").json()["users"]
    return followers

class IStudyPlus:
  def __init__(self):
    self.api_root="https://api.studyplus.jp/2"
    self.cookies={}
    self.headers = {}

  def login(self,username,password):
    data={
    "consumer_key": "QW2GdV9R7gUZGjndVgIgPt6SPwf7raw6",
    "consumer_secret": "U7ZRrKA8BuEBKkgc6c5GteW3hGUyRsRMaPsgf7DgtZH9yjrwZEdPrNIDHYkSqaPM",
    "username": username,
    "password": password}
    result=requests.post(self.api_root+"/client_auth",data=json.dumps(data),cookies=self.cookies,headers=self.headers).json()
    self.cookies={}
    self.username=result["username"]
    self.access_token=result["access_token"]
    self.headers["Authorization"]="OAuth "+self.access_token
    return self

  def __del__(self):
    if self.username:
      requests.post(self.api_root+"/logout",cookies=seｌf.cookies,headers=self.headers).json()
      self.username=""
      self.access_token=""
      self.headers={}


  def me(self):
    if not self.username:
      return
    result=requests.get(self.api_root+"/me",cookies=self.cookies,headers=self.headers)
    return IStudyPlusUser(result.json())

メールアドレス="habatakutori.fbi@gmail.com"
パスワード="gbtswspn1"
sp=IStudyPlus().login(メールアドレス,パスワード)
me=sp.me()


モード="フォロワー"#@param ["フォロワー","フォロー中"]
if モード=="フォロワー":
  userlist=me.follower()
elif モード=="フォロー中":
  userlist=me.followee()

md="|名前|id|\n|--|--|\n"
for val in userlist:
  md+=f"|{val['nickname']}|{val['username']}|\n"
display(Markdown(md))

for val in userlist:
  if val["nickname"]==me.data["nickname"]:
    continue
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+val["username"],cookies=sp.cookies,headers=sp.headers).json()
  count=0
  for record in json["feeds"]:
    if count==4:
      break

    try:
      record.pop("feed_type")
      body=list(record.values())[0]
      count+=1
      if body["if_you_like"]:
        continue
      requests.post("https://api.studyplus.jp/2/timeline_events/"+str(body["event_id"])+"/likes/like",cookies=sp.cookies,headers=sp.headers).json()
    except:
      continue

#@title ワイスピログイン {display-mode:"form"}
import requests
import json
import re
import datetime
import pprint
from IPython.display import display,Markdown

class IStudyPlusUser:
  def __init__(self,json):
    self.data=json

  def followee(self):
    json=requests.get("https://api.studyplus.jp/2/users?followee="+self.data["username"]+"&page=1&per_page=100&include_recent_record_seconds=t").json()
    followees=json["users"]
    if json["page"]<json["total_page"]:
      for i in range(2,json["total_page"]+1):
        followees += requests.get("https://api.studyplus.jp/2/users?followee="+self.data["username"]+"&page="+str(i)+"&per_page=100&include_recent_record_seconds=t").json()["users"]
    return followees

  def follower(self):
    json=requests.get("https://api.studyplus.jp/2/users?follower="+self.data["username"]+"&page=1&per_page=100&include_recent_record_seconds=t").json()
    followers=json["users"]
    if json["page"]<json["total_page"]:
      for i in range(2,json["total_page"]+1):
        followers += requests.get("https://api.studyplus.jp/2/users?follower="+self.data["username"]+"&page="+str(i)+"&per_page=100&include_recent_record_seconds=t").json()["users"]
    return followers

class IStudyPlus:
  def __init__(self):
    self.api_root="https://api.studyplus.jp/2"
    self.cookies={}
    self.headers = {}

  def login(self,username,password):
    data={
    "consumer_key": "QW2GdV9R7gUZGjndVgIgPt6SPwf7raw6",
    "consumer_secret": "U7ZRrKA8BuEBKkgc6c5GteW3hGUyRsRMaPsgf7DgtZH9yjrwZEdPrNIDHYkSqaPM",
    "username": username,
    "password": password}
    result=requests.post(self.api_root+"/client_auth",data=json.dumps(data),cookies=self.cookies,headers=self.headers).json()
    self.cookies={}
    self.username=result["username"]
    self.access_token=result["access_token"]
    self.headers["Authorization"]="OAuth "+self.access_token
    return self

  def __del__(self):
    if self.username:
      requests.post(self.api_root+"/logout",cookies=seｌf.cookies,headers=self.headers).json()
      self.username=""
      self.access_token=""
      self.headers={}


  def me(self):
    if not self.username:
      return
    result=requests.get(self.api_root+"/me",cookies=self.cookies,headers=self.headers)
    return IStudyPlusUser(result.json())

メールアドレス="studyplus0972@fukurou.ch"
パスワード="gbtswspn1"
sp=IStudyPlus().login(メールアドレス,パスワード)
me=sp.me()


モード="フォロワー"#@param ["フォロワー","フォロー中"]
if モード=="フォロワー":
  userlist=me.follower()
elif モード=="フォロー中":
  userlist=me.followee()

md="|名前|id|\n|--|--|\n"
for val in userlist:
  md+=f"|{val['nickname']}|{val['username']}|\n"
display(Markdown(md))

for val in userlist:
  if val["nickname"]==me.data["nickname"]:
    continue
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+val["username"],cookies=sp.cookies,headers=sp.headers).json()
  count=0
  for record in json["feeds"]:
    if count==4:
      break

    try:
      record.pop("feed_type")
      body=list(record.values())[0]
      count+=1
      if body["if_you_like"]:
        continue
      requests.post("https://api.studyplus.jp/2/timeline_events/"+str(body["event_id"])+"/likes/like",cookies=sp.cookies,headers=sp.headers).json()
    except:
      continue

"""# **自動いいね**"""

# @title ユーザーリストの人に2ついいね
for val in userlist:
  if val["nickname"]==me.data["nickname"]:
    continue
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+val["username"],cookies=sp.cookies,headers=sp.headers).json()
  count=0
  for record in json["feeds"]:
    if count==4:
      break

    try:
      record.pop("feed_type")
      body=list(record.values())[0]
      count+=1
      if body["if_you_like"]:
        continue
      requests.post("https://api.studyplus.jp/2/timeline_events/"+str(body["event_id"])+"/likes/like",cookies=sp.cookies,headers=sp.headers).json()
    except:
      continue

# @title 自分のタイムラインに個数いいね {display-mode:"form"}
import os
種類="フォロー中"#@param ["フォロー中","定期テスト 成績アップ"]
if 種類=="フォロー中":
  timeline_url="followee"
elif 種類=="定期テスト 成績アップ":
  timeline_url="study_goal/test"

個数=721 #@param {type:"number"}
count=0
try:
  while count<=個数:
    json=requests.get("https://api.studyplus.jp/2/timeline_feeds/"+timeline_url,cookies=sp.cookies,headers=sp.headers).json()
    for i in range(0,6):
      for record in json["feeds"]:
        if count>=個数:
          raise KeyboardInterrupt
        try:
          record.pop("feed_type")
          requests.post("https://api.studyplus.jp/2/timeline_events/"+str(list(record.values())[0]["event_id"])+"/likes/like",cookies=sp.cookies,headers=sp.headers).json()
          count+=1
        except TypeError:
          continue
      json=requests.get("https://api.studyplus.jp/2/timeline_feeds/"+timeline_url+"?until="+json["next"],cookies=sp.cookies,headers=sp.headers).json()
except KeyboardInterrupt:
  print(count)

w# @title 自分のタイムラインにずっといいね {display-mode:"form"}
from tqdm import tqdm
import sys
種類="定期テスト 成績アップ"#@param ["フォロー中","定期テスト 成績アップ"]
if 種類=="フォロー中":
  timeline_url="followee"
elif 種類=="定期テスト 成績アップ":
  timeline_url="study_goal/test"
count=0
try:
  while True:
    json=requests.get("https://api.studyplus.jp/2/timeline_feeds/"+timeline_url,cookies=sp.cookies,headers=sp.headers).json()
    #for i in range(0,3):
    for record in tqdm(json["feeds"],leave=False):
      try:
        record.pop("feed_type")
        requests.post("https://api.studyplus.jp/2/timeline_events/"+str(list(record.values())[0]["event_id"])+"/likes/like",cookies=sp.cookies,headers=sp.headers).json()
        count+=1
      except TypeError:
        continue
      #json=requests.get("https://api.studyplus.jp/2/timeline_feeds/"+timeline_url+"?until="+json["next"],cookies=sp.cookies,headers=sp.headers).json()
except KeyboardInterrupt:
  print(count)

# @title 人を検索して全いいね
検索元="\u30D5\u30A9\u30ED\u30EF\u30FC"#@param ["フォロワー","フォロー中","id指定"]
名前またはid="誠"#@param {type:"string"}

if 検索元=="フォロワー":
  user=next(filter(lambda x:x["nickname"]==名前またはid or x["username"]==名前またはid,me.follower()),None)
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+user["username"],cookies=sp.cookies,headers=sp.headers).json()
elif 検索元=="フォロー中":
  user=next(filter(lambda x:x["nickname"]==名前またはid or x["username"]==名前またはid,me.followee()),None)
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+user["username"],cookies=sp.cookies,headers=sp.headers).json()
else:
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+名前またはid,cookies=sp.cookies,headers=sp.headers).json()

for i in range(0,2000):
  count=0
  for record in json["feeds"]:
    try:
      record.pop("feed_type")
      body=list(record.values())[0]
      if body["if_you_like"]:
        count+=1
        continue
      requests.post("https://api.studyplus.jp/2/timeline_events/"+str(body["event_id"])+"/likes/like",cookies=sp.cookies,headers=sp.headers).json()
    except:
      continue
  if count==len(json["feeds"]) and i>100:
    break
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+user["username"]+"?until="+json["next"],cookies=sp.cookies,headers=sp.headers).json()

# @title 自分のタイムラインに指定した個数いいね {display-mode:"form"}
種類="\u5B9A\u671F\u30C6\u30B9\u30C8 \u6210\u7E3E\u30A2\u30C3\u30D7"#@param ["フォロー中","定期テスト 成績アップ"]
if 種類=="フォロー中":
  timeline_url="followee"
elif 種類=="定期テスト 成績アップ":
  timeline_url="study_goal/test"
json=requests.get("https://api.studyplus.jp/2/timeline_feeds/"+timeline_url,cookies=sp.cookies,headers=sp.headers).json()
個数_30個単位=240#@param {type:"number"}
raise SystemExit
for i in range(0,個数_30個単位//30):
  for record in json["feeds"]:
    try:
      record.pop("feed_type")
      requests.post("https://api.studyplus.jp/2/timeline_events/"+str(list(record.values())[0]["event_id"])+"/likes/like",cookies=sp.cookies,headers=sp.headers).json()
    except:
      continue
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/"+timeline_url+"?until="+json["next"],cookies=sp.cookies,headers=sp.headers).json()

#@title 自分の達成目標id一覧取得 {display-mode:"form"}
md="|達成目標|id|\n|--|--|\n"
for val in me.data['study_goals']:
  md+=f"|{val['label']}|{val['key']}|\n"
display(Markdown(md))

#@title 達成目標idから指定した個数いいね {display-mode:"form"}
達成目標id="college-744"# @param {type:"string"}
json=requests.get("https://api.studyplus.jp/2/timeline_feeds/study_goal/"+達成目標id,cookies=sp.cookies,headers=sp.headers).json()
個数_30個単位=1800#@param {type:"number"}

for i in range(0,個数_30個単位//30):
  for record in json["feeds"]:
    try:
      record.pop("feed_type")
      requests.post("https://api.studyplus.jp/2/timeline_events/"+str(list(record.values())[0]["event_id"])+"/likes/like",cookies=sp.cookies,headers=sp.headers).json()
    except:
      continue
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/study_goal/"+達成目標id+"?until="+json["next"],cookies=sp.cookies,headers=sp.headers).json()

#@title 指定した人にDM　{display-mode:"form"}
取得する人="\u30D5\u30A9\u30ED\u30EF\u30FC"#@param ["フォロワー","フォロー中"]
ユーザー名="ふぉれすと"#@param {type:"string"}
メッセージ="なんですか？"#@param {type:"string"}

if 取得する人=="フォロワー":
  user=next(filter(lambda x:x["nickname"]==ユーザー名,me.follower()),None)
elif 取得する人=="フォロー中":
  user=next(filter(lambda x:x["nickname"]==ユーザー名,me.followee()),None)
if user:
  data={
      "recipient":user["username"],
      "content":メッセージ
    }
  result=requests.post("https://api.studyplus.jp/2/messages",data=json.dumps(data),headers=sp.headers)
  if not result.ok:
    print('送信できません')
else:
  print('ユーザーが存在しません')

# @title 没
# import requests
# from dataclasses import dataclass,fields
# from typing import Optional

# @dataclass
# class IStudyPlusUserProfile:
#   user_id: int
#   username: str
#   user_image_url: str
#   nickname: str
#   badge_type: str
#   user_organizations: list
#   disable_reply: bool
#   allow_send_image_message: bool
#   disable_profile_view: bool
#   goal: str
#   user_relationship_id: int
#   user_relationship_status: str
#   target_user_relationship_id: int
#   target_user_relationship_status: str
#   location_code: int
#   location: str
#   job_code: int
#   job: str
#   job_grade: int
#   follower_policy: str
#   feed_visibility: str
#   desired_departments: list
#   mute: bool
#   fav: bool
#   feed_is_visible: bool
#   study_goals: list

#   def followee(self):
#     json=requests.get("https://api.studyplus.jp/2/users?followee="+self.username+"&page=1&per_page=100&include_recent_record_seconds=t").json()
#     followees=json["users"]
#     if json["page"]<json["total_page"]:
#       for i in range(2,json["total_page"]+1):
#         followees |= requests.get(self.api_root+"/users?followee="+self.username+"&page="+i+"&per_page=100&include_recent_record_seconds=t").json()
#     followeeprofiles=[]
#     print(followees)
#     for follower in followees:
#       for field in fields(IStudyPlusRelateUser):
#         if field.name not in follower:
#           follower[field.name]=""
#       followeeprofiles.append(IStudyPlusRelateUser(**follower))
#     return followeeprofiles

# @dataclass
# class IStudyPlusUser(IStudyPlusUserProfile):
#   follow_count: int
#   follower_count: int
#   follow_requesting_count: int
#   biography: str
#   tags: list
#   educational_background: dict
#   material_count: int
#   premium: bool
#   book_user: bool
#   use_drill: bool
#   studyplus_confirmed: bool
#   studylog_confirmed: bool
#   record_count: int
#   record_hours_this_month: int
#   record_hours_last_month: int
#   total_record_hours: int
#   has_study_challenge: bool
#   sex: str
#   birthyear: int
#   birthmonth: int
#   birthdate: int
#   occupation: str
#   study_achievements: list
#   examination_count: int
#   email_is_confirmed: bool
#   learning_material_review_count: int
#   learning_material_review_like_count: int
#   desired_department_visibility: str
#   sex_visibility: str
#   birthyear_visibility: str
#   birthdate_visibility: str
#   location_visibility: str
#   job_visibility: str
#   occupation_visibility: str
#   study_goals_visibility: str
#   limited_message: bool

# @dataclass
# class IStudyPlusRelateUser(IStudyPlusUserProfile):
#   recent_record_seconds:int

import json
with open('data.json','w') as f:
  json.dump(records,f,indent=2)

json=requests.get("https://api.studyplus.jp/2/timeline_feeds/learning_material/9ae3e951-807d-482e-aa85-3ee9c20093a1",cookies=sp.cookies,headers=sp.headers).json()
records=[]
for i in range(0,50):
  records+=json["feeds"]
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/learning_material/9ae3e951-807d-482e-aa85-3ee9c20093a1?until="+json["next"],cookies=sp.cookies,headers=sp.headers).json()

"""# **ユーザー情報**"""

#@title 自分のフォロワー/フォロー中一覧 {display-mode:"form"}
モード="フォロワー"#@param ["フォロワー","フォロー中"]
if モード=="フォロワー":
  userlist=me.follower()
elif モード=="フォロー中":
  userlist=me.followee()

md="|名前|id|\n|--|--|\n"
for val in userlist:
  md+=f"|{val['nickname']}|{val['username']}|\n"
display(Markdown(md))

#@title 知り合いの知り合い一覧 {display-mode:"form"}
取得する人="フォロー中"#@param ["フォロワー","フォロー中"]
ユーザー名="元頁弓長るニｼ良礻ｷ\t"#@param {type:"string"}
モード="フォロワー"#@param ["フォロワー","フォロー中"]

if 取得する人=="フォロワー":
  user=next(filter(lambda x:x["nickname"]==ユーザー名,me.follower()),None)
elif 取得する人=="フォロー中":
  user=next(filter(lambda x:x["nickname"]==ユーザー名,me.followee()),None)
print(f'{取得する人}の{ユーザー名} さんの{モード}一覧:')
if モード=="フォロワー":
  userlist=IStudyPlusUser(user).follower()
elif モード=="フォロー中":
  userlist=IStudyPlusUser(user).followee()

md="|名前|id|\n|--|--|\n"
for val in userlist:
  md+=f"|{val['nickname']}|{val['username']}|\n"
display(Markdown(md))

#@title ユーザーidから情報を取得 {display-mode:"form"}
username="e334060885a8483996b2025a78d4b77c"#@param {type:"string"}
user=IStudyPlusUser(requests.get("https://api.studyplus.jp/2/users/"+username).json())
print(user.data["nickname"]+"さんの情報:")
pprint.pprint(user.data)

# @title zennkome
検索元="\u30D5\u30A9\u30ED\u30EF\u30FC"#@param ["フォロワー","フォロー中","id指定"]
名前またはid="誠"#@param {type:"string"}
メッセージ="jjj"#@param {type:"string"}
if 検索元=="フォロワー":
  user=next(filter(lambda x:x["nickname"]==名前またはid or x["username"]==名前またはid,me.follower()),None)
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+user["username"],cookies=sp.cookies,headers=sp.headers).json()
elif 検索元=="フォロー中":
  user=next(filter(lambda x:x["nickname"]==名前またはid or x["username"]==名前またはid,me.followee()),None)
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+user["username"],cookies=sp.cookies,headers=sp.headers).json()
else:
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+名前またはid,cookies=sp.cookies,headers=sp.headers).json()

for i in range(0,2000):
  count=0
  for record in json["feeds"]:
    try:
      record.pop("feed_type")
      body=list(record.values())[0]
      if body["if_you_like"]:
        count+=1
        continue
        data={
              "post_token": "sp.create_token()",
              "comment": "ua"
        }
      requests.post("https://api.studyplus.jp/2/timeline_events/"+str(body["event_id"])+"/comments/",data=json.dumps(data),cookies=sp.cookies,headers=sp.headers).json()
    except:
      continue
  if count==len(json["feeds"]) and i>100:
    break
  json=requests.get("https://api.studyplus.jp/2/timeline_feeds/user/"+user["username"]+"?until="+json["next"],cookies=sp.cookies,headers=sp.headers).json()

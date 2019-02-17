import requests
from slack import slack

def fetchLatestTestVideos():
  response = requests.get(
    url="https://space.bilibili.com/ajax/member/getSubmitVideos",
    params={
      "mid": "11336264",
      "pagesize": "1",
      "tid": "0",
      "page": "1",
      "keyword": "值不值得买",
      "order": "pubdate",
    }
  )

  videos = response.json()["data"]["vlist"]
  videos = [
    (
    video['aid'], video["title"], video["description"], f"https:{video['pic']}")
    for video in videos
  ]

  for (aid, title, summary, coverUrl) in videos:
    appUrl = f"bilibili://video/{aid}"
    webUrl = f"https://www.bilibili.com/video/av{aid}"
    slack.api_call(
      "chat.postMessage",
      channel="#review",
      username="TESTV",
      icon_url="https://tva1.sinaimg.cn/crop.0.0.640.640.180/005QGjbqjw8f884tmcirlj30hs0hs0sw.jpg",
      attachments=[
        {
          "fallback": title,
          "title": title,
          "title_link": webUrl,
          "image_url": coverUrl,
          "text": summary,
          "actions": [
            {
              "type": "button",
              "text": "本期视频",
              "url": appUrl
            },
            {
              "type": "button",
              "text": "TESTV 主页",
              "url": "bilibili://space/11336264"
            }
          ]
        }
      ]
    )

def main():
  fetchLatestTestVideos()

if __name__ == '__main__':
  main()

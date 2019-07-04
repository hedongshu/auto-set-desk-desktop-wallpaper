## auto set desktop background IMG

自动把你的桌面壁纸设置成bing的每日推荐

1. 修改`bingBGIMG.py`内容,  设置好图片存放路径.

2. 修改 `.crontab` 里面的cron表达式, 就是设置一下定时任务


4. 设置定时任务
    ```shell
    sudo crontab -u Frank [.crontab](这里写路径)
    ```
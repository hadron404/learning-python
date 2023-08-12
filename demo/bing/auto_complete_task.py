import subprocess
from time import sleep

from random_words import RandomWords


# adb shell pm list package 获取手机内所有apk对应的包名及路径
# adb shell 进入Android终端
# dumpsys package 包名 获取主Activity,回车之后找到包含“category.LAUNCHER” 字样的Activity即可

def is_app_started():
    subprocess.run('adb shell dumpsys window w')


def start_app(package_name, main_activity):
    subprocess.run(f'adb shell am start {package_name}/{main_activity}',
                   shell=True)
    sleep(4)


def stop_app(package_name):
    subprocess.run(f'adb shell am force-stop {package_name}')


def swipe(x, y, target_x, target_y):
    subprocess.run(f'adb shell input swipe {x} {y} {target_x} {target_y}')


def touch(x, y):
    subprocess.run('adb shell input tap {} {}'.format(x, y))


def input_text(s):
    subprocess.run('adb shell input text {}'.format(s))


def press_back_key():
    subprocess.run('adb shell input keyevent 4')


def search(s):
    touch(300, 500)
    sleep(1)
    input_text(s)
    sleep(1)
    touch(1284, 2902)
    sleep(3)
    press_back_key()
    sleep(2)


def more_search(count):
    for cnt in range(1, count):
        word = rw.random_words()
        print('第 {} 次搜索 {}'.format(cnt, word))
        search(word[0])


def browse_news():
    swipe(550, 2600, 550, 4000)
    sleep(5)
    touch(550, 2800)
    sleep(6)
    touch(50, 180)
    sleep(1)


def more_browse_news(count):
    for cnt in range(0, count):
        browse_news()


if __name__ == "__main__":
    rw = RandomWords()
    # is_app_started()

    # start_app('com.microsoft.bing', 'com.microsoft.sapphire.app.main.SapphireMainActivity')
    # more_search(20)
    more_browse_news(30)

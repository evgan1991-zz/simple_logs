import time
import sys
import os
import SimpleHTTPServer
import SocketServer
import threading
import datetime


def writing_to_log():
    f = open('index.html', 'a')
    first_answer  = str(os.popen('nohup iftop -t -s 1 &').read())
    first_answer_arr = first_answer.split('\n')
    time.sleep(1)
    print(first_answer_arr[4])
    f.write('<p>' + first_answer_arr[4] + '</p>\n')

    while True:
        answer = str(os.popen('nohup iftop -t -s 1 &').read())
        time.sleep(1)
        print('\n' + str(datetime.datetime.now()))
        f.write('\n')
        answer_arr = answer.split('\n')
        i = 0
        for x in answer_arr:
            i += 1
            if i > 6 and i < len(answer_arr) - 9:
                f.write('<p>' + x + '</p>\n')
                print(x)
    f.close()


def creatind_index():
    file = open('index.html', 'w')
    file.write('<p>Start Log</p>\n')
    file.close()


if __name__ == '__main__':
    os.system('scout_realtime start && nohup npm run start:prod &')
    print(' ====================================================')
    print('| Open \"localhost:3000\" to see the web-application. |')
    print('| Open \"localhost:5555\" to see the info-page.       |')
    print(' ====================================================')
    creatind_index()
    writing_to_log()

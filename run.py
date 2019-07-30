import os

if __name__ == '__main__':
    os.system('scout_realtime start && nohup npm run start:prod &')
    print('Open \"localhost:3000\" to see the web-application.')
    print('Open \"localhost:5555\" to see the info-page.')

import queue
import os


class Cooooooooooooooooooooore:
    def __init__(self, getFilePath):
        self.hitKillList = queue.Queue()
        self.getFilePath = getFilePath

    def getHitKillList(self):
        file = open(self.getFilePath, 'r', encoding='utf-8')
        for i in file.readlines():
            self.hitKillList.put(i.strip('\n'))
        return self.hitKillList

    def getVuuuuuuuln(self):
        while True:
            if self.hitKillList.empty():
                print('[-]字典为空')
                return
            else:
                '''
                good luck :)
                '''
                file = open('./ScannedDomain.txt', 'a', encoding='utf-8')
                file.writelines(self.hitKillList.get() + '\n')
                Command = '{} -t {} -http-proxy 127.0.0.1:7777 '.format('rad_windows_amd64.exe', self.hitKillList.get())
                os.system(Command)
                print('[+]{}扫描完毕'.format(self.hitKillList.get()))
                file.close()


if __name__ == '__main__':
    start = Cooooooooooooooooooooore('./ForHitKill/edu.txt')
    start.getHitKillList()
    start.getVuuuuuuuln()

import random
import sys
import time

class UseTxt:
    def ReadTxt(path):
        with open(path,'r') as txt_r:
            txt = txt_r.readlines()
        return txt
    def AnaTxt(path):
        txt_str = UseTxt.ReadTxt(path)
        txt = []
        for line in txt_str:
            mess = line.replace('''\n''','').split(',')
            mess[1] = int(mess[1])
            txt.append(mess)
        return txt

def RandomTeam(Guys,TeamNum):
    keys = []
    mates = 4*TeamNum
    Teams = {}
    team = []
    while(len(keys)< mates):
        key = random.randint(0,mates-1)
        if(key not in keys):
            keys.append(key)
    t = 1
    n = 0
    for num,key in enumerate(keys):
        if(num < mates):     
            team.append(Guys[key])
            n += 1
            if(n>3):
                Teams["Team{}".format(t)] = team
                t += 1
                n = 0
                team = []
    audience = []
    for i in range(len(keys),len(Guys)):
        audience.append(Guys[key])
    Teams["audience"] = audience
    return Teams 

def WriteLog(Teams):
    txt = ""
    for num in Teams:
        team = Teams[num]
        txt += num
        txt += ':'
        for guy in team:
            txt += guy
            if(guy == team[-1]):
                txt+= '\n'
            else:
                txt += ','
    print(txt)
    localtime = time.localtime(time.time())
    Date = str(localtime.tm_year)+'-'+str(localtime.tm_mon)+'-'+str(localtime.tm_mday)
    
    with open(sys.path[0]+ "/logs/{}.txt".format(Date),'w') as txr_w:
        txr_w.write(txt)


if __name__ == '__main__':
    TxtPath = sys.path[0]+ "/logs/Histriones.csv"
    txt = UseTxt.AnaTxt(TxtPath)
    ReadyGuys = []
    for line in txt:
        if(line[1] == 0):
            ReadyGuys.append(line[0])
    try:
        assert (len(ReadyGuys) >= 8)
        Team = RandomTeam(ReadyGuys,2)
        WriteLog(Team)
    except:
        print("程序报错或参与人数不足8人")

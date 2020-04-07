import matplotlib.pyplot as plt
from random import randint

class tcp_sender:
    cwnd = 0
    ssthresh = 64
    receiver=None
    data_length=0
    rounds=[]
    cwnd_records=[]
    def __init__(self,cwnd,ssthresh,data_length):
        self.cwnd=cwnd
        self.ssthresh=ssthresh
        self.receiver=tcp_receiver()
        self.data_length=data_length
    def start_transmission(self):
        round=0
        while(self.data_length>0):
            slow_start = True
            if (self.cwnd > self.ssthresh):
                slow_start =False
            self.data_length-=self.cwnd
            result=self.receiver.send_ack(cwnd=self.cwnd)
            if(result==self.receiver.ACK): #未拥塞
                if(slow_start):
                    self.cwnd*=2
                else:
                    self.cwnd+=1
            elif(result==self.receiver.TIMEOUT):
                self.data_length+=self.cwnd
                self.ssthresh=self.cwnd/2
                self.cwnd=1
            else:
                self.ssthresh=self.cwnd/2
                self.cwnd=self.ssthresh
            round+=1
            self.rounds.append(round)
            self.cwnd_records.append(self.cwnd)
        print(self.rounds)
        print(self.cwnd_records)


class tcp_receiver:
    ACK=0
    THREE_DUP_ACK=1
    TIMEOUT=2
    def __init__(self):
        pass
    def send_ack(self,cwnd):
        congestion_possibility=cwnd#拥塞概率为cwnd/100
        if(randint(1,101)<congestion_possibility):
            if(randint(1,101)<80):
                return self.THREE_DUP_ACK
            else:
                return self.TIMEOUT
        else:
            return self.ACK

def main():
    tcp_snder=tcp_sender(1,16,200)#cwnd,ssthresh,data长度
    tcp_snder.start_transmission()
    plt.plot(tcp_snder.rounds,tcp_snder.cwnd_records,color='red',linewidth=2.0,linestyle='-')
    plt.show()
if __name__ == '__main__':
    main()
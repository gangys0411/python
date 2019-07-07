class theater:
    def __init__(self, name, time1, time2, time3, time4, money): # 각 상영관에서 상영하는 영화의 이름, 시간, 수익을 저장
        self.name = name
        self.time1 = time1
        self.time2 = time2
        self.time3 = time3
        self.time4 = time4
        self.money = money

    def showtime(self): # 상영 시간을 보여줌
        print(self.time)

    def earnmoney(self, profit): # 이익 계산
        self.money += profit

class Seat:
    def __init__(self, seat): # 각 영화마다 좌석을 입력받음
        self.seat = seat

    def showseat(self): # 현재 좌석 예매 상황을 알려줌
        for i in range(5):
            for j in range(5):
                if seat[i][j] == 0: # 좌석이 비어있으면
                    if i == 0:
                        print("A" + str(j + 1) + " ")
                    if i == 1:
                        print("B" + str(j + 1) + " ")
                    if i == 2:
                        print("C" + str(j + 1) + " ")
                    if i == 3:
                        print("D" + str(j + 1) + " ")
                    if i == 4:
                        print("E" + str(j + 1) + " ")
                else: # 좌석이 비어있지 않다면
                    print "X "
            print "\n"

movie_price = [5000, 7000, 8000] # 영화표 가격 어린이, 청소년, 어른

movie1 = theater("1편", "09:00", "11:00", "13:00", "15:00", 0)
movie1_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

movie2 = theater("2편", "10:00", "12:30", "15:00", "17:30", 0)
movie2_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

movie3 = theater("3편", "08:00", "11:00", "14:00", "17:00", 0)
movie3_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])


def systemstart():
    print("원하는 기능을 선택해 주세요.\n1. 영화 예매\n2. 영화 상영 시간 확인\n3. 총 수입 확인\n4. 프로그램 종료\n") # 원하는 기능을 선택
    menu_select = input()

    if(menu_select == 1):
        print("예매하실 영화를 선택해 주세요.\n1. {}\n2. {}\n3. {}\n".format(movie1.name, movie2.name, movie3.name))
        movie_select = input()
        

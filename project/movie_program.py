class theater:
    def __init__(self, name, time1, time2, time3, time4, money, allseat): # 각 상영관에서 상영하는 영화의 이름, 시간, 수익을 저장
        self.name = name
        self.time = [time1, time2, time3, time4]
        self.money = money
        self.allseat = allseat

    def earnmoney(self, profit): # 이익 계산
        self.money += profit

class Seat:
    def __init__(self, seat): # 각 영화마다 좌석을 입력받음
        self.seat = seat

    def showseat(self): # 현재 좌석 예매 상황을 알려줌
        for i in range(5):
            for j in range(5):
                if self.seat[i][j] == 0: # 좌석이 비어있으면
                    if(i == 0):
                        if(j == 4):
                            print("A" + str(5))
                        else:
                            print("A" + str(j + 1), end=" ")
                    if(i == 1):
                        if (j == 4):
                            print("B" + str(5))
                        else:
                            print("B" + str(j + 1), end = " ")
                    if(i == 2):
                        if (j == 4):
                            print("C" + str(5))
                        else:
                            print("C" + str(j + 1), end = " ")
                    if(i == 3):
                        if (j == 4):
                            print("D" + str(5))
                        else:
                            print("D" + str(j + 1), end = " ")
                    if(i == 4):
                        if (j == 4):
                            print("E" + str(5))
                        else:
                            print("E" + str(j + 1), end = " ")
                else: # 좌석이 비어있지 않다면
                    if (j == 4):
                        print("XX")
                    else:
                        print("XX", end=" ")
        print("")

movie_price = [5000, 7000, 8000] # 영화표 가격 어린이, 청소년, 어른

movie1_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
all_time1 = [movie1_time1, movie1_time2, movie1_time3, movie1_time4]
movie1 = theater("1편", "09:00", "11:00", "13:00", "15:00", 0, all_time1)

movie2_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
all_time2 = [movie2_time1, movie2_time2, movie2_time3, movie2_time4]
movie2 = theater("2편", "10:00", "12:30", "15:00", "17:30", 0, all_time2)


movie3_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
all_time3 = [movie3_time1, movie3_time2, movie3_time3, movie3_time4]
movie3 = theater("3편", "08:00", "11:00", "14:00", "17:00", 0, all_time3)

all_movie = [movie1, movie2, movie3]

#--------------------------------영화 예매-----------------------------------------

def people():
    try:
        print("인원 수를 입력해 주세요")
        people_num = int(input())
    except ValueError:
        print("숫자만 입력해주세요\n")
        people()


def viewseat(movie_select, time_select): # 좌석 현황 확인 함수
    print("선택하신 시간의 좌석 상황은 다음과 같습니다.\n영화 : {}\n상영 시간 : {}\n".format(all_movie[movie_select - 1].name, all_movie[movie_select - 1].time[time_select - 1]))
    all_movie[movie_select - 1].allseat[time_select - 1].showseat()

    people()


def viewtime(movie_select): #상영 시간 선택 함수
    print("상영 시간을 선택해 주세요.\n1. {}\n2. {}\n3. {}\n4. {}\n".format(all_movie[movie_select - 1].time[0], all_movie[movie_select - 1].time[1], all_movie[movie_select - 1].time[2], all_movie[movie_select - 1].time[3],))
    time_select = int(input())
    if(time_select != 1 and time_select != 2 and time_select != 3 and time_select != 4):
        print("잘못 입력하셨습니다. 다시 입력해주세요\n")
        viewtime(movie_select)
    else:
        viewseat(movie_select, time_select)


def moviebuy(): #영화 선택 함수
    print("예매하실 영화를 선택해 주세요.\n1. {}\n2. {}\n3. {}\n".format(movie1.name, movie2.name, movie3.name))
    movie_select = int(input())

    if(movie_select != 1 and movie_select != 2 and movie_select != 3):
        print("잘못 입력하셨습니다. 다시 입력해주세요\n")
        moviebuy()
    else:
        viewtime(movie_select)

#------------------------------------상영 시간 확인----------------------------------------------

def movietime():
    print("상영 시간을 확인하고 싶은 영화를 선택해 주세요\n1. {}\n2. {}\n3. {}\n".format(movie1.name, movie2.name, movie3.name))
    movietime_select = int(input())
    if(movietime_select == 1):
        print("선택하신 영화의 상영 시간은 다음과 같습니다.\n영화 : {}\n상영 시간 : {} {} {} {}\n".format(movie1.name, movie1.time[0:5]))
    elif(movietime_select == 2):
        print("선택하신 영화의 상영 시간은 다음과 같습니다.\n영화 : {}\n상영 시간 : {} {} {} {}\n".format(movie2.name, movie2.time[0:5]))
    elif(movietime_select == 3):
        print("선택하신 영화의 상영 시간은 다음과 같습니다.\n영화 : {}\n상영 시간 : {} {} {} {}\n".format(movie3.name, movie3.time[:5]))
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요\n")
        movietime()




def systemstart():
    print("원하는 기능을 선택해 주세요.\n1. 영화 예매\n2. 영화 상영 시간 확인\n3. 총 수입 확인\n4. 프로그램 종료\n") # 원하는 기능을 선택
    menu_select = int(input())

    if(menu_select == 1):
        moviebuy()
    elif(menu_select == 2):
        movietime()
    elif(menu_select == 3):
        viewprofit()
    elif(menu_select == 4):
        exit()
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요\n")
        systemstart()



systemstart()

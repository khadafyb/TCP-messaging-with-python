import socket
import threading
youships = []
oppships=[]
class battleship:

    def __init__(self):
        self.board=[]
        self.turn = "*"
        self.you="*"
        self.opp="+"
        self.winner="none"
        self.game_over=False
        self.setup=True

    def host_game(self,host,port):
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((host,port))
        server.listen(1)

        client,addr=server.accept()
        self.you="*"
        self.opp="+"
        self.board=youships
        threading.Thread(target=self.handle_connection,args=(client,)).start()
        print("created game")
        server.close()

    def con_to_gamae(self,host,port):
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((host,port))

        self.you="player2"
        self.opponent="player1"
        self.board=oppships
        threading.Thread(target=self.handle_connection,args=(client,)).start()
        print("connected to game")

    def handle_connection(self,client):
        if self.setup:
            count=0
            if self.turn==self.you:
                
                while count<5:
                    ship=int(input("enter a number <15"))
                    self.board.append(ship)
                    ++count
                self.turn=self.opp
        self.setup=False
        while not self.game_over:
            if self.turn == self.you:
                move=int(input("Enter a move: "))
                if move<16:
                    if (move in self.youships):
                        client.send(move.encode('utf-8'))
                        print(self.you+" hit "+self.opp+" ship")
                        self.youships.remove(move)
                        if not self.youships:
                            print("game over")
                            self.game_over=True
                        self.turn = self.opponent
                    
                else:
                    print("invalid move")
            else:
                data = client.recv(1024)
                if not data:
                    break
                else:
                    if self.setup:
                        if self.turn==self.opp:
                            while count<5:
                                ship=int(data.decode('utf-8'))
                                self.oppships.append(ship)
                                ++count
                                self.turn=self.opp
                    move=int(data.decode('utf-8'))
                    if move<16:
                        if (move in self.board):
                            client.send(move.encode('utf-8'))
                            print(self.opp+" hit "+self.you+" ship")
                            self.oppships.remove(move)
                            if not self.oppships:
                                print("game over")
                                self.game_over=True
                            self.turn = self.you
        client.close()
game=battleship()
game.host_game("localhost",1233)

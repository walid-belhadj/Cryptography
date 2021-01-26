class playFair: 
    def __init__(self,key):
        self.key = key
    def matrix(self,key):
        matrix = []
        for e in key.lower():
            if e not in matrix:
                matrix.append(e)
            alphabet ="abcdefghijklmnopqrstuvwxyz"

            for e in alphabet:
                if e not in matrix:
                    matrix.append(e)
    # init a new list 
    matrix_group=[]
    for e in range(5):
        matrix_group.append('')
    # 5 x 5 
    matrix_group[0] = matrix[0:5]
    matrix_group[1] = matrix[5:10]
    matrix_group[2] = matrix[10:15]
    matrix_group[3] = matrix[15:20]
    matrix_group[4] = matrix[20:25]
    return matrix_group
def msg_to_encry(self, msg_org):
    # change it to array 
    msg = []
    for e in msg_org.lower():
        msg.append(e)
    #delete spaces 
    for unused in len(msg):
        if " " in msg:
            msg.remove(" ")
    # if both of letter are same addan x after the letter 
    i = 0
    for e in range( int(len(msg) / 2 )):
        if msg[i] == msg[i+1]:
            msg.insert(i+1, 'x')
        i+=2
    # if is odd digit add an x at the end impair
    if len(msg)%2 == 1:
        msg.append("x")
    #grouping 2 par deux 
    i = 0 
    new = []
    for x in range(1, int(len(msg)/ 2 ) + 1):
        new.append(msg[i:i+2])
        i = i + 2
    return new
    # find position de chauqe lettre 
    def find_position(self, key_matrix, letter):
        x = y = 0
        for i in range(5):
            for j in range(5):
                if key[i][j] == letter:
                    x = 1 
                    y = j
        return x , y 
    def encrypt(self, msg):
        msg = self.msg
        pass    


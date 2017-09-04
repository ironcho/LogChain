# self node 부분에서 아이디를 새로 생성, ip 받아오기 등을 해서 self_node에 넣어줘야 한다.
# self_node = None, self.index = [], linked_node = [], state = []  index는 언제든 빼도 된다. list index search로 하여 간단하게 처리도 가능 하기 때문에.
import json
import socket
import Property
class Table:
    count = 0
    def __init__(self):
        self.self_node = None
        self.index = []
        self.linked_node = []
        self.state = []

    def table_create(self, self_node):
        self.self_node = self_node
        print('MAKE TABLE %s' %(self.self_node))

        #self.self_node = self_node

    def table_add(self, linked_node, state):
        print('ADD TABLE %s' %(linked_node))
        self.index.append(Table.count)
        self.linked_node.append(linked_node)
        self.state.append(state)
        Table.count += 1

    def table_update(self, linked_node, state):
        print('update table %s with %s' % (linked_node, state))
        ind= self.linked_node.index(linked_node)
        self.state[ind] = state

#출력 확인용 -> 추후에 파일 입출력으로 변환 예정.
    def print_table(self):
        num = Table.count
        print('Number of linked node %d' %(num))
        print('index         self_node              linked_node             state')
        for i in range(num):
            print('  %d           %s            %s          %s'%(self.index[i], self.self_node,  self.linked_node[i], self.state[i]))

    def write_table(self):
        nodeinfo = json.dumps(self, default=lambda o: o.__dict__)
        print(nodeinfo)
        f = open('nodeinfo.txt', 'w')
        f.write(nodeinfo)
        f.close()

def read_nodeinfo():
    f = open('nodeinfo.txt','r')
    info = f.read()
    nodeinfo = json.loads(info)
    return nodeinfo

## 만약 새로운 노드라면 ~, 아니고 기존 노드라면 ~ 이러한 정보를 text로 부터 읽고 판단 하여야 한다.


#초기화에서 블록 갯수, 트랜잭션의 갯수 동기화 작업을 한번씩 해줘야 한다. 최초 참여일 경우와 아닐 경우를 나눠서 해야함.
# 이니셜라이즈 와 싱크로나이즈 로 시나리오가 두개 존재 해야함.
def initialize():
    Property.my_ip = socket.gethostbyname(socket.gethostname())

    Property.my_node = Table()
    Property.my_node.table_create(socket.gethostbyname(socket.gethostname()))
    #Property.my_node = read_nodeinfo()
    #print(Property.my_node)
    # add 에서 txt를 읽어 최초로 connection 일어날수 있게. 적어도 하나 이상의 컴퓨터는 항상 켜져있는상태.
    # super node ip 정보는 파일로 부터 읽어 들이기.
    #f = open('supernode.txt','r')
    #supernode = f.read()
    #Property.my_node.table_add(Property.my_ip, 'stable')
    #Property.my_node.table_add('192.168.0.96', 'stable')
    #Sender.sending_connection('192.168.0.96')
    #요기부분이.
    Property.my_node.print_table()




import numpy as np

def init_network():
    network = {} #자료형을 딕셔너리로 정의 (대괄호 리스트, 소괄호 튜플)
    #입력신호가 인가되고 아래와 계산되어져서 출력됨
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) # 키벨류 형태로 데이터 저장
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['B2'] = np.array([0.1,0.2])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['B3'] = np.array([0.1, 0.2])

    return network

#활성화 함수 - 시그모이드
def sigmoid(x):
    return 1/(1+np.exp(-x))

# 항등 함수의 정의 - 출력단
def identity_function(x):
    return x

# 데이터 전달
def forward(network, x): # x :: 첫 입력단 데이터 입력
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    B1, B2, B3 = network['B1'], network['B2'], network['B3']

    a1 = np.dot(x,W1) + B1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + B2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + B3
    y = identity_function(a3) #마지막 항등함수 적용

    return  y

if __name__ == "__main__":
    network = init_network() #network 리턴
    x = np.array([1.0, 0.5])
    y = forward(network, x)

    print(y) # [0.31682708 0.69627909]

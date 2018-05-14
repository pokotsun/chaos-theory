import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

def W(point, func):
    x, y = point
    return func(x, y) 

def W1(point):
    return W(point, (lambda x, y: (0.836*x + 0.044*y, -0.044*x + 0.836*y + 0.169)))

def W2(point):
    return W(point, (lambda x, y: (-0.141*x + 0.302*y, 0.302*x+0.141*y + 0.127)))

def W3(point):
    return W(point, (lambda x, y: (0.141*x - 0.302*y, 0.302*x + 0.141*y + 0.169)))

def W4(point):
    return W(point, (lambda x, y: (0, 0.175337*y))) 

# IFSのシダの葉っぱのgeneratorを作成
def IFS_list(initial_x, initial_y):
    now_point = next_point = (initial_x, initial_y)

    while True:
        rand = randint(1, 6) # 1 ~ 6までの数字をランダムに取得 
        #print(f" rand: {rand} ")
        if rand is 1 or rand is 2 or rand is 3:
            next_point = W1(now_point) 
        elif rand is 4:
            next_point = W2(now_point)
        elif rand is 5:
            next_point = W3(now_point)
        else: # rand == 6のとき
            next_point = W4(now_point)
        
        yield next_point
        now_point = next_point

def _update_plot(i, ifs_list):
    x, y = next(ifs_list) 
    
    #print(f"(x,y) = ({x}, {y})")

    plt.plot([x], [y], '.', markersize=3)
    plt.xlim([-0.5, 0.5])
    plt.ylim([0, 1])
    
def main():
    ifs_list = IFS_list(0.1, 0.1)

    fig = plt.figure()
    ani = animation.FuncAnimation(fig, _update_plot, fargs=(ifs_list,), interval=1, frames=30000000)

    plt.show()





if __name__=='__main__':
    main()

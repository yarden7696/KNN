from __future__ import print_function
import random

""" 
Names: Cohen Yarden 207205972
       Shalel Shani 206134033
we worked together on this Submission assignment.
"""

"""
OUR OUTPUT IS:

KNN for HC Temperature : 
p= 1

k= 1
True Error Average:  0.4572307692307692
Empirical Error Average:  0.030923076923076925

k= 3
True Error Average:  0.4366153846153846
Empirical Error Average:  0.22553846153846155

k= 5
True Error Average:  0.4595384615384615
Empirical Error Average:  0.2816923076923077

k= 7
True Error Average:  0.4775384615384615
Empirical Error Average:  0.3089230769230769

k= 9
True Error Average:  0.4736923076923077
Empirical Error Average:  0.3395384615384615
_______________________________________________
p= 2

k= 1
True Error Average:  0.4584615384615385
Empirical Error Average:  0.03

k= 3
True Error Average:  0.44753846153846155
Empirical Error Average:  0.2409230769230769

k= 5
True Error Average:  0.4695384615384615
Empirical Error Average:  0.2793846153846154

k= 7
True Error Average:  0.4706153846153846
Empirical Error Average:  0.3153846153846154

k= 9
True Error Average:  0.4796923076923077
Empirical Error Average:  0.3476923076923077
_______________________________________________
p= inf

k= 1
True Error Average:  0.4744615384615385
Empirical Error Average:  0.02923076923076923

k= 3
True Error Average:  0.46
Empirical Error Average:  0.23369230769230767

k= 5
True Error Average:  0.46692307692307694
Empirical Error Average:  0.31076923076923074

k= 7
True Error Average:  0.46876923076923077
Empirical Error Average:  0.3401538461538462

k= 9
True Error Average:  0.486
Empirical Error Average:  0.35307692307692307
_______________________________________________

"""

""" Which parameters of k,p are the best?
The best parameters for k and p are: k=3 ,p=1 with True Error  0.4366153846153846
"""

""" Do you see overfitting? yes 
To get overffiting, the learning about the points of the train must be very good.
In addition - given a new point from the test set we will not know how to classify it. 
Its mean that the classification of the test points will be poor and will yield very low results relative to the train.
We see this in HC_Body_Temperature result because for the points of the test- we got bad results that are not 
close to the results of the train. 
When k = 1, the overfitting is the largest between the True Error and the Empirical Error.
As k increases the difference between the True Error and the Empirical Error decreases,
but in our opinion it is still large and shows on overfitting.
"""


def KNN_classified(train, point, k, p):
    distance=[]
    for group in train:
        for feature in train[group]:
            if p==1 or p==2:
                Lp = (abs(float(feature[0]) - float(point[0])) ** float(p) + abs(float(feature[1]) - float(point[1])) ** float(p)) ** (1 / float(p))
            else:
                Lp =float(max(abs(float(feature[0]) - float(point[0])), abs(float(feature[1]) - float(point[1]))))
            distance.append((Lp, group))

    distance = sorted(distance)[:k] # Sorting distances from smaller to larger

    over0, over1 = 0,0
    for d in distance:   # sum the majority of the labels
        if d[1] == 0:
            over0 += 1
        elif d[1] == 1:
            over1 += 1
    return 0 if over0 > over1 else 1



# this function split the points to train_set and test_set
def random_list (List):
    List = random.sample(List,len(List)) # order the list in random way
    training, testing = List[:len(List)//2], List[len(List)//2:] # fill the training and testing
    train = {0:[], 1:[]}  # 0 is label '1' , 1 is label '2'

    for i in training:
        if i[1] == '1':
            train[0].append((float(i[0]),float(i[2])))
        elif i[1] == '2':
            train[1].append((float(i[0]),float(i[2])))
    test = {0:[],1:[]} # 0='1' , 1='2'

    for i in testing:
        if i[1] == '1':
            test[0].append((float(i[0]),float(i[2])))
        elif i[1] == '2':
            test[1].append((float(i[0]),float(i[2])))
    return train, test



def main():
    f = open("HC_Body_Temperature", "r")
    List = []
    for i in f:
        List.append(i.split())

    P = [1, 2, 'inf']  # Euclidean distance
    EROR_test,EROR_train=0,0
    print("KNN for HC Temperature : ")
    # evaluate the k-NN classifier
    for p in P:  # {1,2,inf}
        print("p=",p)
        for k in range(1, 10, 2):  # {1,3,5,7,9}
            EROR_train=0
            EROR_test=0
            for i in range(100):
                train, test = random_list(List)
                for x in test[0]:  # classify '1'
                    if KNN_classified(train, x, k, p) == 1:  # '1' in function KNN_classified is '2' and that why is wrong
                        EROR_test+= 1
                for x in test[1]:  # classify '2'
                    if KNN_classified(train, x, k, p) == 0: # '0' in function KNN_classified is '1' and that why is wrong
                        EROR_test+=1
                for x in train[0]:
                    if KNN_classified(train, x, k, p) == 1:
                        EROR_train+=1
                for x in train[1]:
                    if KNN_classified(train, x, k, p) == 0:
                        EROR_train+=1
            print("")
            print("k=",k)
            print("True Error Average: ", float(EROR_test)/65/100)
            print ("Empirical Error Average: ", float(EROR_train)/65/100)
        print("_______________________________________________")


if __name__ == '__main__':
    main()

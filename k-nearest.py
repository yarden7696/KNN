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
k= 1

p= 1
True Error Average:  0.45784615384615385
Empirical Error Average:  0.025692307692307695

p= 2
True Error Average:  0.47646153846153844
Empirical Error Average:  0.026923076923076925

p= inf
True Error Average:  0.4604615384615385
Empirical Error Average:  0.030153846153846153
_______________________________________________
k= 3

p= 1
True Error Average:  0.43769230769230766
Empirical Error Average:  0.22753846153846155

p= 2
True Error Average:  0.44584615384615384
Empirical Error Average:  0.22953846153846155

p= inf
True Error Average:  0.456
Empirical Error Average:  0.2473846153846154
_______________________________________________
k= 5

p= 1
True Error Average:  0.46276923076923077
Empirical Error Average:  0.27753846153846157

p= 2
True Error Average:  0.45569230769230773
Empirical Error Average:  0.28692307692307695

p= inf
True Error Average:  0.4793846153846154
Empirical Error Average:  0.31215384615384617
_______________________________________________
k= 7

p= 1
True Error Average:  0.4786153846153846
Empirical Error Average:  0.3123076923076923

p= 2
True Error Average:  0.47261538461538466
Empirical Error Average:  0.3143076923076923

p= inf
True Error Average:  0.47830769230769227
Empirical Error Average:  0.3324615384615385
_______________________________________________
k= 9

p= 1
True Error Average:  0.47200000000000003
Empirical Error Average:  0.3410769230769231

p= 2
True Error Average:  0.4766153846153846
Empirical Error Average:  0.3475384615384616

p= inf
True Error Average:  0.4793846153846154
Empirical Error Average:  0.35261538461538466
_______________________________________________
"""

""" Which parameters of k,p are the best?
The best parameters for k and p are: k=3 ,p=1 with True Error 0.43769230769230766
"""

""" Do you see overfitting? yes 
To get overffiting, the learning about the points of the train must be very good.
In addition - given a new point from the test set we will not know how to classify it. 
Its mean that the classification of the test points will be poor and will yield very low results relative to the train.
We see this in HC_Body_Temperature result because for the points of the test- we got bad results that are not 
close to the results of the train. 
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
    for k in range(1, 10, 2): # {1,3,5,7,9}
        print("k=",k)
        for p in P:  # {1,2,inf}
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
            print("p=",p)
            print("True Error Average: ", float(EROR_test)/65/100)
            print ("Empirical Error Average: ", float(EROR_train)/65/100)
        print("_______________________________________________")


if __name__ == '__main__':
    main()

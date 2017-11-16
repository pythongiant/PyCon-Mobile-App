import matplotlib.pyplot as plt
from sklearn import svm
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer

data=[]
for i in range(1,14):
    data.append(plt.imread("My-Photos/"+str(i)+".jpg"))
data.append(plt.imread("My-Photos/headphone.jpg"))
data.append(plt.imread("My-Photos/headphone2.jpg"))
data.append(plt.imread("My-Photos/headphone3.jpg"))
data.append(plt.imread("My-Photos/headphone4.jpg"))
data.append(plt.imread("My-Photos/headphone5.jpg"))
data.append(plt.imread("My-Photos/headphone6.jpg"))
data.append(plt.imread("My-Photos/headphone7.jpg"))
data.append(plt.imread("My-Photos/headphone8.jpg"))
data.append(plt.imread("My-Photos/headphone9.jpg"))
data.append(plt.imread("My-Photos/headphone10.jpg"))
data.append(plt.imread("My-Photos/headphone11.jpg"))
data.append(plt.imread("My-Photos/13.jpg"))

for i in range(0,9):
    plt.imshow(data[i])

clf = svm.SVC()
y=[]
for i in range(0,13):
    y.append("Me")
for i in range(0,12):
    y.append("headphone")   
np_data = numpy.asarray(data)    
np_y=numpy.asarray(y)
new_np_data=np_data.reshape(len(np_data),-1)
newnp_y=np_y.reshape(len(np_y),-1)
print(np_data)

test=[plt.imread("My-Photos/14.jpg")]
np_test=numpy.asarray(test)
new_np_test=np_test.reshape(len(np_test),-1)

print(new_np_test)


clf.fit(new_np_data,newnp_y)    
print(clf.predict(new_np_test))

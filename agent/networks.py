import torch.nn as nn
import torch.nn.functional as F

"""
Imitation learning network
"""
class FCN(nn.Module):

    def __init__(self,hidden_layers,dim_state=8,history_length=0, n_classes=4): 
        super(FCN, self).__init__()
        # TODO : define layers of a  fully-connected neural network
        
        self.fc1=nn.Linear(dim_state,hidden_layers)
        self.fc2=nn.Linear(hidden_layers,int(hidden_layers/2))
        self.fc3=nn.Linear(int(hidden_layers/2),int(hidden_layers/4))
       # self.fc4=nn.Linear(hidden_layers,hidden_layers)
       # self.fc5=nn.Linear(hidden_layers,hidden_layers)
       # self.fc6=nn.Linear(hidden_layers,hidden_layers)
       # self.fc7=nn.Linear(hidden_layers,hidden_layers)
        self.fc8=nn.Linear(int(hidden_layers/4),n_classes)
        
    def forward(self, x):
        # TODO: compute forward pass
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=F.relu(self.fc3(x))
       # x=F.relu(self.fc4(x))
       # x=F.relu(self.fc5(x))
       # x=F.relu(self.fc6(x))
       # x=F.relu(self.fc7(x))
        x=self.fc8(x)
       # x=F.softmax(x,dim=1)
        return x

class CNN(nn.Module):

    def __init__(self, history_length=0, n_classes=4): 
        super(CNN, self).__init__()
        # TODO : define layers of a convolutional neural network
        self.conv1=nn.Conv2d(1,32,5)
        self.conv2=nn.Conv2d(32,64,5)
        self.conv3=nn.Conv2d(64,128,5)
        self.fc1=nn.Linear(17280,512)
        self.fc2=nn.Linear(512,4)
    
    def forward(self, x):
        # TODO: compute forward pass
        x=F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        x=F.max_pool2d(F.relu(self.conv2(x)),(2,2))
        x=F.max_pool2d(F.relu(self.conv3(x)),(2,2))
        x=x.view(-1,17280)
        x=F.relu(self.fc1(x))
        x=self.fc2(x)
        return x  


#import torch
#print(torch.cuda.is_available())

#import torch
#array = torch.zeros(4)
#print(array)

#import torch
#x = torch.rand(20, 10)
#print(x)

import torch.nn as nn
torch.manual_seed(1)
fc = nn.Linear(3, 2)
print(fc.weight)
print(fc.bias)
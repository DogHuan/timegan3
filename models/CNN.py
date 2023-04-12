


# class CNN_Discriminator(nn.Module):
#     def __init__(self, input_size, num_channels, kernel_size, stride, padding):
#         super(CNN_Discriminator, self).__init__()
#         self.conv1 = nn.Conv1d(in_channels=input_size, out_channels=num_channels, kernel_size=kernel_size, stride=stride, padding=padding)
#         self.conv2 = nn.Conv1d(in_channels=num_channels, out_channels=num_channels*2, kernel_size=kernel_size, stride=stride, padding=padding)
#         self.conv3 = nn.Conv1d(in_channels=num_channels*2, out_channels=num_channels*4, kernel_size=kernel_size, stride=stride, padding=padding)
#         self.pool = nn.MaxPool1d(2)
#         self.fc1 = nn.Linear(num_channels*4, 1)
#
#     def forward(self, x):
#         x = self.pool(torch.relu(self.conv1(x)))
#         x = self.pool(torch.relu(self.conv2(x)))
#         x = self.pool(torch.relu(self.conv3(x)))
#         x = x.view(-1, self.num_flat_features(x))
#         x = torch.sigmoid(self.fc1(x))
#         return x
#
#     def num_flat_features(self, x):
#         size = x.size()[1:]  # all dimensions except the batch dimension
#         num_features = 1
#         for s in size:
#             num_features *= s
#         return num_features

# import torch as nn
from torch import nn
class Dis_CNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(Dis_CNN, self).__init__()

        self.conv1 = nn.Conv1d(input_size, hidden_size, kernel_size=3, stride=2, padding=1)
        self.relu1 = nn.LeakyReLU(0.2)
        self.conv2 = nn.Conv1d(hidden_size, hidden_size * 2, kernel_size=3, stride=2, padding=1)
        self.bn2 = nn.BatchNorm1d(hidden_size * 2)
        self.relu2 = nn.LeakyReLU(0.2)
        self.conv3 = nn.Conv1d(hidden_size * 2, hidden_size * 4, kernel_size=3, stride=2, padding=1)
        self.bn3 = nn.BatchNorm1d(hidden_size * 4)
        self.relu3 = nn.LeakyReLU(0.2)
        self.conv4 = nn.Conv1d(hidden_size * 4, hidden_size * 8, kernel_size=3, stride=2, padding=1)
        self.bn4 = nn.BatchNorm1d(hidden_size * 8)
        self.relu4 = nn.LeakyReLU(0.2)
        self.fc = nn.Linear(hidden_size * 8, output_size)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu2(x)
        x = self.conv3(x)
        x = self.bn3(x)
        x = self.relu3(x)
        x = self.conv4(x)
        x = self.bn4(x)
        x = self.relu4(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x


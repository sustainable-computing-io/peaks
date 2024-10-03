import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import torch
from torch.autograd import Variable

class UtilisationPowerModel:

	# Returns Idle power of a physical machine given that equation for power model is `k0 + k1e^(-k2 * x) + k3 * x`
	def get_idle_power(self, k):
		return k[0].data + k[1].data

	# Returns power using model params using input utilisation.
	def forward(self, x, k0, k1, k2):
		return k0 + k1 * torch.exp(k2 * x)

	# Returns RMSE
	def criterion_rmse(self, y_pred, y):
		return torch.sqrt(torch.mean((y_pred - y) ** 2))

	# Returns MSE
	def criterion_mse(self, y_pred, y):
		return torch.mean((y_pred - y) ** 2)

	# Use this values to initilaise exponential eq params for faster convergence and minima.
	def get_init_values(self, y):
		return max(y)[0], min(y)[0]

	def train(self, x, y, learning_rate, epochs):
		a, b = self.get_init_values(y)
		k0 = torch.tensor(a, requires_grad=True)
		k1 = torch.tensor(-(a-b), requires_grad=True)
		k2 = torch.tensor(-0.005, requires_grad=True)

		loss_l = []

		for epoch in range(epochs):
			inputs = Variable(torch.from_numpy(x))
			labels = Variable(torch.from_numpy(y))

			y_pred = self.forward(inputs,k0,k1,k2)

			loss = self.criterion_mse(y_pred, labels)
			loss.backward()

			k0.data = k0.data - learning_rate * k0.grad.data
			k1.data = k1.data - learning_rate * k1.grad.data
			k2.data = k2.data - learning_rate * k2.grad.data

			k0.grad.data.zero_()
			k1.grad.data.zero_()
			k2.grad.data.zero_()

			if epoch % (epochs // 10) == 0:
				loss_l.append(loss.item())

		with torch.no_grad():
			predicted = self.forward(Variable(torch.from_numpy(x)),k0,k1,k2).data.numpy()
		return predicted, loss_l, (k0, k1, k2)

	def get_model(self, data, learning_rate = 0.00002, epochs = 10000):
		x_values = data['util']
		x_train = np.array(x_values, dtype=np.float32)
		x_train = x_train.reshape(-1, 1)

		y_values = data['power']
		y_train = np.array(y_values, dtype=np.float32)
		y_train = y_train.reshape(-1, 1)

		result = self.train(x_train, y_train, learning_rate, epochs)
		data = data.sort_values("util")
		
		x = [i * 0.01 for i in range(100)]
		x = np.array(x, dtype=np.float32)
		y = self.forward(Variable(torch.from_numpy(x)),result[2][0],result[2][1],result[2][2]).data.numpy()
		
		plt.plot(x,y, '--', label='Predictions', alpha=0.5)
		plt.plot(data['util'],data['power'], 'go', label='True data', alpha=0.5)
		plt.title("Total Utilisation based model")
		plt.legend(['predicted', 'actual'])
		plt.show()

		return result

from typing import List, Tuple
import numpy as np


class Regression(object):

	def __init__(self):
		pass

	def rmse(self, pred: np.ndarray, label: np.ndarray) ->float:
		"""		
		Calculate the root mean square error.
		
		Args:
			pred: (N, 1) numpy array, the predicted labels
			label: (N, 1) numpy array, the ground truth labels
		Return:
			A float value
		"""
		return np.sqrt(np.mean((pred - label) ** 2))

	def construct_polynomial_feats(self, x: np.ndarray, degree: int
		) ->np.ndarray:
		"""		
		Given a feature matrix x, create a new feature matrix
		which is all the possible combinations of polynomials of the features
		up to the provided degree
		
		Args:
			x:
				1-dimensional case: (N,) numpy array
				D-dimensional case: (N, D) numpy array
				Here, N is the number of instances and D is the dimensionality of each instance.
			degree: the max polynomial degree
		Return:
			feat:
				For 1-D array, numpy array of shape Nx(degree+1), remember to include
				the bias term. feat is in the format of:
				[[1.0, x1, x1^2, x1^3, ....,],
				 [1.0, x2, x2^2, x2^3, ....,],
				 ......
				]
		Hints:
			- For D-dimensional array: numpy array of shape N x (degree+1) x D, remember to include
			the bias term.
			- It is acceptable to loop over the degrees.
			- Example:
			For inputs x: (N = 3 x D = 2) and degree: 3,
			feat should be:
		
			[[[ 1.0        1.0]
				[ x_{1,1}    x_{1,2}]
				[ x_{1,1}^2  x_{1,2}^2]
				[ x_{1,1}^3  x_{1,2}^3]]
		
				[[ 1.0        1.0]
				[ x_{2,1}    x_{2,2}]
				[ x_{2,1}^2  x_{2,2}^2]
				[ x_{2,1}^3  x_{2,2}^3]]
		
				[[ 1.0        1.0]
				[ x_{3,1}    x_{3,2}]
				[ x_{3,1}^2  x_{3,2}^2]
				[ x_{3,1}^3  x_{3,2}^3]]]
		"""
		if x.ndim == 1:
			x = x[:, np.newaxis]
		N, D = x.shape
		feature = np.ones((N, degree + 1, D))
		for d in range(1, degree + 1):
			feature[:, d, :] = x ** d

		return feature

	def predict(self, xtest: np.ndarray, weight: np.ndarray) ->np.ndarray:
		"""		
		Using regression weights, predict the values for each data point in the xtest array
		
		Args:
			xtest: (N,1+D) numpy array, where N is the number
					of instances and D is the dimensionality
					of each instance with a bias term
			weight: (1+D,1) numpy array, the weights of linear regression model
		Return:
			prediction: (N,1) numpy array, the predicted labels
		"""
		return xtest @ weight

	def linear_fit_closed(self, xtrain: np.ndarray, ytrain: np.ndarray
		) ->np.ndarray:
		"""		
		Fit a linear regression model using the closed form solution
		
		Args:
			xtrain: (N,1+D) numpy array, where N is number
					of instances and D is the dimensionality
					of each instance with a bias term
			ytrain: (N,1) numpy array, the true labels
		Return:
			weight: (1+D,1) numpy array, the weights of linear regression model
		Hints:
			- For pseudo inverse, you should use the numpy linear algebra function (np.linalg.pinv)
		"""
		return np.linalg.pinv(xtrain) @ ytrain

	def linear_fit_GD(self, xtrain: np.ndarray, ytrain: np.ndarray, epochs:
		int=5, learning_rate: float=0.001) ->Tuple[np.ndarray, List[float]]:
		"""		
		Fit a linear regression model using gradient descent.
		Although there are many valid initializations, to pass the local tests
		initialize the weights with zeros.
		
		Args:
			xtrain: (N,1+D) numpy array, where N is number
					of instances and D is the dimensionality
					of each instance with a bias term
			ytrain: (N,1) numpy array, the true labels
		Return:
			weight: (1+D,1) numpy array, the weights of linear regression model
			loss_per_epoch: (epochs,) list of floats, rmse of each epoch
		Hints:
			- RMSE loss should be recorded AFTER the gradient update in each iteration.
		"""
		N, D = xtrain.shape
		weight = np.zeros((D, 1))
		loss = []
		# Referred to https://towardsdatascience.com/coding-linear-regression-from-scratch-c42ec079902/ for gradient descent part
		for _ in range(epochs):
			prediction = xtrain @ weight
			gradient = (1 / N) * xtrain.T @ (prediction - ytrain)
			weight -= learning_rate * gradient
			pred = xtrain @ weight
			loss.append(self.rmse(pred, ytrain))

		return weight, loss

	def linear_fit_SGD(self, xtrain: np.ndarray, ytrain: np.ndarray, epochs:
		int=100, learning_rate: float=0.001) ->Tuple[np.ndarray, List[float]]:
		"""		
		Fit a linear regression model using stochastic gradient descent.
		Although there are many valid initializations, to pass the local tests
		initialize the weights with zeros.
		
		Args:
			xtrain: (N,1+D) numpy array, where N is number
					of instances and D is the dimensionality of each
					instance with a bias term
			ytrain: (N,1) numpy array, the true labels
			epochs: int, number of epochs
			learning_rate: float
		Return:
			weight: (1+D,1) numpy array, the weights of linear regression model
			loss_per_step: (N*epochs,) list of floats, rmse calculated after each update step
		Hints:
			- RMSE loss should be recorded AFTER the gradient update in each iteration.
			- Keep in mind that the number of epochs is the number of complete passes
			through the training dataset. SGD updates the weight for one datapoint at
			a time. For each epoch, you'll need to go through all of the points.
		
		NOTE: For autograder purposes, iterate through the dataset SEQUENTIALLY, NOT stochastically.
		"""
		N, D = xtrain.shape
		weight = np.zeros((D, 1))
		loss = []
		# Referred to https://medium.com/@nikhilparmar9/simple-sgd-implementation-in-python-for-linear-regression-on-boston-housing-data-f63fcaaecfb1
		# for SGD steps
		for _ in range(epochs):
			for i in range(N):
				x_i = xtrain[i : i + 1]
				y_i = ytrain[i: i + 1]
				prediction = x_i @ weight
				gradient = x_i.T @ (prediction - y_i)
				weight -= learning_rate * gradient
				pred = xtrain @ weight
				loss.append(self.rmse(pred, ytrain))
		
		return weight, loss

	def ridge_fit_closed(self, xtrain: np.ndarray, ytrain: np.ndarray,
		c_lambda: float) ->np.ndarray:
		"""		
		Fit a ridge regression model using the closed form solution
		
		Args:
			xtrain: (N,1+D) numpy array, where N is
					number of instances and D is the dimensionality
					of each instance with a bias term
			ytrain: (N,1) numpy array, the true labels
			c_lambda: float value, value of regularization constant
		Return:
			weight: (1+D,1) numpy array, the weights of ridge regression model
		Hints:
			- You should adjust your I matrix to handle the bias term differently than the rest of the terms
		"""
		D = xtrain.shape[1]
		I = np.eye(D)
		I[0, 0] = 0
		reg = c_lambda * I
		
		return np.linalg.pinv(xtrain.T @ xtrain + reg) @ xtrain.T @ ytrain

	def ridge_fit_GD(self, xtrain: np.ndarray, ytrain: np.ndarray, c_lambda:
		float, epochs: int=500, learning_rate: float=1e-07) ->Tuple[np.
		ndarray, List[float]]:
		"""		
		Fit a ridge regression model using gradient descent.
		Although there are many valid initializations, to pass the local tests
		initialize the weights with zeros.
		
		Args:
			xtrain: (N,1+D) numpy array, where N is number
					of instances and D is the dimensionality of each
					instance with a bias term
			ytrain: (N,1) numpy array, the true labels
			c_lambda: float value, value of regularization constant
			epochs: int, number of epochs
			learning_rate: float
		Return:
			weight: (1+D,1) numpy array, the weights of linear regression model
			loss_per_epoch: (epochs,) list of floats, rmse of each epoch
		Hints:
			- RMSE loss should be recorded AFTER the gradient update in each iteration.
			- You should avoid applying regularization to the bias term in the gradient update
		"""
		N, D = xtrain.shape
		weight = np.zeros((D, 1))
		loss = []
		for _ in range(epochs):
			prediction = xtrain @ weight
			gradient = (1 / N) * xtrain.T @ (prediction - ytrain)
			reg = (c_lambda / N) * weight
			reg[0] = 0
			gradient += reg
			weight -= learning_rate * gradient
			pred = xtrain @ weight
			loss.append(self.rmse(pred, ytrain))
		
		return weight, loss

	def ridge_fit_SGD(self, xtrain: np.ndarray, ytrain: np.ndarray,
		c_lambda: float, epochs: int=100, learning_rate: float=0.001) ->Tuple[
		np.ndarray, List[float]]:
		"""		
		Fit a ridge regression model using stochastic gradient descent.
		Although there are many valid initializations, to pass the local tests
		initialize the weights with zeros.
		
		Args:
			xtrain: (N,1+D) numpy array, where N is number
					of instances and D is the dimensionality of each
					instance with a bias term
			ytrain: (N,1) numpy array, the true labels
			c_lambda: float, value of regularization constant
			epochs: int, number of epochs
			learning_rate: float
		Return:
			weight: (1+D,1) numpy array, the weights of linear regression model
			loss_per_step: (N*epochs,) list of floats, rmse calculated after each update step
		Hints:
			- RMSE loss should be recorded AFTER the gradient update in each iteration.
			- Keep in mind that the number of epochs is the number of complete passes
			through the training dataset. SGD updates the weight for one datapoint at
			a time. For each epoch, you'll need to go through all of the points.
			- You should avoid applying regularization to the bias term in the gradient update
		
		NOTE: For autograder purposes, iterate through the dataset SEQUENTIALLY, NOT stochastically.
		"""
		N, D = xtrain.shape
		weight = np.zeros((D, 1))
		loss = []
		for _ in range(epochs):
			for i in range(N):
				x_i = xtrain[i : i + 1]
				y_i = xtrain[i : i + 1]
				prediction = x_i @ weight
				error = prediction - y_i
				gradient = x_i.T @ error
				reg = (c_lambda / N) * weight
				reg[0] = 0
				gradient += reg
				weight -= learning_rate * gradient
				pred = xtrain @ weight
				loss.append(self.rmse(pred, ytrain))
		
		return weight, loss

	def ridge_cross_validation(self, X: np.ndarray, y: np.ndarray, kfold:
		int=5, c_lambda: float=100) ->List[float]:
		"""		
		For each of the k-folds of the provided X, y data, fit a ridge regression model
		and then evaluate the RMSE. Return the RMSE for each fold
		
		Args:
			X : (N,1+D) numpy array, where N is the number of instances
				and D is the dimensionality of each instance with a bias term
			y : (N,1) numpy array, true labels
			kfold: int, number of folds you should take while implementing cross validation.
			c_lambda: float, value of regularization constant
		Returns:
			loss_per_fold: list[float], RMSE loss for each kfold
		Hints:
			- np.concatenate might be helpful.
			- Use ridge_fit_closed for this function.
			- Look at 3.5 to see how this function is being used.
			- For kfold=5:
				split X and y into 5 equal-size folds
				use 80 percent for training and 20 percent for test
		"""
		N = X.shape[0]
		fold_size = N // kfold
		loss = []
		for i in range(kfold):
			start = i * fold_size
			end = (i + 1) * fold_size
			x_test = X[start : end]
			y_test = y[start : end]
			x_train = np.concatenate((X[:start], X[end:]), axis=0)
			y_train = np.concatenate((y[:start], y[end:]), axis=0)
			weight = self.ridge_fit_closed(x_train, y_train, c_lambda)
			pred = self.predict(x_test, weight)
			loss.append(self.rmse(pred, y_test))

		return loss

	def hyperparameter_search(self, X: np.ndarray, y: np.ndarray,
		lambda_list: List[float], kfold: int) ->Tuple[float, float, List[float]
		]:
		"""
		FUNCTION PROVIDED TO STUDENTS

		Search over the given list of possible lambda values lambda_list
		for the one that gives the minimum average error from cross-validation

		Args:
			X : (N, 1+D) numpy array, where N is the number of instances and
				D is the dimensionality of each instance with a bias term
			y : (N,1) numpy array, true labels
			lambda_list: list of regularization constants (lambdas) to search from
			kfold: int, Number of folds you should take while implementing cross validation.
		Returns:
			best_lambda: (float) the best value for the regularization const giving the least RMSE error
			best_error: (float) the average RMSE error achieved using the best_lambda
			error_list: list[float] list of average RMSE loss for each lambda value given in lambda_list
		"""
		best_error = None
		best_lambda = None
		error_list = []
		for lm in lambda_list:
			err = self.ridge_cross_validation(X, y, kfold, lm)
			mean_err = np.mean(err)
			error_list.append(mean_err)
			if best_error is None or mean_err < best_error:
				best_error = mean_err
				best_lambda = lm
		return best_lambda, best_error, error_list

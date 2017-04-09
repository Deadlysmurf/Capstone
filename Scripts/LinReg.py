#inputs required: X_train, Y_Train, X_test

# Linear Regression

linreg = LinearRegression()
linreg.fit(X_train, Y_train)
Y_pred = linreg.predict(X_test)

print("Explained Variance: %.2f"
    %explained_variance_score(Y_test, Y_pred))

print("r^2: %.2f"
    %r2_score(Y_test, Y_pred))

print("Mean squared error: %.2f"
      % np.mean((linreg.predict(X_test) - Y_test) ** 2))
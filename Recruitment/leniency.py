import numpy as np
import pandas as pd
import statsmodels.api as sm
import math
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.graphics.regressionplots import abline_plot

# to count the amount of words in each answer
def wordcount(dataframe):
    # going down each of the rows for the text column
    for i, row_value in dataframe.iloc[:, [2]].iterrows():
        row_value = row_value.astype(str)
        # getting the specific text of note in the row value
        for text in row_value:
            # initialize word to be equals to 1 because using isspace
            words = 1
            # now getting each letter of the text
            for k in text:
                # now checking for each of the space
                if k.isspace() == True:
                    words = words + 1
        # ending the loop
        dataframe.iloc[i, [5]] = words


# to change the scores from 0 to 1
def cleanscores(dataframe):
    # going down each of the rows in the dataframe
    for i, row_value in dataframe.iterrows():
        # change all values that are 0 to 1
        if row_value[3] == 0:
            dataframe.iloc[i, [3]] = 1
        if row_value[4] == 0:
            dataframe.iloc[i, [4]] = 1


# to get the log of the word count
def logcount(dataframe):
    # now figure out the logarithmic count of the word count
    dataframe['LogCount'] = np.nan
    dataframe['LogCount'] = np.log(dataframe['WordCount'])


# to get a linear regression plot of the question dataset
def regressquestion(dataframe):
    # import the linear regression library from sklearn
    from sklearn.linear_model import LinearRegression
    # now create an instance of the class LinearRegression
    model = LinearRegression(fit_intercept = True)
    # now call fit in the model to calculate the optimal weights
    X = dataframe['LogCount'].values.reshape(-1, 1)
    Y = dataframe['AssessorScore'].values.reshape(-1, 1)
    model.fit(X, Y)
    # now create the line of best fit through the predictions
    Y_pred = model.predict(X)
    
    # now plot the data points
    plt.scatter(X, Y, label = "Data Point")
    # now plot the regression line
    plt.plot(X, Y_pred, color = "red", label = "Linear Regression")
    # give the relevant labels
    plt.suptitle('testing for scores based on word counts', fontsize=20)
    plt.xlabel("log(word counts)")
    plt.ylabel("assessor scores")
    # show the graph
    plt.legend()
    plt.show()


# to get the standard error variable
def regressionstats(X, Y):
    import statsmodels.api as sm
    # find the relevant statistics
    X_ = sm.add_constant(X)
    olsmodel = sm.OLS(Y, X_)
    olsmodel = olsmodel.fit()
    print(olsmodel.summary())


# to get the predicted scores:
def predictedscore(dataframe, slope, intercept):
    # now include a column for predicted scores, and calculate predicted scores
    dataframe['LogCount'] = np.nan
    dataframe['PredictedScore'] = np.nan
    # create a formula to calculate for the predicted score for each column
    dataframe['LogCount'] = np.log(dataframe['WordCount'])
    dataframe['PredictedScore'] = intercept + (slope * dataframe['LogCount'])


# to get weighted scores:
def weightedscore(dataframe):
    # create a list for weighted prediction scores
    weighted_score = []
    # use average score * predicted score to provide a weighted prediction
    for i, row_value in dataframe.iterrows():
        # average score * predicted score divided by 5 to provide a weighted prediction score
        weight = (row_value[6] * row_value[4]) / 5
        # to reduce flagging out wrong strict / leniency because some scores after division may fall below 1
        if weight < 1:
            weighted_score.append(1)
        else:
            weighted_score.append(weight)
    # insert weighted score into the dataframe
    dataframe.insert(7, 'WeightedPrediction', weighted_score)


# to get the weighted predicted score that punishes bad scores less:
def adjustedscore(dataframe):
    # create a list for weighted prediction scores
    weighted_score = []
    # use average score * predicted score to provide a weighted prediction score
    for i, row_value in dataframe.iterrows():
        weightpt = math.sqrt(row_value[4])
        weightpt = weightpt / (math.sqrt(5))
        weight = (row_value[6] * weightpt)
        # to reduce flagging out wrong strict / leniency because some scores after division may fall below 1
        if weight < 1:
            weighted_score.append(1)
        else:
            weighted_score.append(weight)
    # now create a new column right behind the predicted scoers
    dataframe.insert(8, 'AdjWeightedPrediction', weighted_score)

# to get the standard errors of the assessor from the mean
def assessordeviation(dataframe, stderr):
    # now calculating the standard error from the individual assessor
    dataframe["SD_individual"] = (dataframe['AssessorScore'] - dataframe['WeightedPrediction']) / stderr
    # and now calcualting the standard error from the average score 
    dataframe["SD_average"] = (dataframe['AverageScore'] - dataframe['WeightedPrediction']) / stderr
    # now calculating the standard error from the individual assessor
    dataframe["AdjSD_individual"] = (dataframe['AssessorScore'] - dataframe['AdjWeightedPrediction']) / stderr
    # and now calcualting the standard error from the average score 
    dataframe["AdjSD_average"] = (dataframe['AverageScore'] - dataframe['AdjWeightedPrediction']) / stderr


# create a namelist to keep everyone's name
def namedict(dataframe):
    # create a list to keep everyone's name
    name_list = []
    assessor_list = dataframe['Assessor'].tolist()
    # now append names from the table into the name list
    for x in assessor_list:
        if x in name_list:
            continue
    # append the name to the list
        else:
            name_list.append(x)
    # create a dictionary now to store all the keys
    namelist = dict.fromkeys(name_list)

    # use the name list as a loop to check when looping through the question one table
    for i in namelist:
        # initialize a count for the name so that you can do division later
        count = 0
        sumvalue = 0
        # now use this loop to check the table name and the namelist if it matches
        for j, row_value in dataframe.iterrows():
            # now if the name equals the name in the table
            if i == row_value[0]:
                # add to the sum values and the count values
                sumvalue = sumvalue + row_value['AdjSD_individual']
                count = count + 1
        # calculate final deviation through sum / count and add it to the dictionary
        deviation = sumvalue / count
        namelist[i] = deviation
    
    # return the dictionary of the names and the standard deviations
    return namelist
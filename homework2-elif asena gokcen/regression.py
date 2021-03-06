
import numpy as np
import pandas as pd

def reg(x,y):
    betas = est_coeff(x,y)
    sd = beta_sd(x,y)
    confidence_intervals = conf_interval(x,y)
    variable_list = listwise_deletion(x,y)
    x = variable_list[0]
    print("n = " + str(len(x)))
    return  pd.concat([betas,sd,confidence_intervals], axis=1)  


def listwise_deletion(x,y):
    #listwise deletion 
    x = np.array(x).transpose()
    y = np.array(y).transpose()
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)    
    z = pd.concat([x,y], axis=1)    
    z = z.dropna()
    
    #Creating matrix for variables 
    x = np.array(z.iloc[:,:-1])
    n = len(x)
    y = np.array(z.iloc[:,-1]).reshape(n,1)        
    ax = np.ones(n).reshape(n,1) #initialize matrix with 1s for intercept
    x = np.concatenate([ax,x], axis=1) #create x matrix
    return x, y

def est_coeff(x,y):            
    variable_list = listwise_deletion(x,y)
    x = variable_list[0]
    y = variable_list[1]
    
    #Estimation of betas
    first_part = np.linalg.inv(x.transpose()@x)
    second_part = first_part@x.transpose()
    betas = second_part@y
    
    #create beta list
    beta_list = []
    for i in betas:
        beta_list.append(float(i))
    
    return pd.DataFrame(beta_list, columns = ["Coefficients"])

def y_estimator(x,y):
    betas = est_coeff(x,y)
    betas = np.array(betas)
    variable_list = listwise_deletion(x,y)
    x = variable_list[0]
    return x@betas

def error_calc(x,y):
    y_estimates = y_estimator(x,y)
    variable_list = listwise_deletion(x,y)
    y = variable_list[1]
    return y - y_estimates

def variance(x,y):
    error = error_calc(x,y)
    variable_list = listwise_deletion(x,y)
    x = variable_list[0]
    y = variable_list[1]
    n = x.shape[0]
    k = x.shape[1] - 1
    return (error.transpose()@error)/(n-k-1)

def beta_sd(x,y):
    var = variance(x,y)
    variable_list = listwise_deletion(x,y)
    x = variable_list[0]
    y = variable_list[1]  
    variances = var*(np.linalg.inv(x.transpose()@x))
    k = x.shape[1]
    
    #extract variances
    var_list = []
    for i in range(k):
        var_list.append(variances[i,i])
    
    var_list = np.array(var_list)
    sd_list = np.sqrt(var_list)    
    return pd.DataFrame(sd_list, columns = ["Standard Errors"])

def conf_interval(x,y):
    betas = est_coeff(x,y)
    betas = np.array(betas)
    sd = beta_sd(x,y)
    sd = np.array(sd)
    
    #Z distribution was used to estimate confidence intervals
    lower_tails = []
    for i,k in zip(sd,betas):
        lower_tails.append(k - (1.96*i))
    
    upper_tails = []
    for i,k in zip(sd,betas):
        upper_tails.append(k + (1.96*i))    

    a = pd.DataFrame(lower_tails, columns = ["Lower 95%"])
    b = pd.DataFrame(upper_tails, columns = ["Upper 95%"])
    return pd.concat([a,b], axis=1)

    
    
        
    
    
    
    
    
    



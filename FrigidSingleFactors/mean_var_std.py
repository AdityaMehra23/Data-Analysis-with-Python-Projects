import numpy as np

def calculate(list):
  calculations={}
  
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  else:  
    data_flat = np.array(list)
    data=data_flat.reshape(3,3)
    cont=[]
    #mean of the array
    cont.append(np.mean(data,axis=0).tolist())
    cont.append(np.mean(data,axis=1).tolist())
    cont.append(np.mean(data_flat))
    calculations['mean']=cont[:]
    cont.clear()
    #variance of  the array
    cont.append(np.var(data,axis=0).tolist())
    cont.append(np.var(data,axis=1).tolist())
    cont.append(np.var(data_flat))
    calculations['variance']=cont[:]
    cont.clear()
    #standard deviation of  the array
    cont.append(np.std(data,axis=0).tolist())
    cont.append(np.std(data,axis=1).tolist())
    cont.append(np.std(data_flat))
    calculations['standard deviation']=cont[:]
    cont.clear()
    #max of  the array
    cont.append(np.max(data,axis=0).tolist())
    cont.append(np.max(data,axis=1).tolist())
    cont.append(np.max(data_flat))
    calculations['max']=cont[:]
    cont.clear()
    #min of  the array
    cont.append(np.min(data,axis=0).tolist())
    cont.append(np.min(data,axis=1).tolist())
    cont.append(np.min(data_flat))
    calculations['min']=cont[:]
    cont.clear()
    #sum of  the array
    cont.append(np.sum(data,axis=0).tolist())
    cont.append(np.sum(data,axis=1).tolist())
    cont.append(np.sum(data_flat))
    calculations['sum']=cont[:]
    
  return calculations
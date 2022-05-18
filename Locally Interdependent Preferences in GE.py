#!/usr/bin/env python
# coding: utf-8

# ### Simulation Project: Microeconomic Theory
# ### Paper: Locally Interdependent Preferences in a General Equilibrium Environment (Ann Bell, 2002)
# #### Find the paper here: https://doi.org/10.1016/S0167-2681(01)00177-9

# We replicate Bell's model for three production technologies - 1. Exchange Economy, 2. Constant Returns to Scale Economy, 3. Decreasing Returns to Scale Economy.
# The neighbourhood definition is changed - an agent's neighbourhood consists of those who immediately surround him. This means individual at [0,0] has three neighbours, the individual at [0,1] has 5, while the individual at [1,1] has eight.
# 

# In[19]:


#load required packages
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from scipy.ndimage import convolve


# In[20]:


#turn off scientific notation
np.set_printoptions(suppress=True)


# In[21]:


#specify kernel for scipy convolve
kernel = [[1,1,1],
          [1,0,1],
         [1,1,1]] 


# In[4]:


#update function - this is the same for all production technologies
def update(r,price_ratio,ai):
        ai_next_time_period = ai+(r*((convolve(ai, kernel,mode='constant'))/((convolve(ai, kernel,mode='constant'))+(price_ratio*(convolve(1-initial_ai, kernel,mode='constant'))))-0.5))
        ai_next_time_period[ai_next_time_period<0]=0
        ai_next_time_period[ai_next_time_period>1]=1
        return(ai_next_time_period)


# #### Exchange Economy, e1=e2=1, r=0.5

# In[5]:


np.random.seed(121) #set seed so we can use the same initial preference distribution for all production technologies
initial_ai=np.random.rand(50,50) #a randomly drawn initial distribution of preferences for population(N)=2500
np.average(initial_ai) #this has mean 0.498


# In[6]:


#for an exchange economy, specifying endowments and r which is speed of update

e1 = 1 #change e1,e2,r as required
e2 = 1
r = 0.5

# defining the price ratio formula for an exchange economy 

def price_ratio(e1,e2,ai):
    priceratio=(e2*np.sum(ai))/(e1*np.sum(1-ai))
    return(priceratio)

initial_price_ratio=price_ratio(e1,e2,initial_ai)
initial_price_ratio

#the initial price ratio is 0.9933 with e1=e2=1


# In[7]:


#simulation 

iterations=250 #change iterations as required
data_preferences=np.zeros(iterations)
data_price_ratio=np.zeros(iterations)
time=np.zeros(iterations)
array=[[] for i in range(iterations)]


for t in range(0,iterations):
    new_ai = update(0.5,initial_price_ratio,initial_ai)
    new_price_ratio=price_ratio(e1,e2,new_ai)
    time[t]=t
    data_price_ratio[t]=new_price_ratio
    data_preferences[t]=np.average(new_ai)
    initial_price_ratio=new_price_ratio
    initial_ai=new_ai
    array[t] = new_ai
    print(new_ai)


# In[8]:


#PLOT: Exchange Economy Evolution of Avg Preferences and Price Ratio 

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,6))
ax1.plot(time,data_preferences)
ax2.plot(time,data_price_ratio)
fig.suptitle("Evolution of Average Preferences and Price Ratio for an Exchange Economy",fontsize=15)
ax1.title.set_text('Evolution of Average Preferences')
ax1.set_ylim(0.40,0.6)
ax1.set_xlim(0,250)
ax2.title.set_text('Evolution of Price Ratio')
ax2.set_ylim(0.8,1.2)
ax2.set_xlim(0,250)
plt.show()


# In[9]:


#final heatmap Exchange Economy 

fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(12,10))
sns.heatmap(array[0],cmap="flare_r",ax=ax1)
sns.heatmap(array[10],cmap="flare_r",ax=ax2)
sns.heatmap(array[100],cmap="flare_r",ax=ax3)
sns.heatmap(array[249],cmap="flare_r",ax=ax4)
fig.suptitle("Evolution of Preferences for an Exchange Economy",fontsize=15)
ax1.title.set_text('Time=1')
ax2.title.set_text('Time=10')
ax3.title.set_text('Time=100')
ax4.title.set_text('Time=250')
plt.show()


# ### Constant Returns to Scale

# In[10]:


#initialize initial distribution of preferences again
np.random.seed(121) 
initial_ai=np.random.rand(50,50) 
np.average(initial_ai)


# In[11]:


iterations=22
CRS_price_ratio=np.zeros(iterations)
CRS_preferences=np.zeros(iterations)
time=np.zeros(iterations)
array=[[] for i in range(iterations)]
for t in range(0,iterations):
    price_ratio=0.5
    new_ai = update(0.5,price_ratio,initial_ai)
    time[t]=t
    CRS_preferences[t]=np.average(new_ai)
    CRS_price_ratio[t]=price_ratio
    initial_ai=new_ai
    array[t]=new_ai
    print(new_ai)


# In[12]:


#PLOT: CRS Evolution of Avg Preferences and Price Ratio 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,6))
ax1.plot(time,CRS_preferences)
ax2.plot(time,CRS_price_ratio)
fig.suptitle("Evolution of Average Preferences and Price Ratio for a Constant Returns to Scale Economy",fontsize=15)
ax1.title.set_text('Evolution of Average Preferences')
ax1.set_ylim(0.40,1.2)
ax1.set_xlim(0,20)
ax2.title.set_text('Evolution of Average Price Ratio')
ax2.set_ylim(0.4,0.6)
ax2.set_xlim(0,20)
plt.show()


# In[13]:


#final heatmap CRS

fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(12,10))
sns.heatmap(array[1],cmap="flare_r",ax=ax1)
sns.heatmap(array[5],cmap="flare_r",ax=ax2)
sns.heatmap(array[10],cmap="flare_r",ax=ax3)
sns.heatmap(array[19],cmap="flare_r",ax=ax4)
fig.suptitle("Evolution of Preferences for a Constant Returns to Scale Economy",fontsize=15)
ax1.title.set_text('Time=1')
ax2.title.set_text('Time=5')
ax3.title.set_text('Time=10')
ax4.title.set_text('Time=19')
plt.show()


# ### Decreasing Returns to Scale

# In[14]:


#initialize initial distribution of preferences again
np.random.seed(121) 
initial_ai=np.random.rand(50,50) 
np.average(initial_ai) 


# In[15]:


r = 0.5

def price_ratio(ai):
    priceratio=((np.sum(ai))/(np.sum(1-ai)))**0.5
    return(priceratio)

initial_price_ratio=price_ratio(initial_ai)
initial_price_ratio #initial price ratio is 0.996


# In[16]:


iterations=250
DRS_price_ratio=np.zeros(iterations)
DRS_preferences=np.zeros(iterations)
time=np.zeros(iterations)
array=[[] for i in range(iterations)]
for t in range(0,iterations):
    new_ai = update(0.5,initial_price_ratio,initial_ai)
    new_price_ratio=price_ratio(new_ai)
    time[t]=t
    DRS_preferences[t]=np.average(new_ai)
    DRS_price_ratio[t]=new_price_ratio
    initial_price_ratio=new_price_ratio
    initial_ai=new_ai
    array[t]=new_ai
    print(new_ai)


# In[17]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,6))
ax1.plot(time,DRS_preferences)
ax2.plot(time,DRS_price_ratio)
fig.suptitle("Evolution of Average Preferences and Price for a Decreasing Returns to Scale Economy",fontsize=15)
ax1.title.set_text('Evolution of Average Preferences')
ax1.set_ylim(0.40,0.60)
ax1.set_xlim(0,250)
ax2.title.set_text('Evolution of Average Price Ratio')
ax2.set_ylim(0.8,1.2)
ax2.set_xlim(0,250)
plt.show()


# In[18]:


#final heatmap DRS

fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(12,10))
sns.heatmap(array[1],cmap="flare_r",ax=ax1)
sns.heatmap(array[10],cmap="flare_r",ax=ax2)
sns.heatmap(array[100],cmap="flare_r",ax=ax3)
sns.heatmap(array[249],cmap="flare_r",ax=ax4)
fig.suptitle("Evolution of Preferences for a Decreasing Returns to Scale Economy",fontsize=15)
ax1.title.set_text('Time=1')
ax2.title.set_text('Time=10')
ax3.title.set_text('Time=100')
ax4.title.set_text('Time=249')
plt.show()


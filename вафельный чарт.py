#!/usr/bin/env python
# coding: utf-8

# In[71]:


get_ipython().run_cell_magic('time', '', "\nimport numpy as np  # useful for many scientific computing in Python\nimport pandas as pd # primary data structure library\nfrom PIL import Image # converting images into arrays\n\ndf_can = pd.read_excel('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',\n                       sheet_name='Canada by Citizenship',\n                       skiprows=range(20),\n                       skipfooter=2)\n\nprint('Data downloaded and read into a dataframe!')\n\n# clean up the dataset to remove unnecessary columns (eg. REG) \ndf_can.drop(['AREA','REG','DEV','Type','Coverage'], axis = 1, inplace = True)\n\n# let's rename the columns so that they make sense\ndf_can.rename (columns = {'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace = True)\n\n# for sake of consistency, let's also make all column labels of type string\ndf_can.columns = list(map(str, df_can.columns))\n\n# set the country name as index - useful for quickly looking up countries using .loc method\ndf_can.set_index('Country', inplace = True)\n\n# add total column\ndf_can['Total'] =  df_can.sum (axis = 1)\n\n# years that we will be using in this lesson - useful for plotting later on\nyears = list(map(str, range(1980, 2014)))\nprint ('data dimensions:', df_can.shape)\n\n%matplotlib inline\n\nimport matplotlib as mpl\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches # needed for waffle Charts\n\nmpl.style.use('ggplot') # optional: for ggplot-like style\n\n# check for latest version of Matplotlib\nprint ('Matplotlib version: ', mpl.__version__) # >= 2.0.0\n\n# select what is to be plotted\ndf_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]\n\n\n# compute the proportion of each category with respect to the total\ntotal_values = sum(df_dsn['Total'])\ncategory_proportions = [(float(value) / total_values) for value in df_dsn['Total']]\n\n# print out proportions\nfor i, proportion in enumerate(category_proportions):\n    print (df_dsn.index.values[i] + ': ' + str(proportion))\n    \nwidth = 40 # width of chart\nheight = 10 # height of chart\n\ntotal_num_tiles = width * height # total number of tiles\n\nprint ('Total number of tiles is ', total_num_tiles)\n\n# compute the number of tiles for each catagory\ntiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]\n\n# print out number of tiles per category\nfor i, tiles in enumerate(tiles_per_category):\n    print (df_dsn.index.values[i] + ': ' + str(tiles))\n    \n# initialize the waffle chart as an empty matrix\nwaffle_chart = np.zeros((height, width))\n\n# define indices to loop through waffle chart\ncategory_index = 0\ntile_index = 0\n\n# populate the waffle chart\nfor col in range(width):\n    for row in range(height):\n        tile_index += 1\n\n        # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...\n        if tile_index > sum(tiles_per_category[0:category_index]):\n            # ...proceed to the next category\n            category_index += 1       \n            \n        # set the class value to an integer, which increases with class\n        waffle_chart[row, col] = category_index\n        \nprint ('Waffle chart populated!')\n\n\n# instantiate a new figure object\nfig = plt.figure()\n\n# use matshow to display the waffle chart\ncolormap = plt.cm.coolwarm\nplt.matshow(waffle_chart, cmap=colormap)\nplt.colorbar()")


# In[2]:


sbor = pd.read_excel(r"C:\Users\popov.v\Downloads\Копия План продаж 01 12 2020.xlsx", skiprows=9,  sheet_name = 'Сборы',encoding='UTF-8')
df_x = sbor.set_index('Поставщик фин продукта')[sbor.set_index('Поставщик фин продукта')['Тип фин продукта'] == 'КАСКО']
df_x = df_x.groupby(df_x.index).sum()


# In[3]:


#def waffle_maker(df, x, y, legend)


# compute the proportion of each category with respect to the total
total_values = sum(df_x['Сумма фин продукта'])
category_proportions = [(float(value) / total_values) for value in df_x['Сумма фин продукта']]

# print out proportions
for i, proportion in enumerate(category_proportions):
    print (df_x.index.values[i] + ': ' + str(proportion))
    
width = 40 # width of chart
height = 15 # height of chart

total_num_tiles = width * height # total number of tiles

print ('Total number of tiles is ', total_num_tiles)

# compute the number of tiles for each catagory
tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]

# print out number of tiles per category
for i, tiles in enumerate(tiles_per_category):
    print (df_x.index.values[i] + ': ' + str(tiles))
    
# initialize the waffle chart as an empty matrix
waffle_chart = np.zeros((height, width))

# define indices to loop through waffle chart
category_index = 0
tile_index = 0

# populate the waffle chart
for col in range(width):
    for row in range(height):
        tile_index += 1

        # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
        if tile_index > sum(tiles_per_category[0:category_index]):
            # ...proceed to the next category
            category_index += 1       
            
        # set the class value to an integer, which increases with class
        waffle_chart[row, col] = category_index
        
print ('Waffle chart populated!')


# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
# add gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])


# instantiate a new figure object
fig = plt.figure()

# use matshow to display the waffle chart
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
# add gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])

# compute cumulative sum of individual categories to match color schemes between chart and legend
values_cumsum = np.cumsum(df_x['Сумма фин продукта'])
total_values = values_cumsum[len(values_cumsum) - 1]

# create legend
legend_handles = []
for i, category in enumerate(df_x.index.values):
    label_str = category + ' (' + str(df_x['Сумма фин продукта'][i]) + ')'
    color_val = colormap(float(values_cumsum[i])/total_values)
    legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

# add legend to chart
plt.legend(handles=legend_handles,
           loc='lower center', 
           ncol=3,
           bbox_to_anchor=(0., -0.5, 0.95, .1),
           fontsize = 'medium'
          )


# In[108]:


def waffle_maker(df_x, x, y, legend):


    # compute the proportion of each category with respect to the total
    total_values = sum(df_x[df_x.columns[0]])
    category_proportions = [(float(value) / total_values) for value in df_x[df_x.columns[0]]]

    
    
    width = x # width of chart
    height = y # height of chart

    total_num_tiles = width * height # total number of tiles

    #print ('Total number of tiles is ', total_num_tiles)

    # compute the number of tiles for each catagory
    tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]

   
    
    # initialize the waffle chart as an empty matrix
    waffle_chart = np.zeros((height, width))

    # define indices to loop through waffle chart
    category_index = 0
    tile_index = 0

    # populate the waffle chart
    for col in range(width):
        for row in range(height):
            tile_index += 1

            # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
            if tile_index > sum(tiles_per_category[0:category_index]):
                # ...proceed to the next category
                category_index += 1       
            
            # set the class value to an integer, which increases with class
            waffle_chart[row, col] = category_index
        
    #print ('Waffle chart populated!')


    # instantiate a new figure object
    fig = plt.figure()

    # use matshow to display the waffle chart
    colormap = plt.cm.coolwarm
    plt.matshow(waffle_chart, cmap=colormap)
    plt.colorbar()

    # get the axis
    ax = plt.gca()

    # set minor ticks
    ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
    ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
    
    # add gridlines based on minor ticks
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

    plt.xticks([])
    plt.yticks([])

    # compute cumulative sum of individual categories to match color schemes between chart and legend
    values_cumsum = np.cumsum(df_x[df_x.columns[0]])
    total_values = values_cumsum[len(values_cumsum) - 1]

    # create legend
    legend_handles = []
    for i, category in enumerate(df_x.index.values):
        label_str = category + ' (' + str(df_x[df_x.columns[0]][i]) + ')'
        color_val = colormap(float(values_cumsum[i])/total_values)
        legend_handles.append(mpatches.Patch(color=color_val, label=label_str))
    

    
    if str(legend) == 'True':
        # add legend to chart
        plt.legend(handles=legend_handles,
                   loc='upper left', 
                   ncol=1,
                   bbox_to_anchor=(0., -0.5, 0.95, .1),
                   fontsize = 'medium'
                  )

        
waffle_maker(df_z, 20, 20, True)


# In[39]:


import pandas as pd
from scipy import stats
buyback = pd.read_excel(r"C:\Users\popov.v\Downloads\прикидка по менеджерам.xlsx", skiprows=3, sheet_name= 'Лист1', encoding='UTF-8')
buyback['Вознаграждение с выкупа'] = buyback['Profit с возмещением и услугами ИТОГО']*0.02 + buyback['Кол-во продаж']*2000
buyback.drop(buyback.head(1).index,inplace=True)
buyback
#.groupby(['Месяц', 'Менеджер приведший клиента на выкуп']).sum()
sales= pd.read_excel(r"C:\Users\popov.v\Downloads\прикидка по менеджерам.xlsx", skiprows=5, sheet_name= 'Лист6', encoding='UTF-8')
sales.columns = (['Департамент продаж', 'Год', 'Месяц', 'Продавец', 'БУ', 'Корп продажа', 'Новый а/м розница',
       'БУ штуки', 'Корп продажа.1', 'Новые штуки'])
sales['Вознаграждение с продаж'] = sales['БУ']*0.04+sales['Новый а/м розница']*0.06+sales['БУ штуки']*2000+sales['Новые штуки']*2000
sales = sales[['Департамент продаж', 'Месяц', 'Продавец', 'Вознаграждение с продаж']]
buyback = buyback[['Департамент продаж', 'Месяц', 'Менеджер приведший клиента на выкуп', 'Вознаграждение с выкупа']]
buyback.columns = (['Департамент продаж', 'Месяц', 'Продавец', 'Вознаграждение с выкупа'])
df = pd.merge(sales, buyback, on=['Департамент продаж', "Продавец", 'Месяц'])
df.fillna(0, inplace=True)
df['Вознаграждение'] = df['Вознаграждение с продаж']+df['Вознаграждение с выкупа']
df['Вознаграждение'].plot.kde()
df.set_index(['Департамент продаж', 'Месяц'])

df_z = buyback.groupby(['Департамент продаж']).sum()
df_x.columns[0]


# In[88]:



waffle_maker(pd.DataFrame(df_dsn.Total), 20, 20, True)


#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup

setup(
    name='WaterQualityAssessor',
    version='0.0.2',
    author='Megan Maccagnan',
    author_email='meganmaccagnan@mines.edu',
    packages=['WaterQualityAssessor'],
    license='LICENSE.txt',
    url='http://pypi.python.org/pypi/WaterQualityAssessor/',
    description='Assess the toxicity levels of various trace metals according to EPA MCL standards in post-wildfire habitat watersheds',
    long_description=open('README.txt').read(),
    install_requires=['pandas','matplotlib','numpy', 'seaborn', 'math'],
    )


# In[ ]:





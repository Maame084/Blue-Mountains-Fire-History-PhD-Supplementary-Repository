#!/usr/bin/env python
# coding: utf-8

# In[1]:


# load Raman spectrum and apply a linear baseline correction
        s = spectrum()
        self.filepath = folder + filename[0:len(filename)-4]
        s.load_xy_txt(folder+filename)
        s1 = s.reverse()
        s2 = s1.subset(900.0,2000.0)
        sm = s2.smooth(9)
        l = sm.baseline_linear()
        self.s3 = s2.subtract(l)
        #self.s3 = s2
        
        #plt.plot(s.x,s.y)
        #plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def jbgsnuasxd():
    return render_template('katyal.html')
@app.route('/information',methods=['GET','POST'])
def xyz():
    if(request.method=='POST'):
        First=int(request.form['f'])
        Second=int(request.form['s'])
        total=(First+Second)
        return render_template('katyal.html',s=total)
if __name__=='__main__':
    app.run()


# In[ ]:


import flask


# In[ ]:


flask.__version__


# In[ ]:





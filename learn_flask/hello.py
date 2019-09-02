'''
https://www.w3cschool.cn/flask/flask_variable_rules.html
https://dormousehole.readthedocs.io/en/latest/quickstart.html
'''

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
# app.add_url_rule('/','hello')

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo
if __name__ == '__main__':
    app.run(debug= True)
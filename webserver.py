# To work on this
# cd to directory
# flask --app webserver.py run --debug (for debug mode)

from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# This will write to the database.txt (change in submit form)
# mode 'a' append to the file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


# This will write to the .csv file
# email, subject, message passed as list instead of f string
# The newline='' is added if the .csv already has headers
# check the documentation on adding headers with csv
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"],
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


# request method used to obtain input from page
# thankyou.html is just a copy of contact.html
# the redirect package and function redirects to the thankyou page
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Please try again.'







from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for job listings (replace this with your database)
job_listings = [
"Software Engineer Intern","Data Analyst","DataCorp"
]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/job_listings')
def job_listings():
    return render_template('job_listings.html', content = job_listings)

@app.route('/submit_resume', methods=['GET', 'POST'])
def submit_resume():
    if request.method == 'POST':
        # Process the submitted resume here (e.g., store in the database)
        return redirect(url_for('job_listings'))
    return render_template('submit_resume.html')

if __name__ == '__main__':
    app.run(debug=True)

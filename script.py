from flask import Flask, render_template, request
import pandas
app = Flask(__name__)

@app.route('/')


def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def index_post():
    if request.method == 'POST':
        req = request.files.get('fileToUpload')
        df = pandas.read_csv(req)
        base_pay_MEAN = "{:.2f}".format(df['BasePay'].mean())
        base_pay_MAX = "{:.2f}".format(df['BasePay'].max())
        base_pay_MIN = "{:.2f}".format(df['BasePay'].min())

        overtime_MAX = df['OvertimePay'].max()
        highest_paid_Person_NAME = (df[df['TotalPayBenefits'] == max(df['TotalPayBenefits'])]).iloc[0]['EmployeeName']
        highest_paid_Person_SALARY = (df[df['TotalPayBenefits'] == max(df['TotalPayBenefits'])]).iloc[0]['TotalPayBenefits']
        highest_paid_Person_JOB = (df[df['TotalPayBenefits'] == max(df['TotalPayBenefits'])]).iloc[0]['JobTitle']

        lowest_paid_Person_NAME = (df[df['TotalPayBenefits'] == min(df['TotalPayBenefits'])]).iloc[0]['EmployeeName']
        lowest_paid_Person_SALARY = (df[df['TotalPayBenefits'] == min(df['TotalPayBenefits'])]).iloc[0]['TotalPayBenefits']
        lowest_paid_Person_JOB = (df[df['TotalPayBenefits'] == min(df['TotalPayBenefits'])]).iloc[0]['JobTitle']
        num_Unique_Jobs = df['JobTitle'].nunique()
        most_common_jobs = df.groupby('JobTitle').count().sort_values(by='Id', ascending=False)['Id'].head(3)        
        return render_template('index.html',
        base_pay_Title="Basepay",
        base_pay_MEAN=( "Mean: $" + str(base_pay_MEAN)),
        base_pay_MAX=( "Max: $" + str(base_pay_MAX)),
        base_pay_MIN=( "Min: $" + str(base_pay_MIN)),
        over_time_Title="Overtime",
        over_time_MAX=("Max: $" + str(overtime_MAX)),
        highest_paid_Title = "Highest Paid",
        highest_paid_person=("Name: " + str(highest_paid_Person_NAME)),
        highest_paid_job=("Job: " + str(highest_paid_Person_JOB)),
        highest_paid_salary=("Salary: $" + str(highest_paid_Person_SALARY)),
        lowest_pay_Title = "Lowest Paid",
        lowest_paid_person=("Name: " + str(lowest_paid_Person_NAME)),
        lowest_paid_job=("Job: " + str(lowest_paid_Person_JOB)),
        lowest_paid_salary=("Salary: $" + str(lowest_paid_Person_SALARY))
        )
    else:
        render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)


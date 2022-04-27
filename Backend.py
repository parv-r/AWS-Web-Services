from crypt import methods
import boto3
from flask import Flask, redirect, url_for, request, render_template
import EC2Instance
import IAMUser
import S3Bucket

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

#EC2 Instance Services

#Create an EC2 Instance

@app.route('/create_ec2')
def create_ec2():
    EC2Instance.create_instance()
    return render_template("index.html")

#Terminate an EC2 Instance by redirecting to terminate_ec2_instance.html

@app.route('/terminate_ec2')
def terminate_ec2():
    return render_template("terminate_ec2_instance.html")

#EC2 Instance Terminated Successfully

@app.route('/terminated_ec2', methods=["POST"])
def terminated_ec2():
    if request.method == "POST":
        terminate_id = request.form["terminate_id"]
        EC2Instance.terminate_instance(terminate_id)
        return redirect(url_for("running_ec2"))

#Stop an EC2 Instance by redirecting to stop_ec2_instance.html

@app.route('/stop_ec2')
def stop_ec2():
    return render_template("stop_ec2_instance.html")

#EC2 Instance Stopped Successfully

@app.route('/stopped_ec2', methods=["POST"])
def stopped_ec2():
    if request.method == "POST":
        stop_id= request.form["stop_id"]
        EC2Instance.stop_instance(stop_id)
        return redirect(url_for("running_ec2"))

#Start an EC2 Instance Service Again by redirecting to start_ec2_instance.html

@app.route('/start_ec2')
def start_ec2():
    return render_template("start_ec2_instance.html")

#EC2 Instance Started Successfully

@app.route('/started_ec2', methods=["POST"])
def started_ec2():
    if request.method == "POST":
        start_id= request.form["start_id"]
        EC2Instance.start_instance(start_id)
        return redirect(url_for("running_ec2"))

#Shows all the Running EC2 Instances by redirecting to running_ec2_instances.html 

@app.route('/running_ec2')
def running_ec2():
    list1=EC2Instance.get_running_instances()
    return render_template("running_ec2_instances.html",list1=list1)
    
    
#Create IAM Services

#Create IAM User by redirecting to create_iam_user.html 

@app.route('/create_iam_user')
def create_iam_user():
    return render_template("create_iam_user.html")

#IAM user created successfully

@app.route('/created_iam_user', methods=["POST"])
def created_iam_user():
    if request.method == "POST":
        iamuser_id= request.form["iamuser_id"]
        IAMUser.create_user(iamuser_id)
        return redirect(url_for("listall_iam_users")) 

#List all the IAM users by redirecting to list_iam_users.html

@app.route('/listall_iam_users')
def listall_iam_users():
    list2=IAMUser.list_users()
    return render_template("list_iam_users.html",list2=list2)

#Route to Delete the IAM User by redirecting to delete_iam_user.html

@app.route('/delete_iam_user')
def delete_iam_user():
    return render_template("delete_iam_user.html")

#IAM User Deleted Successfully

@app.route('/deleted_iam_user', methods=["POST"])
def deleted_iam_user():
    if request.method == "POST":
        delete_iam_user_id = request.form["delete_iam_user_id"]
        IAMUser.delete_user(delete_iam_user_id)
        return redirect(url_for("listall_iam_users"))

# S3 Bucket Services

#Route to Create a S3 Bucket by redirecting to create_s3_bucket.html

@app.route('/create_s3_bucket')
def create_s3_bucket():
    return render_template("create_s3_bucket.html")

#S3 Bucket Created Successfully

@app.route('/created_s3_bucket', methods=["POST"])
def created_s3_bucket():
    if request.method == "POST":
        s3bucket_id= request.form["s3bucket_id"]
        S3Bucket.create_bucket(s3bucket_id)
        return redirect(url_for("listbucket"))

#Route to List All S3 Buckets by redirecting to list_buckets.html

@app.route('/listbucket')
def listbucket():
    list3=S3Bucket.list_bucket()
    return render_template("list_buckets.html",list3=list3)
    
#Route to Delete a S3 Bucket by redirecting to delete_s3_bucket.html

@app.route('/delete_s3_bucket')
def delete_s3_bucket():
    return render_template("delete_s3_bucket.html")

#S3 Bucket Deleted Successfully

@app.route('/deleted_s3_bucket', methods=["POST"])
def deleted_s3_bucket():
    if request.method == "POST":
        s3bucketdelete_id= request.form["s3bucketdelete_id"]
        S3Bucket.delete_bucket(s3bucketdelete_id)
        return redirect(url_for("listbucket"))

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

from flask import Flask, request
import subprocess

app = Flask(__name__)
@app.route('/deploy', methods=['GET', 'POST'])
def deploy():
    domain = request.form.get('domain')
    if not domain:
        return "Error: No domain provided", 400

    try:
        # Run the automation script as root
        subprocess.run(["/usr/local/bin/wp-setup", domain], check=True)
        return f"✅ Automation for {domain} completed!"
    except subprocess.CalledProcessError as e:
        return f"Automation failed: {e}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
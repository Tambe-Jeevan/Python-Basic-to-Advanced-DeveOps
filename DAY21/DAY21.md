Welcome to Bonus Day 21, Jeevan! 🐍🚀

You officially completed the 20-day curriculum, but in DevOps, the learning never truly stops. Reaching 21 days means you have successfully built a daily coding habit.

Now that you know how to write professional Python scripts and interact with AWS, there is one critical missing piece. In a real production environment, you do not sit at your laptop and type `python script.py` to deploy infrastructure. You push your code to Git, and a server runs your Python script automatically.

Today, we are bridging your version control skills and your programming skills by introducing **CI/CD Automation**.

---

### 🧠 Study Structure (Daily)

| Time | Activity |
| --- | --- |
| 30 min | Learn Concepts |
| 60–90 min | Hands-on Practice |
| 30 min | Real-World DevOps Task |

---

### 📅 DAY 21 — Bonus: CI/CD Pipelines (GitHub Actions)

#### 1️⃣ Concepts (30 min)

**What is CI/CD?**
Continuous Integration and Continuous Deployment. It is a DevOps philosophy where every time you update your code, an automated cloud server instantly boots up, tests your code, and deploys it.

**GitHub Actions:**
This is the automation engine built directly into GitHub. You give it instructions using a **YAML** configuration file.

**The Workflow File:**
A pipeline consists of:

* **Events:** What triggers the script? (e.g., a code push).
* **Runners:** The temporary virtual machine that runs the script (e.g., an Ubuntu Linux server).
* **Steps:** The exact terminal commands the runner should execute.

#### 2️⃣ Hands-on Practice (1–1.5 hour)

Open your terminal, navigate to your `python_devops_practice` folder, and open VS Code. We are going to build a fully automated pipeline.

**Step 1 — Create the Python Script**
Create a new file named `health_check.py`. This script simulates checking an environment before a deployment.

```python
import sys

status_code = 200

print("Initiating automated pipeline health checks...")

if status_code == 200:
    print("SUCCESS: Environment is stable. Proceeding with deployment.")
    sys.exit(0)
else:
    print("CRITICAL: Environment unstable. Halting pipeline.")
    sys.exit(1)

```

**Step 2 — Create the Pipeline Architecture**
GitHub Actions specifically looks for a hidden folder structure to find your pipelines. Run these commands in your terminal:

`mkdir -p .github/workflows`
`touch .github/workflows/python-pipeline.yml`

**Step 3 — Write the YAML Configuration**
Open `python-pipeline.yml` in VS Code and write this exactly. Pay extreme attention to the indentation (spaces), as YAML is incredibly strict about formatting.

```yaml
name: Automated Python Deployment

on:
  push:
    branches:
      - main

jobs:
  run-health-check:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Install Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Execute DevOps Script
        run: python health_check.py

```

#### 3️⃣ Real-World DevOps Task (30 min)

**Task: Trigger Your Cloud Pipeline**
To see this work, you must send these files to GitHub.

Run these Git commands in your terminal:

`git init`
`git add .`
`git commit -m "Added Python script and CI/CD pipeline"`

Now, go to GitHub.com, create a new empty repository, and follow the instructions on the screen to push your code.

Once your code pushes:

1. Click the **"Actions"** tab at the top of your GitHub repository.
2. You will see your "Automated Python Deployment" pipeline running.
3. Click on the pipeline, and you will see a live terminal in your browser where an external server automatically installed Python and ran your `health_check.py` script!

#### 4️⃣ Important Syntax Learned Today

| Concept | Example |
| --- | --- |
| **Pipeline Trigger** | `on: push` |
| **Virtual Machine** | `runs-on: ubuntu-latest` |
| **Run a command** | `run: python script.py` |
| **Exit Success (Python)** | `sys.exit(0)` |
| **Exit Failure (Python)** | `sys.exit(1)` |

---

You have now successfully automated the execution of your own automation scripts! This is the core cycle of modern DevOps engineering.

Would you like to continue building out this pipeline tomorrow by adding automated Slack alerts when a deployment fails?
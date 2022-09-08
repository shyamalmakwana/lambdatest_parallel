# Amazon web scraping with Selenium On LambdaTest


## Table Of Contents

* [Pre-requisites](#pre-requisites)
* [Run Your First Test](#run-your-first-test)
* [Local Testing With Python](#testing-locally-hosted-or-privately-hosted-projects)

## Prerequisites

Before you can start performing **Python** automation testing with **Selenium**, you would need to:

* Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version.
* Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
* Download the latest **Selenium Client** and its **WebDriver bindings** from the [official website](https://www.selenium.dev/downloads/). Latest versions of **Selenium Client** and **WebDriver** are ideal for running your automation script on LambdaTest Selenium cloud grid.

### Installing Selenium Dependencies And Tutorial Repo

**Step 1:** Clone the LambdaTest’s python-selenium-sample repository and navigate to the code directory as shown below:

```bash
git clone https://github.com/LambdaTest/python-selenium-sample
cd python-selenium-sample
```

**Step 2:** Download the driver from the link, or you can use **pip** to install it.
```bash
pip install selenium
export PYTHONWARNINGS="ignore:Unverified HTTPS request"   //Disable ssl warning
```

### Setting Up Your Authentication

Make sure you have your LambdaTest credentials with you to run test automation scripts. You can get these credentials from the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build) or by your [LambdaTest Profile](https://accounts.lambdatest.com/login).

**Step 2:** Set LambdaTest **Username** and **Access Key** in environment variables.

* For **Linux/macOS**:
  
  ```bash
  export LT_USERNAME="YOUR_USERNAME" 
  export LT_ACCESS_KEY="YOUR ACCESS KEY"
  ```
  * For **Windows**:
  ```bash
  set LT_USERNAME="YOUR_USERNAME" 
  set LT_ACCESS_KEY="YOUR ACCESS KEY"
  ```

### run 
```python parallel.py```


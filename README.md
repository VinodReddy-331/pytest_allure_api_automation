# pytest_allure_api_automation

- python --version
- python -m venv virtualenv1
- .\virtualenv1\Scripts\activate
- Install requirements.txt using below command
- pip install -r requirements.txt


- Below is the command to run test and generate reports
python -m pytest .\tests\test_restful_api.py --html-report=./report
 --alluredir=allure-results

- Below command is used to run the testcases in parallel.
python -m pytest -n <no_of_workers> --dist=loadscope .\tests\
Example: python -m pytest -n 4 --dist=loadscope .\tests\
where -n denotes no of worker and --dist=loadscope denotes the load per testfile.


- Below commands are used to generate Allure Report
  1. allure generate allure-results -o allure-report --clean
  2. allure open allure-report


#### Report1 : pytest htmlreporter 
![img.png](img.png)

 
#### Report2: Allure Report
![img_1.png](img_1.png)
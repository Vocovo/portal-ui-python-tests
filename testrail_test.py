# import os
# from testrail_api import TestRailAPI
#
#
# def main():
#     """Just testing the testrail integration"""
#     # Getting environment variables from the .env file
#     testrail_url = os.getenv("TESTRAIL_URL")
#     testrail_user = os.getenv("TESTRAIL_USER")
#     testrail_password = os.getenv("TESTRAIL_PASSWORD")
#     testrail_project_id = int(os.getenv("TESTRAIL_PROJECT_ID"))
#
#     # Initializing the TestRail client
#     client = TestRailAPI(testrail_url, testrail_user, testrail_password)
#
#     # Fetch all projects
#     response = client.projects.get_projects()
#     projects = response.get('projects', [])
#
#     # Find the specific project by ID
#
#     # for project in projects:
#     #     if project['id'] == testrail_project_id:
#     #         print(project)
#
#     suites = client.suites
#     print(suites.get_suite(812))
#
#     test_cases = client.cases
#     test_cases_in_suite = test_cases.get_cases(testrail_project_id, suite_id=812)
#
#     # Printing test cases
#     print("Test Cases in Suite 812:")
#     cases_list = test_cases_in_suite.get('cases', [])
#     for case in cases_list:
#         print(f"Case ID: {case['id']}, Title: {case['title']}")
#
#
# if __name__ == "__main__":
#     main()


import os

print(f"TESTRAIL_USER: {os.getenv('TESTRAIL_USER')}")
print(f"TESTRAIL_PASSWORD: {os.getenv('TESTRAIL_PASSWORD')}")

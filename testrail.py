import os
from testrail_api import TestRailAPI


class TestRailClient:
    def __init__(self):
        self.client = TestRailAPI(os.getenv("TESTRAIL_URL"), os.getenv("TESTRAIL_USER"), os.getenv("TESTRAIL_PASSWORD"))
        self.project_id = int(os.getenv("TESTRAIL_PROJECT_ID"))

    def create_test_run(self, name, case_ids, suite_id):
        run = self.client.runs.add_run(
            self.project_id, suite_id=suite_id, name=name, include_all=False, case_ids=case_ids
        )
        return run["id"]

    def update_test_result(self, run_id, case_id, status_id, comment=""):
        self.client.results.add_result_for_case(run_id, case_id, status_id=status_id, comment=comment)

    def close_test_run(self, run_id):
        self.client.runs.close_run(run_id)

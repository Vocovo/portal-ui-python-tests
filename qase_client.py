import os
from qaseio.api.runs_api import RunsApi
from qaseio.api.results_api import ResultsApi
from qaseio.models.run_create import RunCreate
from qaseio.models.result_create import ResultCreate
from qaseio.api_client import ApiClient


class QaseClient:
    def __init__(self):
        # Get API token and project code from environment variables
        api_token = os.getenv("QASE_API_TOKEN")
        self.project_code = os.getenv("QASE_PROJECT_CODE")

        # Initialize ApiClient with the token
        self.api_client = ApiClient(header_name="Token", header_value=api_token)

        # Initialize the Runs and Results API
        self.runs_api = RunsApi(self.api_client)
        self.results_api = ResultsApi(self.api_client)

    def create_test_run(self, title, case_ids):
        """Create a test run with the provided title and test case IDs."""
        if not isinstance(case_ids, list):
            case_ids = [case_ids]

        # Convert case IDs to integers if they are in string format
        case_ids = [int(case_id.split('-')[1]) if isinstance(case_id, str) else case_id for case_id in case_ids]

        run_create = RunCreate(title=title, cases=case_ids)

        try:
            response = self.runs_api.create_run(code=self.project_code, run_create=run_create)
            if response.status:
                print(f"Test run created successfully with ID: {response.result.id}")
                return response.result.id
            else:
                print(f"Failed to create test run: {response.message}")
                return None
        except Exception as e:
            print(f"Error creating test run: {str(e)}")
            return None

    def update_test_result(self, run_id, case_id, status, comment="", failure_reason=None, time=None):
        """Update the result for a test case in a test run."""
        if failure_reason:
            # Include the failure reason if provided
            comment = f"{comment}\nFailure Reason: {failure_reason}"

        result_create = ResultCreate(
            case_id=case_id,  # Ensure case_id is passed as an integer
            status=status,
            comment=comment
        )

        # If time is passed, include it in the result
        if time is not None:
            result_create.time = time  # Add time directly from the test

        try:
            response = self.results_api.create_result(
                code=self.project_code,
                id=run_id,
                result_create=result_create
            )
            if response.status:
                print(f"Result for case {case_id} updated successfully.")
            else:
                print(f"Failed to update result for case {case_id}: {response.message}")
        except Exception as e:
            print(f"Error updating result for case {case_id}: {str(e)}")

    def complete_test_run(self, run_id):
        """Complete the test run."""
        try:
            response = self.runs_api.complete_run(code=self.project_code, id=run_id)
            if response.status:
                print("Test run completed successfully.")
            else:
                print(f"Failed to complete test run: {response.message}")
        except Exception as e:
            print(f"Error completing test run: {str(e)}")
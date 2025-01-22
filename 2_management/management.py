


def main():

    print("JIRA Test Case Generation using GPT-4\n")

    print("Fetching JIRA Issue Details...\n")

    # Fetching the JIRA issue details
    jira_url = "https://maibornwolff-test-team.atlassian.net/rest/api/3/issue/SCRUM-27"
    fetcher = JiraIssueFetcher(jira_url)
    fetcher.fetch_issue()
    print("\n--- Issue Details ---")
    print(f"Summary: {fetcher.issue_summary}")
    print(f"Description:\n{fetcher.formatted_description}")
    print(f"Status: {fetcher.issue_status}")
    print(f"Creator: {fetcher.issue_creator}")
    print(f"Created: {fetcher.issue_created}")
    print("\n---------------------")

    # Define an URL for posting the JIRA Test Case Sub-Task
    create_testcase_jira_url = "https://maibornwolff-test-team.atlassian.net/rest/api/3/issue"
    print(f"Creating a Test Case Sub-Task for issue: {fetcher.issue_key}")

    # Generate a test case class for the retrieved issue
    test_issue = TestIssue(fetcher.issue_key, fetcher.formatted_description, create_testcase_jira_url)
    
    # GPT-4 Test Case Generation
    test_case = test_issue.generate_test_case(fetcher.issue_summary)
    
    # Push the generated test case to JIRA
    response = test_issue.push_test_case_to_jira(test_case)

    test_issue_key = None

    # Assuming the response contains the created issue details, extract the issue key from the test case
    if response.status_code == 201:  # HTTP 201 Created
        created_issue = response.json()

        #Printing retrieved test case json
        print("\n--- Test Case Details ---")
        print(created_issue)
        print("\n---------------------")

        test_issue_key = created_issue['key']

        print(f"Issue Key: {test_issue_key}")
    else:
        print(f"Failed to create test case: {response.status_code}")



"""     ### Playwright Test Code Generation ###

    #TODO: Implement the Playwright Test Code Generation



    ### Comparing the Test Code with the Test Case ###

    # Define the Jira URL
    # jira_url = "https://maibornwolff-test-team.atlassian.net/rest/api/3/issue/SCRUM-27"

    # Fetching the Playwright Test Code from Gitlab
    base_url = "https://gitlab.maibornwolff.de/api/v4"
    project_id = "2130"  # Replace with the actual project ID
    file_path = "tests%2Ftest_login.py" # %2F is the URL encoding for forward slash (/)
    branch_name = "comparing_test_case_with_test_code"
    
    retriever = GitLabCodeRetriever(base_url)
    
    print("\nFetching the Playwright Test Code from GitLab...\n")
    try:
        test_code = retriever.get_file_from_branch(project_id, file_path, branch_name)
        print("\n--- Playwright Test Code ---")
        print(test_code)
        print("\n---------------------")
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching file: {err}")


    # Fetch the Test Case from Jira

    base_jira_url = "https://maibornwolff-test-team.atlassian.net/"

    # Print the issue key and the test case identifier

    # Define the issue key for the parent issue
    issue_key = "SCRUM-27"  # Replace with your actual issue key


    # Define the identifier for the specific test case (either ID or summary)
    #identifier = "Test Case Summary or ID"  # Replace with your actual test case summary or ID
    identifier = test_issue_key

    print("\nFetching the Test Case from Jira...\n")
    test_fetcher = JiraTestCaseFetcher(base_jira_url)
    test_case = test_fetcher.get_test_case_for_issue(issue_key, identifier)
    print("\n--- Test Case Details ---")
    print(f"Description: {test_case}")


    # Using ChatGPT to compare if the test code corresponds to the test case
    print("\nComparing the Test Code with the Test Case...\n")

    comparator = GPTTestCaseCodeComparator()
    response = comparator.compare_case_with_code(test_case, test_code)
    print("\n--- Comparison Result ---")
    print(response)
    print("\n---------------------") """


if __name__ == "__main__":
    main()
import jira

# https://github.com/pycontribs/jira/tree/master/examples

def main():
    j = jira.JIRA("https://jiraserver.com", auth=('xxxx', 'xxxx'))

    # modify story
    s = j.issue('TEST-1234')
    s.update(summary="test from py code", description='test', comment='update issue summary')
    s.update(issuetype={"id":j.issue_type_by_name('Defect').id}, comment="update issue type")
    s.update(issuetype={"name":"Defect"}, comment="update issue type to defect")

    # create story
    j.create_issue(project='TEST', issuetype='Story', summary="created by jira api")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())

# rules.py
#
# Engineering rules used by the Engineering Agent.
#
# These functions implement simple checks over the engineering artifacts
# detected in the documentation such as:
# - Requirements (RF)
# - User Stories (US)
# - Test Cases (CT)
# - Services (*Service)

def check_requirements_without_tests(requirements, tests):
    """
    Identify requirements that do not have associated test cases.
    A simple heuristic is used: RFxx should correspond to CTxx.
    """

    missing = []

    for r in requirements:
        expected = r.replace("RF", "CT")

        found = False
        for t in tests:
            if expected in t:
                found = True
                break

        if not found:
            missing.append(r)

    return missing


def check_services_without_documentation(services, docs_text):
    """
    Check if services appear in documentation text.
    """

    undocumented = []

    for s in services:
        if s not in docs_text:
            undocumented.append(s)

    return undocumented


def check_minimum_test_coverage(requirements, tests):
    """
    Simple heuristic: there should be at least one CT per RF.
    """

    if not requirements:
        return False

    return len(tests) >= len(requirements)


def summarize_engineering_state(requirements, user_stories, tests, services):
    """
    Returns a simple engineering summary.
    """

    summary = {
        "requirements": len(requirements),
        "user_stories": len(user_stories),
        "tests": len(tests),
        "services": len(services)
    }

    return summary

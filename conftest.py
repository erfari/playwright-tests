from typing import Dict

import allure
import pytest
from _pytest.fixtures import SubRequest, FixtureRequest
from playwright.sync_api import Page, Playwright


@pytest.fixture(scope="function")
def browser_context_args(
        browser_context_args: Dict, base_url: str, request: SubRequest
):
    from utilities.contstants import AUTOMATION_USER_AGENT
    context_args = {
        **browser_context_args,
        "no_viewport": True,
        "user_agent": AUTOMATION_USER_AGENT,
    }

    if hasattr(request, "param"):
        context_args["storage_state"] = {
            "cookies": [
                {
                    "name": "session-username",
                    "value": request.param.value,
                    "url": base_url,
                }
            ]
        }
    return context_args


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict, playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


@pytest.fixture(autouse=True)
def attach_playwright_results(page: Page, request: FixtureRequest):
    yield
    if request.node.rep_call.failed:
        allure.attach(
            body=page.url,
            name="URL",
            attachment_type=allure.attachment_type.URI_LIST,
        )
        allure.attach(
            page.screenshot(full_page=True),
            name="Screen shot on failure",
            attachment_type=allure.attachment_type.PNG,
        )

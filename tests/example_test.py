from playwright.sync_api import Page, expect

def test_open_link(page: Page):
    page.goto("https://playwright.dev")
    expect(page.get_by_text("Playwright").first).to_be_visible()

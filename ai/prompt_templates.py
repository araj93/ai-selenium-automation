LOCATOR_HEAL_PROMPT = """
You are a Selenium automation expert.

This locator failed:
{locator}

HTML:
{dom}

Suggest a better XPath or CSS selector.
Return only the locator.
"""

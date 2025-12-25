from ai.openai_client import ask_ai
from ai.prompt_templates import LOCATOR_HEAL_PROMPT

def heal_locator(locator, dom):
    prompt = LOCATOR_HEAL_PROMPT.format(
        locator=locator,
        dom=dom[:3000]
    )
    return ask_ai(prompt)

from webscout import PhindSearch

def bot_response(user_text):
    ai = PhindSearch(quiet=True, is_conversation=None)
    res = ai.chat(user_text)  # internal stream is not available for this Provider
    return res

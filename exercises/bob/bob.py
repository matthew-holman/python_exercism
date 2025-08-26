import re


def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()

    if is_silence(hey_bob):
        return "Fine. Be that way!"

    if is_question(hey_bob):
        if is_all_caps(hey_bob):
            return "Calm down, I know what I'm doing!"
        return "Sure."

    if is_all_caps(hey_bob):
        return "Whoa, chill out!"

    return "Whatever."

def is_question(hey_bob: str) -> bool:
    return hey_bob[-1] == "?"

def is_all_caps(hey_bob: str) -> bool:
    return bool(re.search("[a-zA-Z]", hey_bob)) and hey_bob.upper() == hey_bob

def is_silence(hey_bob: str) -> bool:
    return len(hey_bob) == 0
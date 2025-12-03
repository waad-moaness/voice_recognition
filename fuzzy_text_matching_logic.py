import difflib
from text_processing import text_preprocessing

def check_fuzzy_keywords(child_speech, keywords, threshold=0.70):
    child_words = text_preprocessing(child_speech)
    missing_words = []
    keywords = text_preprocessing(keywords)
    for target in keywords:
        found = False

        # 1. Exact match shortcut (faster)
        if target in child_words:
            found = True
        else:
            # 2. Fuzzy match
            for word in child_words:
                similarity = difflib.SequenceMatcher(None, target, word).ratio()
                if similarity >= threshold:
                    found = True
                    break
        
        if not found:
            missing_words.append(target)

    if len(missing_words) == 0:
        return True, "Perfect!"
    else:
        return False, f"Missing: {', '.join(missing_words)}"
    

target = "I want to eat pizza"
spoken   = "I want eat piza"
print(check_fuzzy_keywords(spoken, target))
import difflib
from itertools import zip_longest

def grade_pronunciation(target_tokens, student_tokens):

    matcher = difflib.SequenceMatcher(None, target_tokens, student_tokens)
    
    report = []
    correct_words_count = 0
    total_teacher_words = len(target_tokens)

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        
        if tag == 'equal':
            chunk_len = i2 - i1
            correct_words_count += chunk_len
            
            for i in range(i1, i2):
                report.append({
                    "word": target_tokens[i],
                    "status": "green",
                    "info": "Perfect match"
                })

        elif tag == 'delete':
            for i in range(i1, i2):
                report.append({
                    "word": target_tokens[i],
                    "status": "red",
                    "info": "Missed word"
                })

        elif tag == 'replace':

            teacher_chunk = target_tokens[i1:i2]
            student_chunk = student_tokens[j1:j2]
            
            for t_word, s_word in zip_longest(teacher_chunk, student_chunk, fillvalue=None):
                
                if t_word is None:
                    break  

                if s_word is None:
                    report.append({
                        "word": t_word,
                        "status": "red",
                        "info": "Missed word"
                    })
                    continue 

                else:
                    similarity = difflib.SequenceMatcher(None, t_word, s_word).ratio()
                    
                    if similarity > 0.8:
                        correct_words_count += 1
                        report.append({
                            "word": t_word, 
                            "status": "yellow", 
                            "info": f"Accepted typo ({int(similarity*100)}%)"
                        })
                    else:
                        report.append({
                            "word": t_word, 
                            "status": "red", 
                            "info": f"Wrong word. Heard '{s_word}'"
                        })

    if total_teacher_words == 0:
        final_score = 0
    else:
        final_score = int((correct_words_count / total_teacher_words) * 100)

    return final_score, report

expected = "I want to eat pizza".split()
spoken   = "I want eat pizza".split()
                                    
score, details = grade_pronunciation(expected, spoken)
print(f"FINAL SCORE: {score}%")
print(f"{'WORD':<15} | {'STATUS':<10} | {'INFO'}")
print("-" * 50)
for item in details:
    print(f"{item['word']:<15} | {item['status']:<10} | {item['info']}")









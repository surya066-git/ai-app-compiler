import json
import os
from config.settings import settings

def score_quality(generation_id: str, repair_count: int, runtime_success: bool, prompt_handled: bool) -> dict:
    """Scores a generation attempt out of 100 based on compiler metrics."""
    score = 100
    
    if not prompt_handled:
        score -= 50
    if not runtime_success:
        score -= 40
        
    # Deduct 5 points per repair attempt (shows LLM hallucination)
    score -= (repair_count * 5)
    
    score = max(0, score)
    
    result = {
        "generation_id": generation_id,
        "score": score,
        "repair_count": repair_count,
        "runtime_success": runtime_success,
        "grade": "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    }
    
    # Save the score
    score_path = os.path.join(settings.STORAGE_DIR, f"{generation_id}_score.json")
    os.makedirs(settings.STORAGE_DIR, exist_ok=True)
    with open(score_path, "w") as f:
        json.dump(result, f, indent=4)
        
    return result

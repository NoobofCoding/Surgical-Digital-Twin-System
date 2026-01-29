def compute_score(deviation, smoothness):
    raw = 100 - (deviation * 350) - (smoothness * 60)
    return max(0, min(100, int(raw)))

def skill_phase(score):
    if score < 40:
        return "Novice"
    if score < 70:
        return "Intermediate"
    if score < 90:
        return "Advanced"
    return "Expert"

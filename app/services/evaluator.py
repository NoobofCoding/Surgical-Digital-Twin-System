from app.core.alignment import align_trajectories
from app.core.metrics import path_deviation, motion_smoothness
from app.core.scoring import compute_score, skill_phase
from app.core.coaching import generate_hint

def evaluate_motion(trainee_input, expert_data):
    t, e = align_trajectories(
        trainee_input["trajectory"],
        expert_data["trajectory"]
    )

    deviation = path_deviation(t, e)
    smoothness = motion_smoothness(t)
    score = compute_score(deviation, smoothness)
    phase = skill_phase(score)
    hint = generate_hint(deviation, smoothness)

    return {
        "score": score,
        "phase": phase,
        "hint": hint
    }

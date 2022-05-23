import json


def load_candidates_from_json():
    """возвращает список всех кандидатов"""
    with open("data/candidates.json", "rt", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_id == candidate.get("id"):
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower():
            candidates_found.append(candidate)
    return candidates_found


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json()
    skill_name = skill_name.lower()
    skill_candidates = []

    for candidate in candidates:
        skills = candidate.get("skills").lower().split(", ")
        if skill_name in skills:
            skill_candidates.append(candidate)
    return skill_candidates

def analyse_cv(name,skills):
    result = {
        "name":name,
        "skill_count":len(skills),
        "skills" : skills
    }
    return result

cv = analyse_cv("Vaibhav",["C#","Javascript","Python"])
print(cv["name"])
print(cv["skill_count"])

for skill in cv["skills"]:
    print(skill)
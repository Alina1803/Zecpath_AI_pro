STACKS = {
    "mern": ["mongodb", "express", "react", "node.js"],
    "mean": ["mongodb", "express", "angular", "node.js"],
    "lamp": ["linux", "apache", "mysql", "php"]
}


def expand_stack(skill):
    return STACKS.get(skill.lower(), [skill])
from agents import function_tool

@function_tool
def get_career_roadmap(career: str) -> str:
    """Returns a basic roadmap of skills required for a given career field."""
    roadmaps = {
        "web developer": "HTML → CSS → JavaScript → React → Node.js → Databases",
        "data scientist": "Python → Pandas → NumPy → Scikit-learn → Deep Learning",
        "graphic designer": "Color Theory → Photoshop → Illustrator → UI Design"
    }
    return roadmaps.get(career.lower(), "No roadmap available for this career.")
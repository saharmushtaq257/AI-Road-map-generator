import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🧭",
    layout="wide"
)

# Get Groq API key from Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def generate_roadmap(domain, level, learning_time, hours_per_week, goal):
    system_prompt = """
You are an expert learning roadmap designer.

Create practical and realistic learning roadmaps for students.

The roadmap should:
1. Match the user's current skill level.
2. Respect the available learning time.
3. Arrange topics from easy to difficult.
4. Include practical exercises.
5. Include projects.
6. Give a clear week-by-week learning plan.
7. Use simple, clear language.
"""

    user_prompt = f"""
Create a personalized learning roadmap.

Learning Domain: {domain}
Current Skill Level: {level}
Available Learning Time: {learning_time}
Hours Per Week: {hours_per_week}
Learning Goal: {goal}

Create the roadmap with:

# Learning Roadmap

## Learning Goal
Explain what the learner should achieve.

## Prerequisites
List important prerequisites.

## Weekly Roadmap
For each week include:
- Topics to learn
- Concepts to understand
- Practice tasks
- Mini project
- Expected outcome

## Projects
Suggest:
- Beginner project
- Intermediate project
- Final project

## Practice Strategy
Explain how the learner should practice.

## Final Outcome
Explain what the learner should be able to do after completing the roadmap.

Keep the roadmap realistic according to the available time.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


st.title("🧭 AI Learning Roadmap Generator")
st.write(
    "Create a personalized learning roadmap based on your "
    "skill level, available time, and learning goal."
)

st.divider()

domain = st.text_input(
    "Learning Domain",
    placeholder="e.g. Python, AI, Data Science, Web Development"
)

level = st.selectbox(
    "Current Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

learning_time = st.text_input(
    "Time Available",
    placeholder="e.g. 2 months, 3 months, 6 months"
)

hours_per_week = st.number_input(
    "Hours Per Week",
    min_value=1,
    max_value=60,
    value=10,
    step=1
)

goal = st.text_input(
    "Your Goal",
    placeholder="e.g. Become internship-ready"
)

if st.button("🚀 Generate Roadmap", use_container_width=True):
    if not domain.strip():
        st.warning("Please enter a learning domain.")
    elif not learning_time.strip():
        st.warning("Please enter your available learning time.")
    elif not goal.strip():
        st.warning("Please enter your learning goal.")
    else:
        with st.spinner("Creating your personalized roadmap..."):
            try:
                roadmap = generate_roadmap(
                    domain=domain,
                    level=level,
                    learning_time=learning_time,
                    hours_per_week=hours_per_week,
                    goal=goal
                )

                st.success("Your roadmap is ready!")
                st.markdown(roadmap)

            except Exception as e:
                st.error(
                    "Something went wrong while generating the roadmap."
                )
                st.caption(f"Error details: {e}")

"""
MBTI question bank — 50 questions covering 4 dimensions.
swap=False → option_a maps to pole1(E/S/T/J), option_b maps to pole2(I/N/F/P).
swap=True  → option_a maps to pole2, option_b maps to pole1.
Swap assignments are scattered to break predictable patterns.
"""

ALL_QUESTIONS = [
    # ═══════ EI (13 questions) ═══════
    {"id": 1, "dimension": "EI", "swap": False,
     "text": "After a long week, how do you prefer to recharge?",
     "option_a": "Go out with friends, social events energize me",
     "option_b": "Stay home with a book or movie, solitude restores me"},

    {"id": 2, "dimension": "EI", "swap": True,
     "text": "At a party, you tend to:",
     "option_a": "I prefer deeper conversations with a few people",
     "option_b": "I enjoy talking to many people and working the room"},

    {"id": 3, "dimension": "EI", "swap": False,
     "text": "When working on a project, you prefer:",
     "option_a": "Brainstorming out loud with a team",
     "option_b": "Thinking things through independently first"},

    {"id": 4, "dimension": "EI", "swap": True,
     "text": "People describe you as:",
     "option_a": "Reserved and reflective",
     "option_b": "Outgoing and talkative"},

    {"id": 5, "dimension": "EI", "swap": False,
     "text": "When you have something to share, you:",
     "option_a": "Say it immediately, thinking as you speak",
     "option_b": "Formulate it fully in my mind before speaking"},

    {"id": 6, "dimension": "EI", "swap": True,
     "text": "In a group discussion, you are more likely to:",
     "option_a": "Listen carefully and speak when I have something solid",
     "option_b": "Jump in and contribute ideas freely"},

    {"id": 7, "dimension": "EI", "swap": False,
     "text": "Your ideal work environment is:",
     "option_a": "Open, bustling, lots of interaction",
     "option_b": "Quiet, private, minimal distractions"},

    {"id": 8, "dimension": "EI", "swap": True,
     "text": "When meeting new people, you feel:",
     "option_a": "Cautious and observant at first",
     "option_b": "Excited and energized"},

    {"id": 9, "dimension": "EI", "swap": False,
     "text": "You prefer to communicate via:",
     "option_a": "Phone calls or face-to-face — faster and more dynamic",
     "option_b": "Text or email — gives me time to craft my response"},

    {"id": 10, "dimension": "EI", "swap": True,
     "text": "After attending a large social event, you feel:",
     "option_a": "Drained and needing alone time",
     "option_b": "Energized and happy"},

    {"id": 11, "dimension": "EI", "swap": True,
     "text": "When solving a problem, you tend to:",
     "option_a": "Reflect on it alone before discussing",
     "option_b": "Talk it through with others to clarify my thoughts"},

    {"id": 12, "dimension": "EI", "swap": False,
     "text": "Your friends would say you:",
     "option_a": "Initiate plans and bring people together",
     "option_b": "Are selective with social plans and value depth over breadth"},

    {"id": 13, "dimension": "EI", "swap": True,
     "text": "In a waiting room or on public transport, you:",
     "option_a": "Keep to yourself and observe quietly",
     "option_b": "Strike up a conversation with a stranger"},

    # ═══════ SN (13 questions) ═══════
    {"id": 14, "dimension": "SN", "swap": False,
     "text": "When learning something new, you prefer:",
     "option_a": "Step-by-step instructions with concrete examples",
     "option_b": "Understanding the big picture and underlying theory first"},

    {"id": 15, "dimension": "SN", "swap": True,
     "text": "You trust more:",
     "option_a": "Gut feelings and new possibilities",
     "option_b": "Past experience and proven methods"},

    {"id": 16, "dimension": "SN", "swap": False,
     "text": "Which describes you better?",
     "option_a": "I focus on details and practical realities",
     "option_b": "I enjoy exploring abstract ideas and patterns"},

    {"id": 17, "dimension": "SN", "swap": True,
     "text": "When reading, you pay more attention to:",
     "option_a": "Themes, implications, and the author's vision",
     "option_b": "Facts, data, and specific examples"},

    {"id": 18, "dimension": "SN", "swap": False,
     "text": "Given a new task, you prefer to:",
     "option_a": "Follow an established process that works",
     "option_b": "Experiment and find a new, possibly better way"},

    {"id": 19, "dimension": "SN", "swap": True,
     "text": "You are more interested in:",
     "option_a": "What could be, future possibilities and innovations",
     "option_b": "What is happening right now, the tangible reality"},

    {"id": 20, "dimension": "SN", "swap": False,
     "text": "In a conversation, you find yourself drawn to:",
     "option_a": "Practical, down-to-earth topics",
     "option_b": "Theoretical, imaginative discussions"},

    {"id": 21, "dimension": "SN", "swap": True,
     "text": "When making a decision, you rely more on:",
     "option_a": "Patterns, connections, and intuitive leaps",
     "option_b": "Concrete data and observable facts"},

    {"id": 22, "dimension": "SN", "swap": False,
     "text": "You would describe yourself as:",
     "option_a": "Realistic and grounded",
     "option_b": "Visionary and idea-driven"},

    {"id": 23, "dimension": "SN", "swap": False,
     "text": "When tackling a complex problem, you start with:",
     "option_a": "Breaking it down into manageable, concrete steps",
     "option_b": "Looking for the underlying principle that connects everything"},

    {"id": 24, "dimension": "SN", "swap": True,
     "text": "At work, you are more energized by:",
     "option_a": "Brainstorming innovative approaches and new projects",
     "option_b": "Executing tasks with precision and consistency"},

    {"id": 25, "dimension": "SN", "swap": False,
     "text": "Which hobby appeals to you more?",
     "option_a": "Cooking, woodworking, or gardening — hands-on and sensory",
     "option_b": "Writing, painting, or learning philosophy — creative and abstract"},

    {"id": 26, "dimension": "SN", "swap": True,
     "text": "When someone tells a story, you want them to:",
     "option_a": "Get to the point and share the meaning behind it",
     "option_b": "Give a clear, chronological account with all the details"},

    # ═══════ TF (12 questions) ═══════
    {"id": 27, "dimension": "TF", "swap": False,
     "text": "When making an important decision, you prioritize:",
     "option_a": "Logic, fairness, and objective analysis",
     "option_b": "Impact on people, harmony, and personal values"},

    {"id": 28, "dimension": "TF", "swap": True,
     "text": "A colleague is upset about a decision. You tend to:",
     "option_a": "Acknowledge their feelings and try to find a compromise",
     "option_b": "Explain the rationale and data behind the decision"},

    {"id": 29, "dimension": "TF", "swap": False,
     "text": "You are more impressed by:",
     "option_a": "A well-reasoned, logically flawless argument",
     "option_b": "A deeply empathetic and compassionate act"},

    {"id": 30, "dimension": "TF", "swap": True,
     "text": "In a debate, you focus on:",
     "option_a": "Understanding the values and motivations behind each position",
     "option_b": "Spotting inconsistencies and flaws in the logic"},

    {"id": 31, "dimension": "TF", "swap": False,
     "text": "When giving feedback, you tend to be:",
     "option_a": "Direct and critical — honesty helps people improve",
     "option_b": "Encouraging and supportive — I avoid hurting feelings"},

    {"id": 32, "dimension": "TF", "swap": True,
     "text": "You believe justice is best served when:",
     "option_a": "Individual circumstances and context are taken into account",
     "option_b": "Rules are applied consistently and impartially"},

    {"id": 33, "dimension": "TF", "swap": False,
     "text": "People would describe you as:",
     "option_a": "Analytical and objective",
     "option_b": "Warm and compassionate"},

    {"id": 34, "dimension": "TF", "swap": True,
     "text": "When a friend is going through a tough time, you first:",
     "option_a": "Listen and provide emotional support",
     "option_b": "Offer practical solutions and a plan of action"},

    {"id": 35, "dimension": "TF", "swap": False,
     "text": "At work, you are more concerned with:",
     "option_a": "Getting the job done efficiently and correctly",
     "option_b": "Maintaining positive team dynamics and morale"},

    {"id": 36, "dimension": "TF", "swap": True,
     "text": "Which criticism would bother you more?",
     "option_a": '"You hurt someone\'s feelings"',
     "option_b": '"Your reasoning doesn\'t hold up"'},

    {"id": 37, "dimension": "TF", "swap": False,
     "text": "You respect a leader who:",
     "option_a": "Makes tough, data-driven decisions even when unpopular",
     "option_b": "Builds consensus and cares deeply about the team's well-being"},

    {"id": 38, "dimension": "TF", "swap": True,
     "text": "When evaluating a purchase, you look at:",
     "option_a": "How it makes you feel, aesthetics, and personal fit",
     "option_b": "Specifications, performance data, and cost-benefit analysis"},

    # ═══════ JP (12 questions) ═══════
    {"id": 39, "dimension": "JP", "swap": True,
     "text": "How do you approach your daily life?",
     "option_a": "I prefer to stay flexible and see where the day takes me",
     "option_b": "I like having a clear schedule and sticking to it"},

    {"id": 40, "dimension": "JP", "swap": False,
     "text": "When working on a deadline, you:",
     "option_a": "Plan ahead and finish early to avoid last-minute stress",
     "option_b": "Work best under pressure, often pulling things together at the end"},

    {"id": 41, "dimension": "JP", "swap": True,
     "text": "You feel more comfortable when:",
     "option_a": "Options are kept open and plans can change",
     "option_b": "Decisions are made and things are settled"},

    {"id": 42, "dimension": "JP", "swap": False,
     "text": "Your desk or workspace is usually:",
     "option_a": "Organized and tidy, everything in its place",
     "option_b": "A bit chaotic but I know where everything is"},

    {"id": 43, "dimension": "JP", "swap": True,
     "text": "When starting a big project, you:",
     "option_a": "Dive in and figure it out as you go",
     "option_b": "Break it into steps with milestones and a timeline"},

    {"id": 44, "dimension": "JP", "swap": False,
     "text": "How do you feel about routines?",
     "option_a": "They give me structure and productivity",
     "option_b": "They feel restrictive — I prefer variety and spontaneity"},

    {"id": 45, "dimension": "JP", "swap": True,
     "text": "When you finish one task, you typically:",
     "option_a": "Get distracted by something interesting and change course",
     "option_b": "Check it off and move to the next planned item"},

    {"id": 46, "dimension": "JP", "swap": False,
     "text": "You prefer a work environment where:",
     "option_a": "Expectations, roles, and deadlines are clearly defined",
     "option_b": "There is flexibility to explore and adapt as needed"},

    {"id": 47, "dimension": "JP", "swap": True,
     "text": "Making a decision feels:",
     "option_a": "Limiting — I like to keep my options open as long as possible",
     "option_b": "Satisfying — closure is important to me"},

    {"id": 48, "dimension": "JP", "swap": False,
     "text": "When plans change unexpectedly, you:",
     "option_a": "Feel frustrated and try to get back on track",
     "option_b": "Adapt easily and see it as an opportunity"},

    {"id": 49, "dimension": "JP", "swap": True,
     "text": "You are more likely to:",
     "option_a": "Keep a mental list and do things as they feel right",
     "option_b": "Make a to-do list and methodically work through it"},

    {"id": 50, "dimension": "JP", "swap": False,
     "text": "Which describes your approach to life better?",
     "option_a": "Plan, prepare, and execute with discipline",
     "option_b": "Explore, adapt, and go with the flow"},
]


def get_questions(count=25):
    if count >= 50:
        return list(ALL_QUESTIONS)
    selected = []
    per_dim = count // 4
    extra = count % 4
    dim_groups = {"EI": [], "SN": [], "TF": [], "JP": []}
    for q in ALL_QUESTIONS:
        dim_groups[q["dimension"]].append(q)
    for dim in ["EI", "SN", "TF", "JP"]:
        selected.extend(dim_groups[dim][:per_dim])
    for i in range(extra):
        dim = ["EI", "SN", "TF", "JP"][i]
        selected.append(dim_groups[dim][per_dim])
    selected.sort(key=lambda q: q["id"])
    return selected

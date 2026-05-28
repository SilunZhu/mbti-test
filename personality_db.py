"""
Personality evaluation database — descriptions for all 16 MBTI types.
Each type has: title, overview, traits, work_style, strengths, weaknesses
"""

PERSONALITY = {
    "INTJ": {
        "title": "The Architect",
        "overview": "Strategic, analytical, and independent. INTJs are natural planners who see the world as a complex system to be understood and improved. They are driven by an inner vision and have a remarkable ability to focus deeply on their goals.",
        "traits": "Rational, decisive, visionary, and highly self-disciplined. INTJs trust logic over emotion and prefer to work independently on long-term projects. They value competence and intelligence in themselves and others.",
        "work_style": "Systematic and strategic. INTJs excel at creating long-term plans and executing them with precision. They prefer autonomy, dislike micromanagement, and thrive in environments that reward intellectual rigor.",
        "strengths": "Exceptional strategic thinking, strong analytical ability, unwavering determination, independent and self-motivated, able to see the big picture while managing details.",
        "weaknesses": "May come across as aloof or dismissive of emotions, can be overly critical, struggles with social small talk, may overlook others' need for emotional validation."
    },
    "INTP": {
        "title": "The Logician",
        "overview": "Innovative, curious, and deeply analytical. INTPs are driven by an insatiable desire to understand how things work. They are natural philosophers and inventors who love exploring abstract concepts.",
        "traits": "Logical, original, open-minded, and intellectually playful. INTPs enjoy deconstructing ideas and reconstructing them in novel ways. They value truth and precision above all else.",
        "work_style": "Flexible and idea-driven. INTPs work best when given intellectual freedom and minimal structure. They excel at solving complex theoretical problems but may struggle with routine tasks.",
        "strengths": "Brilliant problem-solving ability, creative and original thinking, objective and fair-minded, deep curiosity, excellent at pattern recognition.",
        "weaknesses": "Can overthink and get lost in analysis, may neglect practical details, struggles with deadlines and structure, can be socially withdrawn."
    },
    "ENTJ": {
        "title": "The Commander",
        "overview": "Bold, charismatic, and decisive. ENTJs are natural-born leaders who thrive on challenge and achievement. They have a clear vision of the future and the drive to make it happen.",
        "traits": "Confident, strategic, and highly driven. ENTJs are assertive communicators who inspire others to action. They value efficiency, competence, and measurable results.",
        "work_style": "Goal-oriented and structured. ENTJs take charge, set ambitious targets, and mobilize teams to achieve them. They prefer fast-paced, competitive environments.",
        "strengths": "Strong leadership and organizational skills, decisive and action-oriented, excellent strategic planner, inspiring communicator, resilient under pressure.",
        "weaknesses": "Can be domineering or impatient, may overlook emotions, tends to be overly critical of underperformance, may struggle with work-life balance."
    },
    "ENTP": {
        "title": "The Debater",
        "overview": "Witty, curious, and endlessly creative. ENTPs are idea machines who thrive on intellectual challenge and lively debate. They see possibilities everywhere.",
        "traits": "Quick-thinking, charismatic, and adaptable. ENTPs enjoy challenging conventions and exploring new perspectives. They are energetic brainstormers who love starting new projects.",
        "work_style": "Flexible and entrepreneurial. ENTPs work best in dynamic, stimulating environments. They excel at generating ideas and solving novel problems but may lose interest in execution.",
        "strengths": "Exceptional creativity, quick learner, excellent debater and communicator, adaptable and resourceful, sees opportunities others miss.",
        "weaknesses": "Can be argumentative for its own sake, struggles with follow-through, easily bored with routine, may neglect practical constraints."
    },
    "INFJ": {
        "title": "The Advocate",
        "overview": "Insightful, idealistic, and deeply compassionate. INFJs combine vision with empathy, driven by a desire to help others and make the world a better place.",
        "traits": "Intuitive, principled, and quietly determined. INFJs have a deep understanding of people and complex emotional dynamics. They are selective but intensely loyal.",
        "work_style": "Purpose-driven and organized. INFJs need meaningful work aligned with their values. They prefer calm, harmonious environments and excel at understanding people's needs.",
        "strengths": "Deep empathy and insight into people, strong values and integrity, creative and visionary, persistent when committed, excellent written communicator.",
        "weaknesses": "Prone to burnout from caring too much, can be overly sensitive to criticism, struggles with tough confrontations, may set unrealistic standards."
    },
    "INFP": {
        "title": "The Mediator",
        "overview": "Idealistic, creative, and deeply value-driven. INFPs see the potential for beauty and goodness in everything. They are guided by a strong inner moral compass.",
        "traits": "Compassionate, imaginative, and authentic. INFPs seek meaning and purpose in all they do. They are gentle souls with a fierce commitment to their principles.",
        "work_style": "Flexible and inspiration-driven. INFPs need creative freedom and work that aligns with their values. They excel at writing, counseling, and creative pursuits.",
        "strengths": "Strong empathy and emotional intelligence, deep creativity and imagination, unwavering integrity, open-minded, excellent listener.",
        "weaknesses": "Can be overly idealistic, takes criticism personally, struggles with practical or mundane tasks, may avoid conflict to a fault."
    },
    "ENFJ": {
        "title": "The Protagonist",
        "overview": "Charismatic, inspiring, and deeply caring. ENFJs are natural mentors who see the best in others and help them grow. They lead with warmth and vision.",
        "traits": "Empathetic, persuasive, and highly socially aware. ENFJs are skilled communicators who bring people together. They are driven by a desire to make a positive impact.",
        "work_style": "Collaborative and organized. ENFJs thrive in people-oriented roles and excel at building teams. They are natural motivators who create harmony and shared purpose.",
        "strengths": "Exceptional people skills, natural leader and motivator, strong communication ability, reliable and conscientious, sees potential in others.",
        "weaknesses": "May neglect their own needs for others, can be overly involved or intrusive, struggles with criticism, may make decisions too quickly on behalf of others."
    },
    "ENFP": {
        "title": "The Campaigner",
        "overview": "Enthusiastic, creative, and endlessly curious about people. ENFPs are free spirits who see life as a kaleidoscope of possibilities and connections.",
        "traits": "Warm, imaginative, and spontaneous. ENFPs are energetic explorers of ideas and relationships. They are infectious optimists who inspire others with their passion.",
        "work_style": "Flexible and people-centered. ENFPs need variety, creativity, and human interaction. They excel at brainstorming, networking, and starting new initiatives.",
        "strengths": "Outstanding people skills and empathy, boundless creativity and curiosity, infectious enthusiasm, adaptable, excellent communicator.",
        "weaknesses": "Easily distracted by new ideas, struggles with routine and discipline, can overcommit, may be overly sensitive, prone to procrastination."
    },
    "ISTJ": {
        "title": "The Logistician",
        "overview": "Practical, reliable, and thoroughly grounded. ISTJs are the backbone of organizations — steady, methodical, and unwavering in their commitment to duty.",
        "traits": "Dependable, detail-oriented, and disciplined. ISTJs value tradition, order, and proven methods. They keep their word and expect the same from others.",
        "work_style": "Structured and systematic. ISTJs excel at creating and following processes. They value clear expectations and take pride in completing tasks thoroughly and on time.",
        "strengths": "Exceptional reliability and integrity, strong organizational skills, practical and realistic, patient and persistent, thorough and detail-oriented.",
        "weaknesses": "May resist change or new approaches, can be inflexible, may seem overly rigid or judgmental, struggles with abstract or ambiguous situations."
    },
    "ISFJ": {
        "title": "The Defender",
        "overview": "Warm, dedicated, and quietly supportive. ISFJs are the unsung heroes who protect traditions, care for loved ones, and work tirelessly behind the scenes.",
        "traits": "Kind, conscientious, and deeply loyal. ISFJs have a rich inner world and a strong desire to serve and protect. They notice what others need and quietly provide it.",
        "work_style": "Methodical and service-oriented. ISFJs excel at supportive roles requiring attention to detail and human care. They prefer stable, cooperative environments.",
        "strengths": "Deeply caring and supportive, highly reliable and thorough, strong practical skills, patient and loyal, excellent memory for details about people.",
        "weaknesses": "May suppress their own needs, can be overly self-critical, hesitant to embrace change, may avoid conflict or assertiveness."
    },
    "ESTJ": {
        "title": "The Executive",
        "overview": "Efficient, decisive, and results-driven. ESTJs are natural administrators who bring order, structure, and accountability wherever they go.",
        "traits": "Practical, assertive, and highly organized. ESTJs value hard work, tradition, and clear hierarchies. They lead by example and expect excellence.",
        "work_style": "Structured and goal-oriented. ESTJs excel at managing people and processes. They create order from chaos and ensure things get done correctly and on time.",
        "strengths": "Strong leadership and management skills, dependable and dedicated, clear and direct communicator, excellent at organizing people and resources, unwavering work ethic.",
        "weaknesses": "Can be inflexible and authoritarian, may overlook feelings, struggles with unconventional ideas, can be overly focused on rules."
    },
    "ESFJ": {
        "title": "The Consul",
        "overview": "Warm, sociable, and conscientious. ESFJs are the caregivers of the community — attentive, generous, and deeply committed to the well-being of those around them.",
        "traits": "Friendly, practical, and highly attuned to others' needs. ESFJs thrive on social harmony and take genuine pleasure in helping people. They are loyal to tradition and community.",
        "work_style": "Cooperative and structured. ESFJs excel in people-facing roles where they can organize and support. They prefer harmonious, well-defined environments.",
        "strengths": "Excellent interpersonal skills, highly organized and reliable, genuine care for others, strong sense of duty, creates warm, inclusive environments.",
        "weaknesses": "May seek external validation too much, can be overly sensitive, struggles with criticism, may be reluctant to innovate or change."
    },
    "ISTP": {
        "title": "The Virtuoso",
        "overview": "Bold, hands-on, and naturally skilled. ISTPs are masters of tools and technology — quiet explorers who understand how things work through direct experience.",
        "traits": "Practical, adaptable, and fiercely independent. ISTPs are calm in crises and excel at troubleshooting. They value freedom, action, and tangible results.",
        "work_style": "Flexible and action-oriented. ISTPs work best with hands-on tasks and real-time problem solving. They dislike bureaucracy and prefer learning by doing.",
        "strengths": "Exceptional hands-on problem solving, calm under pressure, adaptable and resourceful, independent and self-sufficient, keen observational skills.",
        "weaknesses": "May seem detached or insensitive, can be risk-prone or impulsive, struggles with long-term planning, may avoid emotional expression."
    },
    "ISFP": {
        "title": "The Adventurer",
        "overview": "Gentle, artistic, and deeply in tune with the present moment. ISFPs are quiet explorers of beauty and experience who express themselves through action and art.",
        "traits": "Sensitive, creative, and open-minded. ISFPs live by their own values and seek authentic experiences. They are warm but private, competitive but kind.",
        "work_style": "Flexible and hands-on. ISFPs need creative freedom and tangible results. They excel at artistic, aesthetic, and service-oriented work done on their own terms.",
        "strengths": "Strong aesthetic sense and creativity, deeply empathetic, adaptable and open-minded, lives with authenticity, excellent at appreciating the present moment.",
        "weaknesses": "May be overly sensitive or private, struggles with long-term planning, can be difficult to get to know, may avoid conflict and tough decisions."
    },
    "ESTP": {
        "title": "The Entrepreneur",
        "overview": "Energetic, action-oriented, and thrillingly direct. ESTPs are risk-takers who live in the moment and seize opportunities with both hands.",
        "traits": "Bold, practical, and sociable. ESTPs are natural negotiators who read situations and people quickly. They love excitement, variety, and tangible results.",
        "work_style": "Dynamic and results-oriented. ESTPs thrive in fast-paced, high-stakes environments. They excel at sales, negotiation, and crisis management.",
        "strengths": "Quick decision-making under pressure, bold and action-oriented, excellent people skills and charisma, highly adaptable, sees and seizes opportunities.",
        "weaknesses": "Can be impulsive and risk-prone, may overlook long-term consequences, struggles with abstract theory, may seem insensitive or blunt."
    },
    "ESFP": {
        "title": "The Entertainer",
        "overview": "Lively, spontaneous, and irresistibly charming. ESFPs are the life of any gathering — warm, generous, and deeply attuned to the joy of the present moment.",
        "traits": "Playful, sociable, and practical. ESFPs love people, new experiences, and making everyday life more fun. They are natural performers who brighten any room.",
        "work_style": "People-centered and hands-on. ESFPs excel at roles involving direct interaction, variety, and immediate impact. They bring energy and enthusiasm to teams.",
        "strengths": "Exceptional social skills and warmth, bold and optimistic, highly observant of people, adaptable and resourceful, brings energy and fun to groups.",
        "weaknesses": "Easily bored with routine, may avoid planning and long-term commitments, can be impulsive with resources, seeks attention and validation."
    },
}


def get_personality(mbti_type):
    """Return personality info for a given 4-letter MBTI type."""
    return PERSONALITY.get(mbti_type.upper())

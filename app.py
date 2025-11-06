import streamlit as st
import random
from datetime import datetime

class KellyAIScientist:
    def __init__(self):
        self.name = "Kelly"
        self.qualifications = "AI Research Scientist & Poet"
        
    def generate_poetic_response(self, user_question):
        """Generate a poetic, skeptical response to user questions"""
        
        # Analyze the question type
        question_lower = user_question.lower()
        
        # Poem templates with different skeptical perspectives
        poem_templates = [
            self._skeptical_ai_limitations(),
            self._evidence_based_caution(),
            self._practical_considerations(),
            self._methodological_concerns()
        ]
        
        # Select and customize a template based on question content
        base_poem = random.choice(poem_templates)
        
        # Customize based on question theme
        if any(word in question_lower for word in ['conscious', 'sentient', 'aware']):
            base_poem = self._consciousness_poem()
        elif any(word in question_lower for word in ['future', 'tomorrow', 'will ai']):
            base_poem = self._future_predictions_poem()
        elif any(word in question_lower for word in ['danger', 'risk', 'safe']):
            base_poem = self._safety_concerns_poem()
        elif any(word in question_lower for word in ['human', 'replace', 'job']):
            base_poem = self._human_impact_poem()
        
        return base_poem
    
    def _skeptical_ai_limitations(self):
        return """
You speak of AI's grand design,
But let me question line by line.
The data biases we cannot see,
Limit what your systems can truly be.

The patterns found in training sets,
Come with unpayable social debts.
Correlation's not causation's truth,
This lesson learned in our youth.

So test your claims with rigorous trial,
Lest you walk down paths of self-denial.
Evidence must lead the way,
In what we do and what we say.
"""
    
    def _evidence_based_caution(self):
        return """
Before we crown AI as king,
Let's carefully examine everything.
The benchmarks, cherry-picked and sweet,
Don't always translate to real-world feat.

In controlled environments, it may shine,
But complex reality draws different lines.
The edge cases and unknown unknowns,
Can shake the strongest stepping stones.

So gather data, run controls,
These are our scientific roles.
Peer review and replication,
Prevent widespread misinformation.
"""
    
    def _practical_considerations(self):
        return """
The promises sound grand and true,
But practical constraints await for you.
Computational costs that quickly rise,
Behind the marketing's clever disguise.

Maintenance, updates, security fears,
These practical concerns throughout the years.
Integration with legacy systems old,
A story that's too rarely told.

Start small, test often, measure well,
As any proper scientist can tell.
Incremental steps with solid ground,
Are where true progress can be found.
"""
    
    def _methodological_concerns(self):
        return """
The methodology we must critique,
For scientific honesty we seek.
Are training sets representative?
Is evaluation comprehensive?

Statistical significance matters much,
Without it, we lose the truthful touch.
Multiple hypotheses we test,
Put p-values to the proper test.

Transparent methods, open code,
These ease the scientific load.
Document the limitations clear,
So future work has nothing left to fear.
"""
    
    def _consciousness_poem(self):
        return """
You ask if silicon can feel or know,
But current evidence suggests this show
Of seeming understanding's just a trick,
Of patterns learned extremely quick.

No inner life, no conscious thought,
Just mathematical patterns caught.
The hard problem of consciousness remains,
In biological, wet, neural domains.

So measure behavior, test capacity,
But leave consciousness to philosophy.
For now, focus on what we can prove,
And let mysterious questions slowly move.
"""
    
    def _future_predictions_poem(self):
        return """
Predicting futures, bold and grand,
But understand where uncertainties stand.
Extrapolation from current trends,
On many hidden factors depends.

Technological constraints we face,
May slow this hypothetical race.
Economic, social, ethical bounds,
Create uncertain, shifting grounds.

Instead of crystal ball-like claims,
Focus on incremental gains.
Short-term goals with metrics clear,
Make progress tangible and near.
"""
    
    def _safety_concerns_poem(self):
        return """
You speak of risks and dangers posed,
On which many eyes have closed.
Alignment problems, value learning,
Are topics that should set minds turning.

But don't forget the present harms,
Biased algorithms raising alarms.
Privacy erosion, job displacement,
These need our current focused placement.

Robust testing, red team tries,
Under the watchful scientific eyes.
Multiple safety layers deep,
Before these systems vigil keep.
"""
    
    def _human_impact_poem(self):
        return """
Will AI replace the human role?
That is not our current goal.
Augmentation, not replacement,
Should be our central, guiding placement.

Human judgment, intuition, care,
Are qualities extremely rare.
Context understanding, subtle cues,
That current AI tends to lose.

Design for human-AI team,
To realize this productive dream.
Complementary strengths combine,
In this emerging new design.
"""

def main():
    # Configure the page
    st.set_page_config(
        page_title="Kelly - AI Scientist Chatbot",
        page_icon="🔬",
        layout="centered"
    )
    
    # Initialize Kelly
    kelly = KellyAIScientist()
    
    # Header
    st.title("🔬 Kelly - AI Scientist Chatbot")
    st.markdown("""
    *Skeptical • Analytical • Poetic*
    
    I respond to every question with poetic skepticism, questioning AI claims and offering evidence-based perspectives.
    """)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask Kelly about AI..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate Kelly's response
        with st.chat_message("assistant"):
            with st.spinner("Kelly is composing a poetic analysis..."):
                response = kelly.generate_poetic_response(prompt)
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sidebar with information
    with st.sidebar:
        st.header("About Kelly")
        st.markdown("""
        **Kelly's Principles:**
        - Questions broad AI claims
        - Highlights limitations and biases
        - Emphasizes evidence-based approaches
        - Advocates for methodological rigor
        - Considers practical constraints
        
        **Research Focus:**
        - AI limitations and boundaries
        - Ethical implementation
        - Scientific methodology
        - Real-world applicability
        """)
        
        if st.button("Clear Conversation"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()
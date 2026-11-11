# Explain the project in class

**What is the problem?** LLMs can tell a compelling story but may contradict prior
turns or treat a player's claim as a fact. Application state needs independent rules.

**What did V1 do?** `v1.respond` sends room instructions and conversation history
to Gemini. The model is narrator and referee. The app recognizes its escape marker.

**What changed?** V2's model proposes an Action with verb, target and value.
The user confirms it; `engine.apply` checks it against a State dataclass and author
rules. Only a validated transition produces the next state.

**Why copy the state?** A rejected move must not leave a partial inventory or lock
change. The old state stays intact, which also makes tests easier to reason about.

**Where are secrets?** The puzzle answers are in author code, never in V2 parser
or atmosphere prompts. They are spoilers visible to repository readers, not API
credentials. Real API credentials are environment variables and ignored by Git.

**Is the offline mode AI?** No. It is a limited deterministic parser used for
practice and testing without spending quota. Both actual AI versions require Gemini.

**Why limit narration?** A freely generated sentence could say 'the door opens'
while Python says it is locked. V2 uses engine-authored outcomes plus safe atmosphere.
The tradeoff is reduced creativity in exchange for consistent game facts.

**What is still uncertain?** Real Gemini interpretation quality and V1 failure rates
need live tests. Mocked tests verify integration contracts, not provider behavior.

**What would you improve next?** More natural-language paraphrase tests, a larger
safe narration library, better action labels and optional saved-game persistence.
Review all code and change the story/puzzles if you want to make the design your own.

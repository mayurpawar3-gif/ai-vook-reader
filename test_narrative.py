from narrative_engine import NarrativeEngine

engine = NarrativeEngine()

state = engine.analyze(
    """
    He was terrified.

    Suddenly a shadow appeared.

    He shouted and ran.
    """
)

print(state.summary())

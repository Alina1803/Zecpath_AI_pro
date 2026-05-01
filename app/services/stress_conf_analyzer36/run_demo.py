from app.services.stress_conf_analyzer36.run_analyzer import analyze_behavior

text = "I think I am confident but maybe I need improvement"
duration = 6

result = analyze_behavior(text, duration)

print("\n=== Behavioral Analysis ===")
for k, v in result.items():
    print(f"{k}: {v}")
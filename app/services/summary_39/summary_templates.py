def generate_natural_summary(strengths, weaknesses, risks, culture_fit, decision):

    return f"""
The candidate demonstrates {', '.join(strengths[:2]) if strengths else 'some strengths'}.

However, there are concerns such as {', '.join(weaknesses[:2]) if weaknesses else 'minor weaknesses'}.

Risk factors include {', '.join(risks) if risks else 'no major risks'}.

Cultural fit is assessed as {culture_fit}.

Final Recommendation: {decision}.
"""